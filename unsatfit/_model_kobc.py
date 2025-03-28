# KO1BC2 model
import numpy as np


def init_model_kobc(self):
    self.model['KOBC'] = self.model['KO1BC2'] = self.model['KB'] = self.model['kobc'] = {
        'function': (self.kobc, self.kobc_k),
        'bound': self.bound_kobc,
        'get_init': self.get_init_kobc,
        'get_wrf': self.get_wrf_kobc,
        'param': ['qs', 'qr', 'w1', 'hm1', 'sigma1', 'hb2', 'l2', 'Ks', 'p', 'q', 'r'],
        'k-only': [7, 8, 9, 10]
    }
    self.model['KOBCIP'] = self.model['KO1BC2-IP'] = self.model['KB-IP'] = self.model['kobcp2'] = {
        'function': (self.kobc, self.kobcp2_k),
        'bound': self.bound_kobcp2,
        'get_init': self.get_init_kobc,
        'get_wrf': self.get_wrf_kobc,
        'param': ['qs', 'qr', 'w1', 'hm1', 'sigma1', 'hb2', 'l2', 'Ks', 'p1', 'p2', 'q'],
        'k-only': [7, 8, 9, 10]
    }
    self.model['KOBCCH'] = self.model['KO1BC2-CH'] = self.model['KBC'] = self.model['kobcch'] = {
        'function': (self.kobcch, self.kobcch_k),
        'bound': self.bound_kobcch,
        'get_init': self.get_init_kobcch,
        'get_wrf': self.get_wrf_kobcch,
        'param': ['qs', 'qr', 'w1', 'hm', 'sigma1', 'l2', 'Ks', 'p', 'q', 'r'],
        'k-only': [6, 7, 8, 9]
    }
    self.model['KOBCCHIP'] = self.model['KO1BC2-CH-IP'] = self.model['KBC-IP'] = self.model['kobcchp2'] = {
        'function': (self.kobcch, self.kobcchp2_k),
        'bound': self.bound_kobcchp2,
        'get_init': self.get_init_kobcch,
        'get_wrf': self.get_wrf_kobcch,
        'param': ['qs', 'qr', 'w1', 'hm', 'sigma1', 'l2', 'Ks', 'p1', 'p2', 'q'],
        'k-only': [6, 7, 8, 9]
    }
    self.model['kobcchca'] = {
        'function': (self.kobcch, self.kobcchca_k),
        'bound': self.bound_kobcch,
        'get_init': self.get_init_kobcch,
        'get_wrf': self.get_wrf_kobcch,
        'param': ['qs', 'qr', 'w1', 'hm', 'sigma1', 'l2', 'Ks', 'p', 'a', 'r'],
        'k-only': [6, 7, 8, 9]
    }


def bound_kobc(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_hm1, self.b_sigma,
            self.b_hb2, self.b_lambda2, self.b_ks, self.b_p, self.b_q, self.b_r]


