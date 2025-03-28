# Peters model
import numpy as np


def init_model_pe(self):
    self.model['PK'] = self.model['Peters-KO'] = self.model['Peters'] = self.model['PE'] = self.model['pk'] = {
        'function': (self.pk, self.pk_k),
        'bound': self.bound_pk,
        'get_init': self.get_init_pk,
        'get_wrf': self.get_wrf_pk,
        'param': ['qs', 'qr', 'w1', 'hm', 'sigma1', 'he', 'Ks', 'p', 'a', 'omega'],
        'k-only': [6, 7, 8, 9]
    }


def bound_pk(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_hm1, self.b_sigma,
            self.b_he, self.b_ks, self.b_p, self.b_a, self.b_w1]


def pk(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.pk_se(p, x) * (p[0] - p[1]) + p[1]


def pk_se(self, p, x):
    qs, qr, w, ha, sigma1, he = p
    s1 = self.ln_se([ha, sigma1], x)
    bunbo = np.log(1 + he / ha)
    xm = 1 / (1 - np.log(2) / bunbo)
    s2 = np.where(x < ha, 1, xm * (1 - np.log(1 + x / ha) / bunbo))
    return w * s1 + (1 - w) * s2


def pk_k(self, p, x):
    from scipy.stats import norm
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w, ha, sigma1, he, ks, p, a, omega = par
    s1 = 1 - norm.cdf(np.log(x / ha) / sigma1 + sigma1)
    k1 = self.pk_se(par[:6], x)**p * s1**2
    k2 = np.where(x < ha, 1, (x / ha) ** (-a))
    return ks * ((1 - omega) * k1 + omega * k2)


def get_init_pk(self, he):  # w1, hm, s1
    from .unsatfit import Fit
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    w1, h1, s1, l2 = f.get_init_kobcch()
    result = f.ini = (w1, h1, s1)
    f.set_model('Peters', const=[[1, 1], [2, 0], [6, he]])
    r2 = -1000
    f.b_sigma = (0, 3)
    for f.b_hm1 in [(h1 * 0.9, h1 * 1.1), (0, np.inf)]:
        f.optimize()
        if f.success and f.r2_ht > r2:
            result = f.fitted
            r2 = f.r2_ht
    if r2 < 0.8:
        f.b_sigma = (0, 5)
        hm, sigma = f.get_init_ln()
        if sigma > 4:
            sigma = 4
        w1, a, m1, l2 = f.get_init_vgbcch()
        n1 = 1 / (1 - m1)
        sigma1 = 1.2 * (n1 - 1)**(-0.8)
        if sigma1 > 3:
            sigma1 = 3
        f.ini = [(0.05, 0.95), (h1, hm, 1 / a), (sigma1, sigma, s1)]
        f.optimize()
        if f.success and f.r2_ht > r2:
            result = f.fitted
            r2 = f.r2_ht
    return result


def get_wrf_pk(self, he):
    from .unsatfit import Fit
    f = Fit()
    f.swrc = self.swrc
    f.debug = self.debug
    w1, hm, s1 = f.get_init_pk(he)
    if s1 > 2.5:
        s1 = 2.5
    f.set_model('pk', const=['qr=0', [6, he]])
    qs = max(f.swrc[1])
    f.ini = (qs, w1, hm, s1)
    f.b_sigma = (0, 2.5)
    f.b_qs = (qs * 0.95, qs * 3)
    f.optimize()
    if f.success:
        import copy
        f2 = copy.deepcopy(f)
        f.b_sigma = (0, 3)
        f.optimize()
        if f.success and f.r2_ht > f2.r2_ht:
            return (f.fitted[0], 0, *f.fitted[1:], he)
        else:
            return (f2.fitted[0], 0, *f2.fitted[1:], he)
    f.b_qs = (qs * 0.95, qs * 1.2)
    f.optimize()
    if f.success:
        return (f.fitted[0], 0, *f.fitted[1:], he)
    return (qs, 0, *f.ini[1:], he)
