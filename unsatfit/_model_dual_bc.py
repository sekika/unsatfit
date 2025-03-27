# dual-BC model
import numpy as np


def init_model_bc2(self):
    self.model['DB'] = self.model['dual-BC'] = self.model['bc2f'] = {
        'function': (self.bc2f, self.bc2f_k),
        'bound': self.bound_bc2f,
        'get_init': self.get_init_bc2f,
        'get_wrf': self.get_wrf_bc2f,
        'param': ['qs', 'qr', 'w1', 'hb1', 'l1', 'hb2', 'l2', 'Ks', 'p', 'q', 'r'],
        'k-only': [7, 8, 9, 10]
    }
    self.model['DBCH'] = self.model['DBC'] = self.model['dual-BC-CH'] = self.model['bc2'] = {
        'function': (self.bc2, self.bc2_k),
        'bound': self.bound_bc2,
        'get_init': self.get_init_bc2,
        'get_wrf': self.get_wrf_bc2,
        'param': ['qs', 'qr', 'hb', 'hc', 'l1', 'l2', 'Ks', 'p', 'q', 'r'],
        'k-only': [6, 7, 8, 9]
    }
    self.model['bc2ca'] = {
        'function': (self.bc2, self.bc2ca_k),
        'bound': self.bound_bc2,
        'get_init': self.get_init_bc2,
        'get_wrf': self.get_wrf_bc2,
        'param': ['qs', 'qr', 'hb', 'hc', 'l1', 'l2', 'Ks', 'p', 'a', 'r'],
        'k-only': [6, 7, 8, 9]
    }


def bound_bc2f(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_hb, self.b_lambda1, self.b_hb2,
            self.b_lambda2, self.b_ks, self.b_p, self.b_q, self.b_r]