def kobc(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.kobc_se(p, x) * (p[0] - p[1]) + p[1]


def kobc_se(self, p, x):
    qs, qr, w, hm1, sigma1, hb2, l2 = p
    s1 = self.ln_se([hm1, sigma1], x)
    s2 = np.where(x < hb2, 1, (x / hb2) ** (-l2))
    return w * s1 + (1 - w) * s2


def kobc_k(self, p, x):
    from scipy.stats import norm
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, hm1, sigma1, hb2, l2, ks, p, q, r = par
    w1b1 = w * (hm1 ** (-q)) * np.exp((q * sigma1)**2 / 2)
    w2b2 = (1 - w) / hb2 ** q / (q / l2 + 1)
    s1 = 1 - norm.cdf(np.log(x / hm1) / sigma1 + q * sigma1)
    s2 = np.where(x < hb2, 1, (x / hb2) ** (-l2 - q))
    bunshi = w1b1 * s1 + w2b2 * s2
    bunbo = w1b1 + w2b2
    return ks * self.kobc_se(par[:7], x)**p * (bunshi / bunbo)**r


def get_init_kobc(self):  # w1, hm1, sigma1, hb2, l2
    from .unsatfit import Fit
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    w1, hm, sigma1, l2 = f.get_init_kobcch()
    f.set_model('kobc', const=[[1, 1], [2, 0]])
    f.ini = (w1, hm, sigma1, hm, l2)
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
        hm1, sigma1 = f.get_init_ko()
    except BaseException:
        return ch
    f.swrc = (h[i:], t[i:])
    try:
        hb2, l2 = f.get_init_bc()
    except BaseException:
        return ch
    f.set_model('kobc', const=['qs=1', 'qr=0'])
    f.swrc = (h, t)
    f.ini = (1 - t[i], hm1, sigma1, hb2, l2)
    f.optimize()
    if not f.success:
        return ch
    if ch_r2 > f.r2_ht:
        return ch
    return f.fitted


def get_wrf_kobc(self):
    from .unsatfit import Fit
    f = Fit()
    f.swrc = self.swrc
    f.debug = self.debug
    w1, hm1, sigma1, hb2, l2 = f.get_init_kobc()
    f.set_model('kobc', const=['qr=0'])
    f.ini = (max(f.swrc[1]), w1, hm1, sigma1, hb2, l2)
    f.optimize()
    if f.success:
        return (f.fitted[0], 0, *f.fitted[1:])
    qs, qr, w1, h1, s1, l2 = f.get_wrf_kobcch()
    return (qs, qr, w1, h1, s1, h1, l2)

# KO1BC2 model with r=1 and independent p1, p2


def bound_kobcp2(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_hm1, self.b_sigma,
            self.b_hb2, self.b_lambda2, self.b_ks, self.b_p, self.b_p, self.b_q]


def kobcp2_k(self, p, x):
    from scipy.stats import norm
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, hm1, sigma1, hb2, l2, ks, p1, p2, q = par
    w1b1 = w * (hm1 ** (-q)) * np.exp((q * sigma1)**2 / 2)
    w2b2 = (1 - w) / (hb2 ** q) / (q / l2 + 1)
    w1a1 = w1b1 * (1 - norm.cdf(np.log(x / hm1) / sigma1 + q * sigma1))
    w2a2 = w2b2 * (np.where(x < hb2, 1, (x / hb2) ** (-l2 - q)))
    # Seki et al. (2021) eq.(19)
    # s1 = 1 - norm.cdf(np.log(x / hm1)/sigma1)
    # s2 = np.where(x < hb2, 1, (x/hb2) ** (-l2))
    # bunshi = s1**p1 * w1a1 + s2**p2 * w2a2
    # Corrected from Si(h) to Se(h)
    se = self.kobc_se(par[:7], x)
    bunshi = se**p1 * w1a1 + se**p2 * w2a2  # Corrected
    bunbo = w1b1 + w2b2
    return ks * bunshi / bunbo

# KO1BC2-CH model


def bound_kobcch(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_hm1, self.b_sigma,
            self.b_lambda2, self.b_ks, self.b_p, self.b_q, self.b_r]


def kobcch(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.kobcch_se(p, x) * (p[0] - p[1]) + p[1]


def kobcch_se(self, p, x):
    qs, qr, w, h, sigma, l2 = p
    s1 = self.ln_se([h, sigma], x)
    s2 = np.where(x < h, 1, (x / h) ** (-l2))
    return w * s1 + (1 - w) * s2


def kobcch_k(self, p, x):
    from scipy.stats import norm
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, h, sigma, l2, ks, p, q, r = par
    w1b1 = w * (h ** (-q)) * np.exp((q * sigma)**2 / 2)
    w2b2 = (1 - w) / h ** q / (q / l2 + 1)
    s1 = 1 - norm.cdf(np.log(x / h) / sigma + q * sigma)
    s2 = np.where(x < h, 1, (x / h) ** (-l2 - q))
    bunshi = w1b1 * s1 + w2b2 * s2
    bunbo = w1b1 + w2b2
    return ks * self.kobcch_se(par[:6], x)**p * (bunshi / bunbo)**r


def get_init_kobcch(self):  # w1, hm, sigma1, l2
    from .unsatfit import Fit
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    w1, a, m1, l2 = f.get_init_vgbcch()
    if w1 < 0.1 or w1 > 0.9:
        w1, a, m1, m2 = f.get_init_vg2ch()
        n2 = 1 / (1 - m2)
        l2 = n2 - 1
    f.set_model('kobcch', const=[[1, 1], [2, 0]])
    if l2 < 0.01:
        l2 = 0.01
    if l2 > 3:
        l2 = 2.99
    n1 = 1 / (1 - m1)
    sigma1 = 1.2 * (n1 - 1)**(-0.8)
    if sigma1 > 2.99:
        sigma1 = 2.99
    ini = f.ini = (w1, 1 / a, sigma1, l2)
    f.b_sigma = (0, 3)
    f.b_lambda2 = (0.001, 3)
    f.optimize()
    if f.success:
        return f.fitted
    h, sigma = f.get_init_ln()
    if sigma > 2.99:
        sigma = 2.99
    f.ini = ([0.2, 0.8], [h, 1 / a], [sigma, ], [l2, ])
    f.optimize()
    if f.success:
        return f.fitted
    return ini


def get_wrf_kobcch(self):
    from .unsatfit import Fit
    f = Fit()
    f.swrc = self.swrc
    f.debug = self.debug
    w1, h1, s1, l2 = f.get_init_kobcch()
    f.set_model('kobcch', const=['qr=0'])
    qs = max(f.swrc[1])
    f.ini = (qs, w1, h1, s1, l2)
    f.b_sigma = (0, 4)
    f.optimize()
    if f.success:
        import copy
        f2 = copy.deepcopy(f)
        f.b_sigma = (0, np.inf)
        f.optimize()
        if f.success and f.r2_ht > f2.r2_ht:
            return (f.fitted[0], 0, *f.fitted[1:])
        else:
            return (f2.fitted[0], 0, *f2.fitted[1:])
    f.b_qs = (qs * 0.95, qs * 1.5)
    f.optimize()
    if f.success:
        return (f.fitted[0], 0, *f.fitted[1:])
    hb, hc, l1, l2 = f.get_init_bc2()
    w = 1 / (1 + (hc / hb)**(l2 - l1))
    s1 = 1.2 * l1**(-0.8)
    if s1 > 4:
        s1 = 4
    f.ini = (qs, w, hb, s1, l2)
    f.optimize()
    return (qs, 0, *f.ini[1:])

# KO1BC2-CH model with r=1 and independent p1, p2


def bound_kobcchp2(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_hm1, self.b_sigma,
            self.b_lambda2, self.b_ks, self.b_p, self.b_p, self.b_q]


def kobcchp2_k(self, p, x):
    from scipy.stats import norm
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, h, sigma, l2, ks, p1, p2, q = par
    w1b1 = w * (h ** (-q)) * np.exp((q * sigma)**2 / 2)
    w2b2 = (1 - w) / h ** q / (q / l2 + 1)
    w1a1 = w1b1 * (1 - norm.cdf(np.log(x / h) / sigma + q * sigma))
    w2a2 = w2b2 * (np.where(x < h, 1, (x / h) ** (-l2 - q)))
    # s1 = 1 - norm.cdf(np.log(x / h)/sigma)
    # s2 = np.where(x < h, 1, (x/h) ** (-l2))
    # bunshi = s1**p1 * w1a1 + s2**p2 * w2a2 # Seki et al. (2021) eq.(19)
    # Corrected from Si(h) to Se(h)
    se = self.kobcch_se(par[:6], x)
    bunshi = se**p1 * w1a1 + se**p2 * w2a2
    bunbo = w1b1 + w2b2
    return ks * bunshi / bunbo

# KO1BC2-CH model, constant a


def kobcchca_k(self, p, x):
    from scipy.stats import norm
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, h, sigma, l2, ks, p, a, r = par
    q = (a - p * l2) / r - l2
    w1b1 = w * (h ** (-q)) * np.exp((q * sigma)**2 / 2)
    w2b2 = (1 - w) / h ** q / (q / l2 + 1)
    s1 = 1 - norm.cdf(np.log(x / h) / sigma + q * sigma)
    s2 = np.where(x < h, 1, (x / h) ** (-l2 - q))
    bunshi = w1b1 * s1 + w2b2 * s2
    bunbo = w1b1 + w2b2
    return ks * self.kobcch_se(par[:6], x)**p * (bunshi / bunbo)**r
