# tri-VG model
import numpy as np


def init_model_tri_vg(self):
    self.model['TV'] = self.model['tri-VG'] = self.model['vg3'] = {
        'function': (self.vg3, self.vg3_k),
        'bound': self.bound_vg3,
        'get_init': self.get_init_vg3,
        # ww2 = w2 / (1-w1)
        # w2 was transformed to make the bound independent of w1
        'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'ww2', 'a2', 'm2', 'a3', 'm3', 'Ks', 'p', 'q', 'r'],
        'k-only': [10, 11, 13],
        'sort_param': self.sort_param_vg3
    }


def bound_vg3(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
            self.b_w1, self.b_a2, self.b_m, self.b_a2, self.b_m, self.b_ks, self.b_p, self.b_q, self.b_r]


def vg3(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.vg3_se(p, x) * (p[0] - p[1]) + p[1]


def vg3_se(self, p, x):
    s1 = self.vg_se([p[3], p[4], p[10]], x)
    s2 = self.vg_se([p[6], p[7], p[10]], x)
    s3 = self.vg_se([p[8], p[9], p[10]], x)
    w1 = p[2]
    w2 = (1 - w1) * p[5]
    return w1 * s1 + w2 * s2 + (1 - w1 - w2) * s3


def vg3_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, w1, a1, m1, ww2, a2, m2, a3, m3, ks, p, q, r = par
    w2 = (1 - w1) * ww2
    w1a1q = w1 * (a1 ** q)
    w2a2q = w2 * (a2 ** q)
    w3a3q = (1 - w1 - w2) * (a3 ** q)
    s1 = self.vg_se([a1, m1, q], x)
    s2 = self.vg_se([a2, m2, q], x)
    s3 = self.vg_se([a3, m3, q], x)
    bunshi = w1a1q * (1 - (1 - s1**(1 / m1))**m1) + \
        w2a2q * (1 - (1 - s2**(1 / m2))**m2) + \
        w3a3q * (1 - (1 - s3**(1 / m3))**m3)
    bunbo = w1a1q + w2a2q + w3a3q
    return ks * self.vg3_se(par[:10] + [q], x)**p * (bunshi / bunbo)**r


def get_init_vg3(self, a1=0):  # w1, alpha1, m1, ww2, alpha2, m2, alpha3, m3
    # w2 = (1-w1) * ww2
    if a1 > 0:
        return self.get_init_vg3_fix_a1(a1)
    from .unsatfit import Fit
    n_max = 8
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    w, a1, m1, a3, m3 = f.get_init_vg2()
    if a1 < a3:
        a1, a3 = a3, a1
        m1, m3 = m3, m1
        w = 1 - w
    m_max = 1 - 1 / n_max
    f.b_m = (0, m_max)
    f.b_a1 = self.b_a1
    f.b_a2 = self.b_a1
    f.b_a3 = self.b_a1
    if a1 < f.b_a1[0]:
        a1 = f.b_a1[0] * 1.0001
    if a1 > f.b_a1[1]:
        a1 = f.b_a1[1] * 0.9999
    if a3 < f.b_a3[0]:
        a3 = f.b_a3[0] * 1.0001
    if a3 > f.b_a3[1]:
        a3 = f.b_a3[1] * 0.9999
    f.set_model('vg3', const=[[1, 1], [2, 0], [9, a3], [10, m3], 'q=1'])
    r2 = 0
    for p in (0.05, 0.3, 0.6):
        f.ini = (w * p, a1, m1, w * (1 - p) / (1 - w * p), a1, m1)
        f.optimize()
        if r2 < f.r2_ht:
            fitted = f.fitted
            r2 = f.r2_ht
    f.set_model('vg3', const=[[1, 1], [2, 0], 'q=1'])
    f.ini = (*fitted, a3, m3)
    f.optimize()
    # sort
    w1, a1, m1, ww2, a2, m2, a3, m3 = f.fitted
    w2 = (1 - w1) * ww2
    param = ((w1, a1, m1), (w2, a2, m2), (1 - w1 - w2, a3, m3))
    ((w1, a1, m1), (w2, a2, m2), (w3, a3, m3)) = tuple(
        sorted(param, key=lambda x: x[1], reverse=True))
    f.fitted = w1, a1, m1, w2 / (1 - w1), a2, m2, a3, m3
    if f.success:
        ch = f.fitted
        ch_r2 = f.r2_ht
    else:
        ch = f.ini
        ch_r2 = f.f_r2_ht(f.ini, x, y)
    if len(x) < 10:
        return ch
    # Find a place to split to subfunctions
    try:
        c = np.polyfit(np.log10(x), y, 7)  # Fit with 7th degree
    except BaseException:
        return ch
    y_pred = np.polyval(c, np.log10(x))
    ss_res = np.sum((y - y_pred) ** 2)  # residual sum of squares
    ss_tot = np.sum((y - np.mean(y)) ** 2)  # total sum of squares
    r_squared = 1 - (ss_res / ss_tot)
    d = np.polyder(np.polyder(c))  # Second derivative
    split = []
    for root in np.roots(d):
        if root.imag == 0 and np.polyval(
                d, root + 0.01) < 0 and np.polyval(c, root) > 0.1:
            split.append(10**root.real)
    split.sort()
    if r_squared < 0.8 or len(split) < 2:
        return ch
    swrc = list(zip(*f.swrc))
    swrc_sort = sorted(swrc, key=lambda x: x[0])
    swrc = list(zip(*swrc_sort))
    h = np.array(swrc[0])
    t = np.array(swrc[1])
    i, j = np.searchsorted(h, split, side='right')[:2]
    if i < 4 or j - i < 3:
        return ch
    # Fit first subfunction
    f.swrc = (h[:i], t[:i] - t[i - 1])
    try:
        a1, m1 = f.get_init_vg()
    except BaseException:
        return ch
    if m1 > m_max:
        m1 = m_max
    if a1 < f.b_a1[0]:
        a1 = f.b_a1[0] * 1.0001
    if a1 > f.b_a1[1]:
        a1 = f.b_a1[1] * 0.9999
    # Fit second subfunction
    f.swrc = (h[i - 1:j], t[i - 1:j] - t[j - 1])
    try:
        a2, m2 = f.get_init_vg()
    except BaseException:
        return ch
    if m2 > m_max:
        m2 = m_max
    if a2 < f.b_a2[0]:
        a2 = f.b_a2[0] * 1.0001
    if a2 > f.b_a2[1]:
        a2 = f.b_a2[1] * 0.9999
    # Fit third subfunction
    f.swrc = (h[j - 1:], t[j - 1:])
    try:
        a3, m3 = f.get_init_vg()
    except BaseException:
        return ch
    if m3 > m_max:
        m3 = m_max
    if a3 < f.b_a3[0]:
        a3 = f.b_a3[0] * 1.0001
    if a3 > f.b_a3[1]:
        a3 = f.b_a3[1] * 0.9999
    # Final fitting
    w1 = 1 - t[i - 1]
    w2 = t[i - 1] - t[j - 1]
    ww2 = w2 / (1 - w1)
    f.set_model('vg3', const=['qs=1', 'qr=0', [3, w1], [6, ww2], 'q=1'])
    f.swrc = (h, t)
    f.ini = (a1, m1, a2, m2, a3, m3)
    f.optimize()
    a1, m1, a2, m2, a3, m3 = f.fitted
    f.set_model('vg3', const=['qs=1', 'qr=0', 'q=1'])
    f.ini = (w1, a1, m1, ww2, a2, m2, a3, m3)
    f.optimize()
    if not f.success:
        return ch
    if ch_r2 > f.r2_ht:
        return ch
    return f.fitted


def get_init_vg3_fix_a1(self, a1):  # w1, m1, ww2, alpha2, m2, alpha3, m3
    # w2 = (1-w1) * ww2
    from .unsatfit import Fit
    n_max = 8
    swrc = list(zip(*self.swrc))
    swrc_sort = sorted(swrc, key=lambda x: x[0])
    swrc = list(zip(*swrc_sort))
    x, t = swrc
    x = np.array(x)
    t = np.array(t)
    y = t / max(t)
    idx = np.searchsorted(x, 1 / a1)
    x_b = np.array(x[idx:])
    t_b = np.array(t[idx:])
    y_b = t_b / max(t_b)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x_b, y_b)  # for h>a/a1
    f.b_a1 = (0, a1)
    f.b_a2 = (0, min(1, self.b_a3[1]))
    w, a2, m2, a3, m3 = f.get_init_vg2()
    f.b_a1 = f.b_a2 = (0, a1)
    f.b_a3 = (0, min(1, self.b_a3[1]))
    if a2 < f.b_a2[0]:
        a2 = f.b_a2[0] * 1.0001
    if a2 > f.b_a2[1]:
        a2 = f.b_a2[1] * 0.9999
    if a3 < f.b_a3[0]:
        a3 = f.b_a3[0] * 1.0001
    if a3 > f.b_a3[1]:
        a3 = f.b_a3[1] * 0.9999
    if a2 < a3:
        a2, a3 = a3, a2
        m2, m3 = m3, m2
        w = 1 - w
    m_max = 1 - 1 / n_max
    f.swrc = (x, y)  # For all data
    f.b_m = (0, m_max)
    f.set_model('vg3', const=[[1, 1], [2, 0],
                f'a1={a1}', f'a3={a3}', f'm3={m3}', 'q=1'])
    r2 = 0
    for p in (0.05, 0.3, 0.6):
        f.ini = (w * p, m2, w * (1 - p) / (1 - w * p), a2, m2)
        f.optimize()
        if r2 < f.r2_ht:
            fitted = f.fitted
            r2 = f.r2_ht
    f.set_model('vg3', const=[[1, 1], [2, 0], f'a1={a1}', 'q=1'])
    f.ini = (*fitted, a3, m3)
    f.optimize()
    if f.success:
        ch = f.fitted
    else:
        ch = f.ini
    return ch


def sort_param_vg3(self, param):
    """Sort fitted

    After f.set_model('tri-VG'), this function can be called with f.sort_param()

    Sort parameters of tri-VG model in the reverse order of alpha

    ww2 is converted to w2

    Input: w1, alpha1, m1, ww2, alpha2, m2, alpha3, m3

    Return: w1, alpha1, m1, w2, alpha2, m2, alpha3, m3
    """
    w1, a1, m1, ww2, a2, m2, a3, m3 = param
    w2 = (1 - w1) * ww2
    param = ((w1, a1, m1), (w2, a2, m2), (1 - w1 - w2, a3, m3))
    ((w1, a1, m1), (w2, a2, m2), (_, a3, m3)) = tuple(
        sorted(param, key=lambda x: x[1], reverse=True))
    return w1, a1, m1, w2, a2, m2, a3, m3
