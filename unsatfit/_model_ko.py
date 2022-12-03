# Kosugi model
import numpy as np


def init_model_ln(self):
    self.model['Kosugi'] = self.model['KO'] = self.model['ln'] = {
        'function': (self.ln, self.ln_k),
        'bound': self.bound_ln,
        'get_init': self.get_init_ln,
        'get_wrf': self.get_wrf_ln,
        'param': ['qs', 'qr', 'hm', 'sigma', 'Ks', 'p', 'q', 'r'],
        'k-only': [4, 5, 6, 7],
    }


def bound_ln(self):
    return [self.b_qs, self.b_qr, self.b_hm, self.b_sigma,
            self.b_ks, self.b_p, self.b_q, self.b_r]


def ln(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    qs, qr, hm, s = p
    return self.ln_se([hm, s], x) * (qs - qr) + qr


def ln_se(self, p, x):
    from scipy.stats import norm  # type: ignore
    # Ignore runtime warning, because divide by zero is warned when x=0
    import warnings
    warnings.simplefilter('ignore', category=RuntimeWarning)
    return 1 - norm.cdf(np.log(x / p[0]) / p[1])


def ln_k(self, p, x):
    from scipy.stats import norm
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, hm, s, ks, p, q, r = par
    qq = 1 - norm.cdf(np.log(x / hm) / s + q * s)
    return ks * self.ln_se([hm, s], x)**p * qq**r


def get_init_ln(self):  # hm and sigma
    from .unsatfit import Fit
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.set_model('ln', const=[[1, 1], [2, 0]])
    f.swrc = (x, y)
    a, m = f.get_init_vg()
    n = 1 / (1 - m)
    s = 1.2 * (n - 1)**(-0.8)
    if s < 0.15:
        s = 0.15
    if s > 3:
        s = 3
    f.ini = (1 / a, s)
    f.b_sigma = (0, 3.2)
    f.optimize()
    return f.fitted


def get_wrf_ln(self):
    from .unsatfit import Fit
    f = Fit()
    f.swrc = self.swrc
    f.debug = self.debug
    hm, s = f.get_init_ln()
    f.set_model('ln', const=[])
    qs = max(f.swrc[1])
    if s > 2.4:
        s = 2.4
    f.ini = (qs, 0, hm, s)
    f.b_sigma = (0, 2.5)
    f.optimize()
    if f.success:
        f.b_sigma = (0, np.inf)
        import copy
        f2 = copy.deepcopy(f)
        f.optimize()
        if f.success:
            return f.fitted
        else:
            return f2.fitted
    hb, l = f.get_init_bc()
    sigma = 1.2 * l**(-0.8)
    if sigma > 2.5:
        sigma = 2.5
    f.ini = (qs, 0, hb, sigma)
    f.b_qs = (qs * 0.95, qs * 1.5)
    f.optimize()
    if f.success:
        return f.fitted
    return f.ini
