# Optimization
import numpy as np


def optimize(self):
    import copy
    import math
    from scipy import optimize, linalg  # type: ignore

    self.success = False

    if len(self.swrc) != 2:
        self.message = 'Error: No data of soil water retention curve.'
        return

    try:
        a = self.ini[0][0]
        gl = True
    except BaseException:
        gl = False
    if gl:
        f = self.multi_ini()
        if f.success:
            self.ini = f.fitted
        else:
            self.ini = f.ini

    self.mean_theta = np.average(self.swrc[1])
    self.var_theta = np.average((self.swrc[1] - self.mean_theta)**2)
    b = self.b_func()

    for c in sorted(self.const, reverse=True):
        b = b[:c[0] - 1] + b[c[0]:]

    if len(self.unsat) == 2:
        self.ht_only = False
        if min(self.unsat[1]) <= 0:
            self.message = 'Error: K should be positive.'
            return
        if 0 in self.f_hk(self.ini, self.unsat[0]):
            self.message = 'Overflow error: K(h) is too small and calculated as 0'
            return
        a = (self.swrc[0], self.swrc[1], self.unsat[0], self.unsat[1])
        cost = self.total_cost
        self.mean_k = np.average(self.unsat[1])
        self.var_k = np.average((self.unsat[1] - self.mean_k)**2)
        self.mean_ln_k = np.average(np.log(self.unsat[1]))
        self.var_ln_k = np.average(
            (np.log(self.unsat[1]) - self.mean_ln_k)**2)
    else:
        self.ht_only = True
        a = self.swrc
        cost = self.residual_ht
        for c in sorted(self.p_k_only, reverse=True):
            b = b[:c] + b[c + 1:]

    b = tuple(zip(*b))

    if self.debug:
        print('ini = {0}\nbounds = {1}'.format(
            self.ini, b))  # for debugging

    ini = self.ini
    success = False
    for ftol in self.lsq_ftol:
        result = optimize.least_squares(
            cost, ini, jac=self.lsq_jac, method=self.lsq_method, loss=self.lsq_loss,
            ftol=ftol, max_nfev=self.lsq_max_nfev, bounds=b, verbose=self.lsq_verbose, args=a)
        if result.success:
            ini = result.x
            success = True
            prev_result = copy.deepcopy(result)
        else:
            if success:
                result = copy.deepcopy(prev_result)
            break

    self.success = result.success  # True if convergence criteria is satisfied
    if not self.success:
        self.fitted = []
        self.message = result.message  # Verbal description of the termination reason
        return

    self.fitted = result.x  # Fitted parameters
    n = result.fun.size  # sample size
    k = self.fitted.size  # number of paramteres
    if self.ht_only:
        self.mse_ht = np.average(
            self.residual_ht(self.fitted, *self.swrc)**2)
        self.rss = self.mse_ht * n
        self.se_ht = math.sqrt(self.mse_ht)  # Standard error
        self.r2_ht = 1 - self.mse_ht / self.var_theta  # Coefficient of determination
        self.aic_ht = n * np.log(self.mse_ht) + 2 * k  # AIC
        if n - k - 1 > 0:
            self.aicc_ht = self.aic_ht + 2 * k * \
                (k + 1) / (n - k - 1)  # Corrected AIC
        else:
            self.aicc_ht = None
        # Uncertainty on fitted parameters
        # Section 15.4.2 of Numerical Recipes 3rd ed.
        # https://stackoverflow.com/questions/42388139/how-to-compute-standard-deviation-errors-with-scipy-optimize-least-squares
        self.jac = result.jac
        self.dof = n - k  # degree of freedom
        if self.dof <= 0:
            self.cov = self.perr = self.cor = None
            return
        U, s, Vh = linalg.svd(self.jac, full_matrices=False)
        tol = np.finfo(float).eps * s[0] * max(self.jac.shape)
        w = s > tol
        cov = (Vh[w].T / s[w]**2) @ Vh[w]  # robust covariance matrix
        # self.cov = linalg.inv(result.jac.T @ result.jac)  # Simpler way of
        # getting covariance matrix
        # Rescale the covariance matrix with data uncertanty
        cov *= self.rss / self.dof
        # 1 sigma uncertainty on fitted parameters
        self.perr = np.sqrt(np.diag(cov))
        Dinv = np.diag(1 / self.perr)
        self.cor = Dinv @ cov @ Dinv  # Correlation matrix
        self.message = self.format(
            self.param_ht, False).format(*self.fitted, self.r2_ht)
    else:
        p = list(self.fitted)
        for c in sorted(self.p_k_only, reverse=True):
            p = p[:c] + p[c + 1:]
        self.mse_ht = np.average(
            self.residual_ht(p, *self.swrc)**2)
        self.se_ht = math.sqrt(self.mse_ht)  # Standard error
        self.r2_ht = 1 - self.mse_ht / self.var_theta  # Coefficient of determination
        self.aic_ht = n * np.log(self.mse_ht) + 2 * k  # AIC
        if n - k - 1 > 0:
            self.aicc_ht = self.aic_ht + 2 * k * \
                (k + 1) / (n - k - 1)  # Corrected AIC
        else:
            self.aicc_ht = None
        self.mse_ln_hk = np.average(
            self.residual_ln_hk(self.fitted, *self.unsat)**2)
        n = len(self.unsat[0])
        self.rss = self.mse_ln_hk * n
        self.se_ln_hk = math.sqrt(self.mse_ln_hk)  # Standard error
        self.r2_ln_hk = 1 - self.mse_ln_hk / self.var_ln_k  # Coefficient of determination
        self.aic_ln_hk = n * np.log(self.mse_ln_hk) + 2 * k  # AIC
        self.aicc_ln_h = self.aic_ln_hk + 2 * k * \
            (k + 1) / (n - k - 1)  # Corrected AIC
        # Uncertainty is calculated only for SWRC
        self.jac = self.cov = self.perr = self.cor = None
        self.message = self.format(
            self.param, DualFitting=True).format(*self.fitted, self.r2_ht, self.r2_ln_hk)


def multi_ini(self):
    import copy
    import itertools
    comb = list(itertools.product(*self.ini))
    max_cost = -100000
    ftol = self.lsq_ftol
    self.lsq_ftol = self.lsq_ftol_global
    for ini in comb:
        self.ini = ini
        self.optimize()
        if self.success:
            if len(self.unsat) == 2:
                cost = self.r2_ht + self.r2_ln_hk
            else:
                cost = self.r2_ht
            if cost > max_cost:
                max_cost = cost
                max_f = copy.copy(self)
    self.lsq_ftol = ftol
    if max_cost == -100000:
        return self
    return max_f


def format(self, param, ShowR2=True, DualFitting=False):
    format = ''
    count = 0
    for i in param:
        format += i + ' = {' + str(count) + ':' + \
            self.output_format[i] + '} '
        count += 1
    if ShowR2:
        if DualFitting:
            format += 'R2 q = {' + str(count) + \
                ':' + self.r2_format + \
                '} R2 logK = {' + str(count + 1) + ':' + self.r2_format + '}'
        else:
            format += 'R2 = {' + str(count) + ':' + self.r2_format + '}'
    return format


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
