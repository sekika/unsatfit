# BVV model
import numpy as np


def init_model_bvv(self):
    self.model['BVV'] = self.model['BC1VG2VG3'] = {
        'function': (self.bvv, self.bvv_k),
        'bound': self.bound_bvv,
        'get_init': self.get_init_bvv,
        # ww2 = w2 / (1-w1)
        # w2 was transformed to make the bound independent of w1
        'param': ['qs', 'qr', 'w1', 'hb1', 'l1', 'ww2', 'a2', 'm2', 'a3', 'm3', 'Ks', 'p', 'q', 'r'],
        'k-only': [10, 11, 13]
    }


def bound_bvv(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_hb, self.b_lambda,
            self.b_w1, self.b_a2, self.b_m, self.b_a2, self.b_m, self.b_ks, self.b_p, self.b_q, self.b_r]


def bvv(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.bvv_se(p, x) * (p[0] - p[1]) + p[1]


def bvv_se(self, p, x):
    s1 = np.where(x < p[3], 1, (x / p[3]) ** (-p[4]))
    s2 = self.vg_se([p[6], p[7], p[10]], x)
    s3 = self.vg_se([p[8], p[9], p[10]], x)
    w1 = p[2]
    w2 = (1 - w1) * p[5]
    return w1 * s1 + w2 * s2 + (1 - w1 - w2) * s3


def bvv_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w1, hb1, l1, ww2, a2, m2, a3, m3, ks, p, q, r = par
    w2 = (1 - w1) * ww2
    w1a1q = w1 / hb1 ** q / (q / l1 + 1)
    w2a2q = w2 * (a2 ** q)
    w3a3q = (1 - w1 - w2) * (a3 ** q)
    s1 = np.where(x < hb1, 1, (x / hb1) ** (-l1 - q))
    s2 = self.vg_se([a2, m2, q], x)
    s3 = self.vg_se([a3, m3, q], x)
    bunshi = w1a1q * s1 + \
        w2a2q * (1 - (1 - s2**(1 / m2))**m2) + \
        w3a3q * (1 - (1 - s3**(1 / m3))**m3)
    bunbo = w1a1q + w2a2q + w3a3q
    return ks * self.bvv_se(par[:10] + [q], x)**p * (bunshi / bunbo)**r


def get_init_bvv(self, hb1=0):  # w1, hb1, l1, ww2, alpha2, m2, alpha3, m3
    # w2 = (1-w1) * ww2
    if hb1 > 0:
        return self.get_init_bvv_fix_hb1(hb1)
    from .unsatfit import Fit
    n_max = 8
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    if self.b_hb[0] > 0:
        f.b_a1 = f.b_a2 = f.b_a3 = (0, 1 / self.b_hb[0])
    w1, a1, m1, ww2, a2, m2, a3, m3 = f.get_init_vg3()
    m_max = 1 - 1 / n_max
    f.b_m = (0, m_max)
    f.b_hb = self.b_hb
    f.set_model('BVV', const=[[1, 1], [2, 0], [3, w1], [6, ww2], [
                7, a2], [8, m2], [9, a3], [10, m3], 'q=1'])
    f.ini = (max(1 / a1, f.b_hb[0] * 1.001), 1 / (1 - m1) - 1)
    f.optimize()
    hb1, l1 = f.fitted
    f.set_model('BVV', const=[[1, 1], [2, 0], 'q=1'])
    f.ini = (w1, hb1, l1, ww2, a2, m2, a3, m3)
    f.optimize()
    return f.fitted


def get_init_bvv_fix_hb1(self, hb1):  # w1, l1, ww2, alpha2, m2, alpha3, m3
    # w2 = (1-w1) * ww2
    from .unsatfit import Fit
    n_max = 8
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    f.b_a2 = f.b_a3 = (0, 1 / hb1)
    w1, m1, ww2, a2, m2, a3, m3 = f.get_init_vg3(a1=1 / hb1)
    m_max = 1 - 1 / n_max
    f.b_m = (0, m_max)
    f.b_hb = self.b_hb
    f.set_model('BVV', const=[[1, 1], [2, 0], [3, w1], [4, hb1], [6, ww2], [
                7, a2], [8, m2], [9, a3], [10, m3], 'q=1'])
    f.ini = (1 / (1 - m1) - 1)
    f.optimize()
    l1 = f.fitted[0]
    f.set_model('BVV', const=[[1, 1], [2, 0], [4, hb1], 'q=1'])
    f.ini = (w1, l1, ww2, a2, m2, a3, m3)
    f.optimize()
    return f.fitted