def bc2f(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.bc2f_se(p, x) * (p[0] - p[1]) + p[1]


def bc2f_se(self, p, x):
    qs, qr, w1, hb1, l1, hb2, l2 = p
    s1 = np.where(x < hb1, 1, (x / hb1) ** (-l1))
    s2 = np.where(x < hb2, 1, (x / hb2) ** (-l2))
    return w1 * s1 + (1 - w1) * s2


def bc2f_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w1, hb1, l1, hb2, l2, ks, p, q, r = par
    w1b1 = w1 / hb1 ** q / (q / l1 + 1)
    w2b2 = (1 - w1) / hb2 ** q / (q / l2 + 1)
    s1 = np.where(x < hb1, 1, (x / hb1) ** (-l1 - q))
    s2 = np.where(x < hb2, 1, (x / hb2) ** (-l2 - q))
    bunshi = w1b1 * s1 + w2b2 * s2
    bunbo = w1b1 + w2b2
    return ks * self.bc2f_se(par[:7], x)**p * (bunshi / bunbo)**r


def get_init_bc2f(self):
    from .unsatfit import Fit
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    hb, hc, l1, l2 = f.get_init_bc2()
    f.set_model('bc2f', const=['qs=1', 'qr=0'])
    w1 = 1 / (1 + (hc / hb)**(l2 - l1))
    f.ini = (w1, hb, l1, hb, l2)
    f.optimize()
    if f.success:
        ch = f.fitted
        ch_r2 = f.r2_ht
    else:
        ch = f.ini
        ch_r2 = f.f_r2_ht(f.ini, x, y)
    if len(x) < 6:
        return ch
    swrc = list(zip(*f.swrc))
    swrc_sort = sorted(swrc, key=lambda x: x[0])
    swrc = list(zip(*swrc_sort))
    h = np.array(swrc[0])
    t = np.array(swrc[1])
    t_med = (max(t) + min(t)) / 2
    for i in range(len(h)):
        if t[i] < t_med:
            break
    if i < 3:
        i = 3
    if i > len(h) - 3:
        i = len(h) - 3
    f.swrc = (h[:i], t[:i] - t[i])
    try:
        hb1, l1 = f.get_init_bc()
    except BaseException:
        return ch
    f.swrc = (h[i:], t[i:])
    try:
        hb2, l2 = f.get_init_bc()
    except BaseException:
        return ch
    f.set_model('DB', const=['qs=1', 'qr=0'])
    f.swrc = (h, t)
    f.ini = (1 - t[i], hb1, l1, hb2, l2)
    f.optimize()
    if not f.success:
        return ch
    if ch_r2 > f.r2_ht:
        return ch
    return f.fitted


def get_wrf_bc2f(self):
    from .unsatfit import Fit
    f = Fit()
    f.swrc = self.swrc
    f.debug = self.debug
    w1, hb1, l1, hb2, l2 = f.get_init_bc2f()
    f.set_model('bc2f', const=['qr=0'])
    f.ini = (max(f.swrc[1]), w1, hb1, l1, hb2, l2)
    f.optimize()
    if f.success:
        return (f.fitted[0], 0, *f.fitted[1:])
    return (f.ini[0], 0, *f.ini[1:])


# dual-BC-CH model


def bound_bc2(self):
    return [self.b_qs, self.b_qr, self.b_hb, self.b_hc, self.b_lambda1,
            self.b_lambda2, self.b_ks, self.b_p, self.b_q, self.b_r]


def bc2(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.bc2_se(p, x) * (p[0] - p[1]) + p[1]


def bc2_se(self, p, x):
    w = 1 / (1 + (p[3] / p[2])**(p[5] - p[4]))
    # Ignore runtime warning, because divide by zero is warned when x=0
    import warnings
    warnings.simplefilter('ignore', category=RuntimeWarning)
    s1 = (x / p[2]) ** (-p[4])
    s2 = (x / p[2]) ** (-p[5])
    return np.where(x < p[2], 1, w * s1 + (1 - w) * s2)


def bc2_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, hb, hc, l1, l2, ks, p, q, r = par
    w1 = 1 / (1 + (hc / hb)**(l2 - l1))
    w1b1 = w1 / (q / l1 + 1)
    w2b2 = (1 - w1) / (q / l2 + 1)
    s1 = np.where(x < hb, 1, (x / hb) ** (-l1 - q))
    s2 = np.where(x < hb, 1, (x / hb) ** (-l2 - q))
    bunshi = w1b1 * s1 + w2b2 * s2
    bunbo = w1b1 + w2b2
    return ks * self.bc2_se(par[:6], x)**p * (bunshi / bunbo)**r


def get_init_bc2(self):  # hb, hc, l1, l2
    from .unsatfit import Fit
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    hb, l = f.get_init_bc()
    min_hb = min(min(x[np.nonzero(x)]) / 5, hb / 2)
    max_hb, min_hc, hc, max_hc = hb * (0.8, 0.7, 0.3, 0.1) ** (-1 / l)
    f.b_hb = (min_hb, max_hb)
    f.b_hc = (min_hc, max_hc)
    i = sum(x < max_hc)
    if len(x) - i > 1:
        w = 1 / (1 + (hc / hb)**(-l))
        x = np.log(x[i:] / hb)
        y = -np.log(y[i:] / (1 - w))
        l2 = self.linear_regress(x, y)
        if l2 < 0.01:
            l2 = 0.01
    else:
        l2 = 0
    f.set_model('bc2', const=[[1, 1], [2, 0], [3, hb], [4, hc], [6, l2]])
    f.ini = (l)
    f.optimize()
    if f.success:
        l1, = f.fitted
    else:
        l1, = l,
    f.set_model('bc2', const=[[1, 1], [2, 0]])
    f.ini = (hb, hc, l1, l2)
    f.b_lambda1 = (min(l, l1), l1 + 2)
    f.b_lambda2 = (0, max(l, l2))
    f.optimize()
    if f.success:
        r2 = f.r2_ht
        fitted = f.fitted
    else:
        r2 = 0
    f.ini = (hb, hc, l, l / 5)
    f.b_lambda1 = (0, np.inf)
    f.b_lambda2 = (0, np.inf)
    f.optimize()
    if f.success:
        if f.r2_ht > r2:
            return f.fitted
        else:
            return fitted
    if r2 > 0:
        return fitted
    return f.ini


def get_wrf_bc2(self):
    from .unsatfit import Fit
    f = Fit()
    f.swrc = self.swrc
    f.debug = self.debug
    hb, hc, l1, l2 = f.get_init_bc2()
    f.set_model('bc2', const=['qr=0'])
    f.ini = (max(f.swrc[1]), hb, hc, l1, l2)
    f.optimize()
    if f.success:
        r2 = f.r2_ht
        fitted = (f.fitted[0], 0, *f.fitted[1:])
    else:
        r2 = 0
    hb, l = f.get_init_bc()
    f.ini = (max(f.swrc[1]), hb, hb, l * 5, l)
    f.optimize()
    if f.success:
        if f.r2_ht > r2:
            return (f.fitted[0], 0, *f.fitted[1:])
        else:
            return fitted
    if r2 > 0:
        return fitted
    return (f.ini[0], 0, *f.ini[1:])

# dual-BC-CH constant a model


def bc2ca_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, hb, hc, l1, l2, ks, p, a, r = par
    q = (a - p * l2) / r - l2
    w1 = 1 / (1 + (hc / hb)**(l2 - l1))
    w1b1 = w1 / (q / l1 + 1)
    w2b2 = (1 - w1) / (q / l2 + 1)
    s1 = np.where(x < hb, 1, (x / hb) ** (-l1 - q))
    s2 = np.where(x < hb, 1, (x / hb) ** (-l2 - q))
    bunshi = w1b1 * s1 + w2b2 * s2
    bunbo = w1b1 + w2b2
    return ks * self.bc2_se(par[:6], x)**p * (bunshi / bunbo)**r
