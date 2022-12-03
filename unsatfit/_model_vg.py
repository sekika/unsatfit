# van Genuchten model
import numpy as np


def init_model_vg(self):
    self.model['van Genuchten'] = self.model['VG'] = self.model['vg'] = {
        'function': (self.vg, self.vg_k),
        'bound': self.bound_vg,
        'get_init': self.get_init_vg,
        'get_wrf': self.get_wrf_vg,
        'param': ['qs', 'qr', 'a', 'm', 'Ks', 'p', 'q', 'r'],
        'k-only': [4, 5, 7]
    }
    self.model['MVG'] = self.model['Modified VG'] = self.model['mvg'] = {
        'function': (self.mvg, self.mvg_k),
        'bound': self.bound_mvg,
        'param': ['qs', 'qr', 'a', 'm', 'hs', 'Ks', 'p', 'q', 'r'],
        'k-only': [5, 6, 8]
    }


def bound_vg(self):
    return [self.b_qs, self.b_qr, self.b_a, self.b_m,
            self.b_ks, self.b_p, self.b_q, self.b_r]


def vg(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.vg_se(p[2:5], x) * (p[0] - p[1]) + p[1]


def vg_se(self, p, x):
    a, m, q = p
    n = q / (1 - m)
    return (1 + (a * x)**n)**(-m)


def vg_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, a, m, ks, p, q, r = par
    s = self.vg_se([a, m, q], x)
    k = ks * s**p * (1 - (1 - s**(1 / m))**m)**r
    return k


def get_init_vg(self):  # alpha and m
    from .unsatfit import Fit
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.set_model('vg', const=[[1, 1], [2, 0], [7, 1]])
    f.swrc = (x, y)
    hb, l = f.get_init_bc()
    n = l + 1
    f.ini = (1 / hb, 1 - 1 / n)
    f.optimize()
    return f.fitted


def get_wrf_vg(self):
    from .unsatfit import Fit
    f = Fit()
    f.swrc = self.swrc
    f.debug = self.debug
    a, m = f.get_init_vg()
    f.set_model('vg', const=['q=1'])
    qs = max(f.swrc[1])
    f.ini = (qs, 0, a, m)
    f.b_a = (0, a * 100)
    f.optimize()
    if f.success:
        return (*f.fitted, 1)
    f.b_qs = (qs * 0.95, qs * 1.5)
    f.b_qr = (0, min(f.swrc[1]))
    f.optimize()
    if f.success:
        return (*f.fitted, 1)
    return (*f.ini, 1)

# Modified van Genuchten model (Vogel, 2000)


def bound_mvg(self):
    return [self.b_qs, self.b_qr, self.b_a, self.b_m,
            self.b_hs, self.b_ks, self.b_p, self.b_q, self.b_r]


def mvg(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.mvg_se(p[2:6], x) * (p[0] - p[1]) + p[1]


def mvg_se(self, p, x):
    a, m, hs, q = p
    n = q / (1 - m)
    sm = (1 + (a * hs)**n)**(m)
    return np.where(x < hs, 1, sm * (1 + (a * x)**n)**(-m))


def mvg_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, a, m, hs, ks, p, q, r = par
    s = self.vg_se([a, m, q], x)
    shs = self.vg_se([a, m, q], hs)
    ah = (1 - (1 - s**(1 / m))**m) / (1 - (1 - shs**(1 / m))**m)
    return np.where(x < hs, ks, ks * s**p * ah**r)
