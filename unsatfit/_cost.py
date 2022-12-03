# Cost function
import numpy as np


def residual_ht(self, p, x, y):
    return self.f_ht(p, x) - y


def residual_ln_hk(self, p, x, y):
    return np.log(self.f_hk(p, x) / y)


def residual_log10_hk(self, p, x, y):
    return np.log10(self.f_hk(p, x) / y)


def f_r2_ht(self, p, x, y):
    mse_ht = np.average(self.residual_ht(p, x, y)**2)
    return 1 - mse_ht / self.var_theta


def f_r2_ln_hk(self, p, x, y):
    mse_ln_hk = np.average(self.residual_ln_hk(p, x, y)**2)
    return 1 - mse_ln_hk / self.var_ln_k


def p_ht(self, p):
    p = list(p)
    for c in self.p_k_only:
        if c + 2 > len(p):
            p = p[:c]
        else:
            p = p[:c] + p[c + 1:]
    return p


def total_cost(self, p, x1, y1, x2, y2):
    r2 = self.f_r2_ht(self.p_ht(p), x1, y1) + self.f_r2_ln_hk(p, x2, y2)
    return 2 - r2
