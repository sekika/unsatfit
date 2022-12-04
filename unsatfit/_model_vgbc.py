# VG1BC2 model
import numpy as np


def init_model_vgbc(self):
    self.model['VGBC'] = self.model['VG1BC2'] = self.model['VB'] = self.model['vgbc'] = {
        'function': (self.vgbc, self.vgbc_k),
        'bound': self.bound_vgbc,
        'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'hb2', 'l2', 'Ks', 'p', 'q', 'r'],
        'k-only': [7, 8, 10]
    }
    self.model['VGBCIP'] = self.model['VG1BC2-IP'] = self.model['VB-IP'] = self.model['vgbcp2'] = {
        'function': (self.vgbc, self.vgbcp2_k),
        'bound': self.bound_vgbcp2,
        'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'hb2', 'l2', 'Ks', 'p1', 'p2', 'q'],
        'k-only': [7, 8, 9]
    }
    self.model['VGBCCH'] = self.model['VG1BC2-CH'] = self.model['VBC'] = self.model['vgbcch'] = {
        'function': (self.vgbcch, self.vgbcch_k),
        'bound': self.bound_vgbcch,
        'get_init': self.get_init_vgbcch,
        'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'l2', 'Ks', 'p', 'q', 'r'],
        'k-only': [6, 7, 9]
    }
    self.model['VGBCCHIP'] = self.model['VG1BC2-CH-IP'] = self.model['VBC-IP'] = self.model['vgbcchp2'] = {
        'function': (self.vgbcchp2, self.vgbcchp2_k),
        'bound': self.bound_vgbcchp2,
        'get_init': self.get_init_vgbcch,
        'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'l2', 'Ks', 'p1', 'p2', 'q'],
        'k-only': [6, 7, 8]
    }


def bound_vgbc(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
            self.b_hb2, self.b_lambda2, self.b_ks, self.b_p, self.b_q, self.b_r]


