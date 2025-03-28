# dual-KO model
import numpy as np


def init_model_ln2(self):
    self.model['DK'] = self.model['dual-KO'] = self.model['ln2'] = {
        'function': (self.ln2, self.ln2_k),
        'bound': self.bound_ln2,
        'get_init': self.get_init_ln2,
        'get_wrf': self.get_wrf_ln2,
        'param': ['qs', 'qr', 'w1', 'hm1', 'sigma1', 'hm2', 'sigma2', 'Ks', 'p', 'q', 'r'],
        'k-only': [7, 8, 9, 10]
    }
    self.model['DKCH'] = self.model['DKC'] = self.model['dual-KO-CH'] = self.model['ln2ch'] = {
        'function': (self.ln2ch, self.ln2ch_k),
        'bound': self.bound_ln2ch,
        'get_init': self.get_init_ln2ch,
        'get_wrf': self.get_wrf_ln2ch,
        'param': ['qs', 'qr', 'w1', 'hm1', 'sigma1', 'sigma2', 'Ks', 'p', 'q', 'r'],
        'k-only': [6, 7, 8, 9]
    }


def bound_ln2(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_hm1, self.b_sigma,
            self.b_hm2, self.b_sigma, self.b_ks, self.b_p, self.b_q, self.b_r]


