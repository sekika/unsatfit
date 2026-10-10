# Brooks and Corey model
import numpy as np


def init_model_bc(self):
    self.model['Brooks and Corey'] = self.model['BC'] = self.model['bc'] = {
        # Water retention and hydraulic conductivity functions
        'function': (self.bc, self.bc_k),
        # Bound of paramters
        'bound': self.bound_bc,
        # Name of parameters
        'param': ['qs', 'qr', 'hb', 'l', 'Ks', 'p', 'q', 'r'],
        # Function to get initial WRF parameters except qs, qr
        'get_init': self.get_init_bc,
        # Function to get initial WRF parameters
        'get_wrf': self.get_wrf_bc,
        # Index of parameters (starting from 0) used only for K function
        'k-only': [4, 5, 6, 7]
    }


def bound_bc(self):
    return [self.b_qs, self.b_qr, self.b_hb, self.b_lambda,
            self.b_ks, self.b_p, self.b_q, self.b_r]


def bc(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.bc_se(p, x) * (p[0] - p[1]) + p[1]


def bc_se(self, p, x):
    # Ignore runtime warning, because divide by zero is warned when x=0
    import warnings
    warnings.simplefilter('ignore', category=RuntimeWarning)
    return np.where(x < p[2], 1, (x / p[2]) ** (-p[3]))


def bc_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, hb, l, ks, p, q, r = par
    s = self.bc_se(par[:4], x)
    k = ks * s**p * (np.where(x < hb, 1, (x / hb) ** (-l - q)))**r
    return k


def get_init_bc(self):  # hb and lambda
    import math
    from .unsatfit import Fit
    swrc = list(zip(*self.swrc))
    swrc_sort = sorted(swrc, key=lambda x: x[0])
    swrc = list(zip(*swrc_sort))
    x, t = swrc
    y = t / max(t)
    hbi = sum(y > 0.95 + min(y) * 0.05)
    hli = sum(y > 0.15 + min(y) * 0.85)
    if hbi == hli:
        hli = hli + 1
    if hbi > hli:
        hbi = hbi - 1
        hli = hbi + 1
    hb = x[hbi]
    if hb == 0:
        hb = x[2] / 10
    l = -math.log(y[hli] / y[hbi]) / math.log(x[hli] / hb)
    if l < 0.1:
        l = 0.1
    if l > 10:
        l = 10
    f = Fit()
    f.set_model('bc', const=[[1, 1], [2, 0]])
    f.swrc = (x, y)
    f.ini = (hb, l)
    f.optimize()
    hb, l = f.fitted
    r2 = f.r2_ht
    if r2 < 0.6:
        f.set_model('bc', const=[[2, 0]])
        f.ini = (1, *f.ini)
        f.optimize()
        if f.r2_ht > r2:
            hb, l = f.fitted[1:]
    return hb, l


def get_wrf_bc(self):
    from .unsatfit import Fit
    f = Fit()
    f.swrc = self.swrc
    f.debug = self.debug
    hb, l = f.get_init_bc()
    f.set_model('bc', const=[])
    f.ini = (max(f.swrc[1]), 0, hb, l)
    f.optimize()
    if f.success:
        return f.fitted
    return f.ini