def vgbc(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.vgbc_se(p, x) * (p[0] - p[1]) + p[1]


def vgbc_se(self, p, x):
    qs, qr, w, a1, m1, hb2, l2, q = p
    s1 = self.vg_se([a1, m1, q], x)
    s2 = np.where(x < hb2, 1, (x / hb2) ** (-l2))
    return w * s1 + (1 - w) * s2


def vgbc_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, a1, m1, hb2, l2, ks, p, q, r = par
    w1b1 = w * (a1 ** q)
    w2b2 = (1 - w) / hb2 ** q / (q / l2 + 1)
    s1 = self.vg_se([a1, m1, q], x)
    s1 = 1 - (1 - s1**(1 / m1))**m1
    s2 = np.where(x < hb2, 1, (x / hb2) ** (-l2 - q))
    bunshi = w1b1 * s1 + w2b2 * s2
    bunbo = w1b1 + w2b2
    return ks * self.vgbc_se(par[:7] + [q], x)**p * (bunshi / bunbo)**r

# VG1BC2 model with r=1 and independent p1, p2


def bound_vgbcp2(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
            self.b_hb2, self.b_lambda2, self.b_ks, self.b_p, self.b_p, self.b_q]


def vgbcp2_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, a1, m1, hb2, l2, ks, p1, p2, q = par
    w1b1 = w * (a1 ** q)
    w2b2 = (1 - w) / (hb2 ** q) / (q / l2 + 1)
    s1 = self.vg_se([a1, m1, q], x)
    w1a1 = w1b1 * (1 - (1 - s1**(1 / m1))**m1)
    w2a2 = w2b2 * (np.where(x < hb2, 1, (x / hb2) ** (-l2 - q)))
    # Seki et al. (2021) eq.(19)
    # s2 = np.where(x < hb2, 1, (x/hb2) ** (-l2))
    # Corrected from Si(h) to Se(h)
    se = self.vgbc_se(par[:7] + [q], x)
    bunshi = se**p1 * w1a1 + se**p2 * w2a2
    bunbo = w1b1 + w2b2
    return ks * bunshi / bunbo

# VG1BC2-CH model


def bound_vgbcch(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
            self.b_lambda2, self.b_ks, self.b_p, self.b_q, self.b_r]


def vgbcch(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.vgbcch_se(p, x) * (p[0] - p[1]) + p[1]


def vgbcch_se(self, p, x):
    qs, qr, w, a1, m1, l2, q = p
    hb2 = 1 / a1
    s1 = self.vg_se([a1, m1, q], x)
    # Ignore runtime warning, because divide by zero is warned when x=0
    import warnings
    warnings.simplefilter('ignore', category=RuntimeWarning)
    s2 = np.where(x < hb2, 1, (x / hb2) ** (-l2))
    return w * s1 + (1 - w) * s2


def vgbcch_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, a1, m1, l2, ks, p, q, r = par
    hb2 = 1 / a1
    w1b1 = w * (a1 ** q)
    w2b2 = (1 - w) / hb2 ** q / (q / l2 + 1)
    s1 = self.vg_se([a1, m1, q], x)
    s1 = 1 - (1 - s1**(1 / m1))**m1
    s2 = np.where(x < hb2, 1, (x / hb2) ** (-l2 - q))
    bunshi = w1b1 * s1 + w2b2 * s2
    bunbo = w1b1 + w2b2
    return ks * self.vgbcch_se(par[:6] + [q], x)**p * (bunshi / bunbo)**r


def get_init_vgbcch(self):  # w, alpha, m1, l2
    from .unsatfit import Fit
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    w, a, m1, m2 = f.get_init_vg2ch()
    f.set_model('vgbcch', const=[[1, 1], [2, 0], 'q=1'])
    n2 = 1 / (1 - m2)
    if n2 < 1.1:
        n2 = 1.1
    f.ini = (w, a, m1, n2 - 1)
    f.optimize()
    if f.success:
        return f.fitted
    hb, hc, l1, l2 = f.get_init_bc2()
    w = 1 / (1 + (hc / hb)**(l2 - l1))
    n1 = l1 + 1
    f.ini = (w, 1 / hb, 1 - 1 / n1, l2)
    f.optimize()
    if f.success:
        return f.fitted
    f.ini = (w, 1 / hb, m1, l2)
    f.optimize()
    if f.success:
        return f.fitted
    a, m = f.get_init_vg()
    f.b_w1 = (0.8, 1)
    f.ini = (0.99, a, m, 0.001)
    f.optimize()
    if f.success:
        return f.fitted
    return f.ini

# VG1BC2-CH model with r=1 and independent p1, p2


def bound_vgbcchp2(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
            self.b_lambda2, self.b_ks, self.b_p, self.b_p, self.b_q]


def vgbcchp2(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.vgbcch_se(p, x) * (p[0] - p[1]) + p[1]


def vgbcchp2_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, a1, m1, l2, ks, p1, p2, q = par
    hb2 = 1 / a1
    w1b1 = w * (a1 ** q)
    w2b2 = (1 - w) / (hb2 ** q) / (q / l2 + 1)
    s1 = self.vg_se([a1, m1, q], x)
    w1a1 = w1b1 * (1 - (1 - s1**(1 / m1))**m1)
    w2a2 = w2b2 * (np.where(x < hb2, 1, (x / hb2) ** (-l2 - q)))
    # Seki et al. (2021) eq.(19)
    # s2 = np.where(x < hb2, 1, (x/hb2) ** (-l2))
    # bunshi = s1**p1 * w1a1 + s2**p2 * w2a2
    # Corrected from Si(h) to Se(h)
    se = self.vgbcch_se(par[:6] + [q], x)
    bunshi = se**p1 * w1a1 + se**p2 * w2a2
    bunbo = w1b1 + w2b2
    return ks * bunshi / bunbo
