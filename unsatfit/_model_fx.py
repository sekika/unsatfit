# Fredlund and Xing model
import numpy as np


def init_model_fx(self):
    self.model['FX'] = self.model['fx'] = {
        'function': (self.fx, False),
        'bound': self.bound_fx,
        'get_init': self.get_init_fx,
        'get_wrf': self.get_wrf_fx,
        'param': ['qs', 'qr', 'a', 'm', 'n'],
        'k-only': []
    }


def bound_fx(self):
    return [self.b_qs, self.b_qr, self.b_fxa, self.b_fxm, self.b_fxn]


def fx(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.fx_se(p[2:], x) * (p[0] - p[1]) + p[1]


def fx_se(self, p, x):
    a, m, n = p
    return (np.log(np.e + (x / a)**n))**(-m)


def get_init_fx(self):  # a, m, n
    from .unsatfit import Fit
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.set_model('fx', const=[[1, 1], [2, 0]])
    f.swrc = (x, y)
    a, m = f.get_init_vg()
    n = 1 / (1 - m)
    vg = f.ini = (1 / a, 2.54 * (1 - 1 / n), 0.95 * n)
    f.optimize()
    if f.success:
        return f.fitted
    hm, sigma = f.get_init_ln()
    f.ini = (hm, 2.54, 1.52 / sigma)
    f.optimize()
    if f.success:
        return f.fitted
    hb, l = f.get_init_bc()
    n = l + 1
    f.ini = (hb, 2.54 * (1 - 1 / n), 0.95 * n)
    f.optimize()
    if f.success:
        return f.fitted
    f.set_model('fx', const=[[2, 0]])
    f.ini = (1, *vg)
    f.optimize()
    if f.success:
        return f.fitted[1:]
    return vg


def get_wrf_fx(self):
    from .unsatfit import Fit
    f = Fit()
    f.swrc = self.swrc
    f.debug = self.debug
    a, m, n = f.get_init_fx()
    f.set_model('fx', const=[])
    qs = max(f.swrc[1])
    f.ini = (qs, 0, a, m, n)
    f.optimize()
    if f.success:
        return f.fitted
    f.b_qs = (qs * 0.95, qs * 1.5)
    f.b_qr = (0, min(f.swrc[1]))
    f.optimize()
    if f.success:
        return f.fitted
    return f.ini
