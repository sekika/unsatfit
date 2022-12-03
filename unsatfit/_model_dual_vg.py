# dual-VG model
import numpy as np


def init_model_vg2(self):
    self.model['DV'] = self.model['dual-VG'] = self.model['vg2'] = {
        'function': (self.vg2, self.vg2_k),
        'bound': self.bound_vg2,
        'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'a2', 'm2', 'Ks', 'p', 'q', 'r'],
        'k-only': [7, 8, 10]
    }
    self.model['DVCH'] = self.model['DVC'] = self.model['dual-VG-CH'] = self.model['vg2ch'] = {
        'function': (self.vg2ch, self.vg2ch_k),
        'bound': self.bound_vg2ch,
        'get_init': self.get_init_vg2ch,
        'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'm2', 'Ks', 'p', 'q', 'r'],
        'k-only': [6, 7, 9]
    }
    self.model['vg2chca'] = {
        'function': (self.vg2ch, self.vg2chca_k),
        'bound': self.bound_vg2ch,
        'get_init': self.get_init_vg2ch,
        'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'm2', 'Ks', 'p', 'q', 'a'],
        'k-only': [6, 7, 9]
    }


def bound_vg2(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
            self.b_a2, self.b_m, self.b_ks, self.b_p, self.b_q, self.b_r]


def vg2(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.vg2_se(p, x) * (p[0] - p[1]) + p[1]


def vg2_se(self, p, x):
    s1 = self.vg_se([p[3], p[4], p[7]], x)
    s2 = self.vg_se([p[5], p[6], p[7]], x)
    return p[2] * s1 + (1 - p[2]) * s2


def vg2_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, a1, m1, a2, m2, ks, p, q, r = par
    w1a1q = w * (a1 ** q)
    w2a2q = (1 - w) * (a2 ** q)
    s1 = self.vg_se([a1, m1, q], x)
    s2 = self.vg_se([a2, m2, q], x)
    bunshi = w1a1q * (1 - (1 - s1**(1 / m1))**m1) + \
        w2a2q * (1 - (1 - s2**(1 / m2))**m2)
    bunbo = w1a1q + w2a2q
    return ks * self.vg2_se(par[:7] + [q], x)**p * (bunshi / bunbo)**r

# dual-VG-CH model


def bound_vg2ch(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
            self.b_m, self.b_ks, self.b_p, self.b_q, self.b_r]


def vg2ch(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.vg2ch_se(p, x) * (p[0] - p[1]) + p[1]


def vg2ch_se(self, p, x):
    s1 = self.vg_se([p[3], p[4], p[6]], x)
    # s2 = self.vg_se([p[4], p[5], p[6]], x)
    s2 = self.vg_se([p[3], p[5], p[6]], x)  # Fixed
    return p[2] * s1 + (1 - p[2]) * s2


def vg2ch_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, a1, m1, m2, ks, p, q, r = par
    s1 = self.vg_se([a1, m1, q], x)
    s2 = self.vg_se([a1, m2, q], x)
    bunshi = w * (1 - (1 - s1**(1 / m1))**m1) + \
        (1 - w) * (1 - (1 - s2**(1 / m2))**m2)
    return ks * self.vg2ch_se(par[:6] + [q], x)**p * bunshi**r


def get_init_vg2ch(self):  # w, alpha, m1, m2
    from .unsatfit import Fit
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    a, m1 = f.get_init_vg()
    hb, l = f.get_init_bc()
    hc, max_hc = hb * (0.3, 0.1) ** (-1 / l)
    w = 1 / (1 + (hc / hb)**(-l))
    i = sum(x < max_hc)
    if len(x) - i > 1:
        x = np.log(x[i:] / hb)
        y = -np.log(y[i:] / (1 - w))
        l2 = self.linear_regress(x, y)
        if l2 < 0.01:
            l2 = 0.01
    else:
        l2 = 0
    n2 = l2 + 1
    m2 = 1 - 1 / n2
    f.set_model('vg2ch', const=[[1, 1], [2, 0], [
                3, w], [4, a], [6, m2], [9, 1]])
    f.ini = (m1)
    f.optimize()
    m1, = f.fitted
    f.set_model('vg2ch', const=[[1, 1], [2, 0], [9, 1]])
    f.ini = (w, a, m1, m2)
    f.optimize()
    if f.success:
        return f.fitted
    a, m = f.get_init_vg()
    f.ini = (0.5, a, m, m)
    f.optimize()
    if f.success:
        return f.fitted
    return f.ini


def get_wrf_vg2ch(self):
    from .unsatfit import Fit
    f = Fit()
    f.swrc = self.swrc
    f.debug = self.debug
    w, a, m1, m2 = f.get_init_vg2ch()
    f.set_model('vg2ch', const=['qr=0', 'q=1'])
    f.ini = (max(f.swrc[1]), w, a, m1, m2)
    f.optimize()
    if f.success:
        return (f.fitted[0], 0, *f.fitted[1:], 1)
    return (f.ini[0], 0, *f.ini[1:], 1)

# dual-VG-CH constant a model


def vg2chca_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, a1, m1, m2, ks, p, q, a = par
    n2 = q / (1 - m2)
    r = (a + p * q) / n2 - p
    s1 = self.vg_se([a1, m1, q], x)
    s2 = self.vg_se([a1, m2, q], x)
    bunshi = w * (1 - (1 - s1**(1 / m1))**m1) + \
        (1 - w) * (1 - (1 - s2**(1 / m2))**m2)
    return ks * self.vg2ch_se(par[:6] + [q], x)**p * bunshi**r