def ln2(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.ln2_se(p, x) * (p[0] - p[1]) + p[1]


def ln2_se(self, p, x):
    s1 = self.ln_se([p[3], p[4]], x)
    s2 = self.ln_se([p[5], p[6]], x)
    return p[2] * s1 + (1 - p[2]) * s2


def ln2_k(self, p, x):
    from scipy.stats import norm
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, hm1, s1, hm2, s2, ks, p, q, r = par
    w1b1 = w * np.exp((q * s1)**2 / 2) / (hm1 ** q)
    w2b2 = (1 - w) * np.exp((q * s2)**2 / 2) / (hm2 ** q)
    q1 = 1 - norm.cdf(np.log(x / hm1) / s1 + q * s1)
    q2 = 1 - norm.cdf(np.log(x / hm2) / s2 + q * s2)
    bunshi = w1b1 * q1 + w2b2 * q2
    bunbo = w1b1 + w2b2
    return ks * self.ln2_se(par[:7], x)**p * (bunshi / bunbo)**r


def get_init_ln2(self):  # w1, hm1, sigma1, hm2, sigma2
    from .unsatfit import Fit
    sigma_min = 0.2
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    w1, hm, sigma1, sigma2 = f.get_init_ln2ch()
    if sigma1 < sigma_min:
        sigma1 = sigma_min + 0.01
    if sigma2 < sigma_min:
        sigma2 = sigma_min + 0.01
    if sigma2 > 3:
        sigma2 = 3
    f.set_model('ln2', const=[[1, 1], [2, 0]])
    f.ini = (w1, hm, sigma1, hm, sigma2)
    f.b_sigma = (sigma_min, np.inf)
    f.optimize()
    if f.success:
        ch = f.fitted
        ch_r2 = f.r2_ht
    else:
        ch = f.ini
        ch_r2 = f.f_r2_ht(f.ini, x, y)
    if len(x) < 6:
        return ch
    w1, a1, m1, a2, m2 = f.get_init_vg2()
    hm1 = 1 / a1
    n1 = 1 / (1 - m1)
    sigma1 = 1.2 * (n1 - 1) ** (-0.8)
    if sigma1 < sigma_min:
        sigma1 = sigma_min + 0.01
    hm2 = 1 / a2
    n2 = 1 / (1 - m2)
    sigma2 = 1.2 * (n2 - 1) ** (-0.8)
    if sigma2 < sigma_min:
        sigma2 = sigma_min + 0.01
    if sigma2 > 3:
        sigma2 = 3
    f.set_model('ln2', const=[[1, 1], [2, 0]])
    f.ini = (w1, hm1, sigma1, hm2, sigma2)
    f.b_sigma = (sigma_min, np.inf)
    f.optimize()
    if not f.success:
        return ch
    if ch_r2 > f.r2_ht:
        return ch
    return f.fitted


def get_wrf_ln2(self):
    from .unsatfit import Fit
    sigma_min = 0.2
    f = Fit()
    f.swrc = self.swrc
    f.debug = self.debug
    w1, hm1, sigma1, hm2, sigma2 = f.get_init_ln2()
    f.set_model('ln2', const=['qr=0'])
    f.ini = (max(f.swrc[1]), w1, hm1, sigma1, hm2, sigma2)
    f.sigma_min = (sigma_min, np.inf)
    f.optimize()
    if f.success:
        return (f.fitted[0], 0, *f.fitted[1:])
    return (f.ini[0], 0, *f.ini[1:])

# dual-KO-CH model


def bound_ln2ch(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_hm1, self.b_sigma,
            self.b_sigma, self.b_ks, self.b_p, self.b_q, self.b_r]


def ln2ch(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.ln2ch_se(p, x) * (p[0] - p[1]) + p[1]


def ln2ch_se(self, p, x):
    s1 = self.ln_se([p[3], p[4]], x)
    s2 = self.ln_se([p[3], p[5]], x)
    return p[2] * s1 + (1 - p[2]) * s2


def ln2ch_k(self, p, x):
    from scipy.stats import norm
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, hm1, s1, s2, ks, p, q, r = par
    w1b1 = w * np.exp((q * s1)**2 / 2) / (hm1 ** q)
    w2b2 = (1 - w) * np.exp((q * s2)**2 / 2) / (hm1 ** q)
    q1 = 1 - norm.cdf(np.log(x / hm1) / s1 + q * s1)
    q2 = 1 - norm.cdf(np.log(x / hm1) / s2 + q * s2)
    bunshi = w1b1 * q1 + w2b2 * q2
    bunbo = w1b1 + w2b2
    return ks * self.ln2ch_se(par[:6], x)**p * (bunshi / bunbo)**r


def get_init_ln2ch(self):  # w1, hm, sigma1, sigma2
    from .unsatfit import Fit
    sigma_min = 0.2
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    f.sigma = (sigma_min, np.inf)
    w1, a1, m1, m2 = f.get_init_vg2ch()
    hm = 1 / a1
    n1 = 1 / (1 - m1)
    sigma1 = 1.2 * (n1 - 1) ** (-0.8)
    if sigma1 < sigma_min:
        sigma1 = sigma_min + 0.01
    if sigma1 > 3:
        sigma1 = 2.99
    n2 = 1 / (1 - m2)
    sigma2 = 1.2 * (n2 - 1) ** (-0.8)
    if sigma2 < sigma_min:
        sigma2 = sigma_min + 0.01
    if sigma2 > 3:
        sigma2 = 2.99
    f.set_model('ln2ch', const=[[1, 1], [2, 0]])
    f.b_sigma = (sigma_min, 3)
    f.ini = (w1, hm, sigma1, sigma2)
    f.optimize()
    if f.success:
        return f.fitted
    hm, sigma = f.get_init_ln()
    f.ini = (0.5, hm, sigma, sigma)
    f.optimize()
    if f.success:
        return f.fitted
    return f.ini


def get_wrf_ln2ch(self):
    from .unsatfit import Fit
    f = Fit()
    f.swrc = self.swrc
    f.debug = self.debug
    w1, hm, sigma1, sigma2 = f.get_init_ln2ch()
    f.set_model('ln2ch', const=['qr=0'])
    f.ini = (max(f.swrc[1]), w1, hm, sigma1, sigma2)
    f.b_sigma = (0.2, 3)
    f.optimize()
    if f.success:
        return (f.fitted[0], 0, *f.fitted[1:])
    return (f.ini[0], 0, *f.ini[1:])
