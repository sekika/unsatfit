# VVP model
import numpy as np


def init_model_vvp(self):
    self.model['VVP'] = self.model['tri-PDI'] = {
        'function': (self.vvp, self.vvp_k),
        'bound': self.bound_vvp,
        'get_init': self.get_init_vvp,
        # ww2 = w2 / (1-w1)
        'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'ww2', 'a2', 'm2', 'he', 'Ks', 'p', 'q', 'r', 'a'],
        'k-only': [9, 10, 12, 13]
    }
    self.model['VVPS'] = {
        'function': (self.vvps, self.vvps_k),
        'bound': self.bound_vvps,
        'get_init': self.get_init_vvps,
        # ww2 = w2 / (1-w1)
        'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'ww2', 'a2', 'm2', 'hf', 'he', 'Ks', 'p', 'q', 'r', 'a'],
        'k-only': [10, 11, 13, 14]
    }

# VG1VG2PE3


def bound_vvp(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
            self.b_w1, self.b_a2, self.b_m, self.b_he, self.b_ks, self.b_p, self.b_q, self.b_r, self.b_a]


def vvp(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.vvp_se(p, x) * (p[0] - p[1]) + p[1]


def vvp_se(self, p, x):
    qs, qr, w1, a1, m1, ww2, a2, m2, he, q = p[:10]
    w2 = (1 - w1) * ww2
    s1 = self.vg_se([a1, m1, q], x)
    s2 = self.vg_se([a2, m2, q], x)

    def L(h):
        return np.log(1 + a2 * h)
    s3 = np.where(x < 1 / a2, 1, (L(he) - L(x)) / (L(he) - np.log(2)))
    return w1 * s1 + w2 * s2 + (1 - w1 - w2) * s3


def vvp_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w1, a1, m1, ww2, a2, m2, he, ks, p, q, r, a = par
    # dual-VG component
    w2 = (1 - w1) * ww2
    w1a1q = w1 * (a1 ** q)
    w2a2q = w2 * (a2 ** q)
    s1 = self.vg_se([a1, m1, q], x)
    s2 = self.vg_se([a2, m2, q], x)
    bunshi = w1a1q * (1 - (1 - s1**(1 / m1))**m1) + \
        w2a2q * (1 - (1 - s2**(1 / m2))**m2)
    bunbo = w1a1q + w2a2q
    k12 = self.vvp_se(par[:9] + [q], x)**p * (bunshi / bunbo)**r
    # Film component
    k3 = np.where(x < 1 / a2, 1, (a2 * x) ** (-a))
    bunshi = (1 - w1 - w2) * (a2 ** q)
    bunbo = w1a1q + (1 - w1) * (a2 ** q)
    omega = self.vvp_se(par[:9] + [q], 1 / a2)**p * (bunshi / bunbo)**r
    kr = k12 * (1 - omega) + k3 * omega
    return ks * kr


def get_init_vvp(self, he):  # w1, a1, m1, ww2, a2, m2
    # w2 = (1-w1) * ww2
    from .unsatfit import Fit
    n_max = 8
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    w1, a1, m1, ww2, a2, m2, a3, m3 = f.get_init_vg3()
    m_max = 1 - 1 / n_max
    f.b_m = (0, m_max)
    w2, hm, sigma2 = f.get_init_pk(he)
    ww2 = w2 / (1 - w1)
    if ww2 > 1:
        ww2 = 0.99
    a2 = 1 / hm
    n2 = sigma2 ** (-1.25) / 1.2 + 1
    m2 = 1 - 1 / n2
    f.set_model('VVP', const=[[1, 1], [2, 0], [9, he], 'q=1'])
    m_max = 1 - 1 / n_max
    f.b_m = (0, m_max)
    f.b_a1 = self.b_a1
    f.b_a2 = self.b_a1
    if a1 < f.b_a1[0]:
        a1 = f.b_a1[0] * 1.0001
    if a1 > f.b_a1[1]:
        a1 = f.b_a1[1] * 0.9999
    if a2 < f.b_a2[0]:
        a2 = f.b_a2[0] * 1.0001
    if a2 > f.b_a2[1]:
        a2 = f.b_a2[1] * 0.9999
    if m1 > m_max:
        m1 = m_max * 0.9999
    if m2 > m_max:
        m2 = m_max * 0.9999
    f.ini = (w1, a1, m1, ww2, a2, m2)
    f.optimize()
    return f.fitted

# VG1VG2PE3, separate hf


def bound_vvps(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
            self.b_w1, self.b_a2, self.b_m, self.b_hb, self.b_he, self.b_ks, self.b_p, self.b_q, self.b_r, self.b_a]


def vvps(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.vvps_se(p, x) * (p[0] - p[1]) + p[1]


def vvps_se(self, p, x):
    qs, qr, w1, a1, m1, ww2, a2, m2, hf, he, q = p[:11]
    w2 = (1 - w1) * ww2
    s1 = self.vg_se([a1, m1, q], x)
    s2 = self.vg_se([a2, m2, q], x)

    def L(h):
        return np.log(1 + h / hf)
    s3 = np.where(x < hf, 1, (L(he) - L(x)) / (L(he) - np.log(2)))
    return w1 * s1 + w2 * s2 + (1 - w1 - w2) * s3


def vvps_k(self, p, x):
    # Requires update as vvp_k
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w1, a1, m1, ww2, a2, m2, hf, he, ks, p, q, r, a = par
    w2 = (1 - w1) * ww2
    w1a1q = w1 * (a1 ** q)
    w2a2q = w2 * (a2 ** q)
    s1 = self.vg_se([a1, m1, q], x)
    s2 = self.vg_se([a2, m2, q], x)
    bunshi = w1a1q * (1 - (1 - s1**(1 / m1))**m1) + \
        w2a2q * (1 - (1 - s2**(1 / m2))**m2)
    bunbo = w1a1q + w2a2q
    k12 = self.vvps_se(par[:10] + [q], x)**p * (bunshi / bunbo)**r
    k3 = np.where(x < hf, 1, (x / hf) ** (-a))
    w3b3 = (1 - w1 - w2) / (hf ** q)
    bunbo = w1a1q + w2a2q + w3b3
    omega = self.vvps_se(par[:10] + [q], hf)**p * (w3b3 / bunbo)**r
    return ks * (k12 * (1 - omega) + k3 * omega)


def get_init_vvps(self, he):  # w1, a1, m1, ww2, a2, m2, hf
    # w2 = (1-w1) * ww2
    from .unsatfit import Fit
    n_max = 8
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    w1, a1, m1, ww2, a2, m2, a3, m3 = f.get_init_vg3()
    f.set_model('VVPS', const=[[1, 1], [2, 0], [9, he], 'q=1'])
    f.ini = (w1, a1, m1, ww2, a2, m2, 1 / a3)
    m_max = 1 - 1 / n_max
    f.b_m = (0, m_max)
    f.b_a1 = self.b_a1
    f.b_a2 = self.b_a1
    f.optimize()
    return f.fitted
