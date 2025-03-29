# Fayer and Simmons model
import numpy as np


def init_model_fs(self):
    self.model['VGFS'] = self.model['Fayer-VG'] = self.model['vgfs'] = {
        'function': (self.vgfs, self.vgfs_k),
        'bound': self.bound_vgfs,
        'get_init': self.get_init_vgfs,
        'get_wrf': self.get_wrf_vgfs,
        'param': ['qs', 'qr', 'qa', 'a', 'm', 'he', 'Ks', 'p', 'q', 'r'],
        'k-only': [6, 7, 9]
    }


def bound_vgfs(self):
    return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
            self.b_he, self.b_ks, self.b_p, self.b_q, self.b_r]


def vgfs(self, p, x):
    p = list(p)
    for c in self.const_ht:
        p = p[:c[0] - 1] + [c[1]] + p[c[0] - 1:]
    return self.vgfs_se(p, x) * (p[0] - p[1]) + p[1]


def vgfs_se(self, p, x):
    qs, qr, qa, a, m, he, q = p
    vg = self.vg_se([a, m, q], x)
    xi = np.where(x > 1, 1 - np.log(x) / np.log(he), 1)
    xisa = xi * qa / qs
    return xisa + (1 - xisa) * vg


def vgfs_k(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr, qa, a, m, hm, ks, p, q, r = par
    if q != 1:  # Note that q should be 1
        return 1
    sa = qa / qs
    n = q / (1 - m)
    beta = 1
    gse = 1 - np.log(a / beta) / np.log(beta * hm) * \
        sa - sa  # 1 - gamma Se - Se

    def gamma(x, a, m, n, hm, sa, gse):
        w = 1 / (1 + (a * x)**n)
        wm = 1 / (1 + (a * hm)**n)

        def gs(w, m):
            s = 0
            for k in range(101):
                s += w**k / (m + 1 + k)
            return w**(m + 1) * s

        def h(w, m):
            return np.log(w) - m * w + m * (m - 1) * w * w / \
                4 - m * (m - 1) * (m - 2) * w**3 / 18

        def g(w, m):
            return np.where(w > 0.9, gs(0.9, m)
                            + h(0.1, m) - h(1 - w, m), gs(w, m))

        def f(w, m):
            return (1 - w)**m * (np.log((1 - w) / w) - 1 / m)

        def i3b(w, wm, m):
            return m * ((w - wm) + wm * (np.log(wm)) - w * np.log(w))

        w0 = max(10**(-10), wm)
        i1 = (1 - wm)**m - (1 - w)**m
        i2 = (1 / x - 1 / hm) / a + (1 - wm)**(m - 1) - (1 - w)**(m - 1)
        i3a = f(w0, m) - f(w, m) + g(1 - w, m) - g(1 - w0, m)
        i3 = np.where(w > w0, i3a + i3b(w0, wm, m), i3b(w, wm, m))
        result = i1 * a * gse + a * sa / np.log(hm) * (i2 + i3 / n)
        return result
    h0 = 0.025 / a
    hc = 10**(-7)  # Typical values for h_c range from 10^-7 to 10^-20

    def f(ah, n):
        return ah**(n - 1) * (np.log(ah) - 1 / (n - 1))

    gamma_0c = a * (gse + sa / n / np.log(hm)) * \
        ((a * h0)**(n - 1) - (a * hc)**(n - 1))
    gamma_0c += a * sa / np.log(hm) * (f(a * h0, n) - f(a * hc, n))
    gamma_max = gamma(h0, a, m, n, hm, sa, gse) + gamma_0c
    integral = gamma(x, a, m, n, hm, sa, gse) / gamma_max
    return ks * self.vgfs_se(par[:6] + [q], x)**p * integral**r


def get_init_vgfs(self, he):  # qa, a, m
    from .unsatfit import Fit
    x, t = self.swrc
    y = t / max(t)
    f = Fit()
    f.debug = self.debug
    f.swrc = (x, y)
    w, a, m, l2 = f.get_init_vgbcch()
    result = f.ini = (1 - w, a, m)
    f.set_model('vgfs', const=['qs=1', 'qr=0', [6, he], 'q=1'])
    f.optimize()
    if f.success:
        result = f.fitted
    return result


def get_wrf_vgfs(self, he):
    from .unsatfit import Fit
    f = Fit()
    f.swrc = self.swrc
    f.debug = self.debug
    qa, a, m = f.get_init_vgfs(he)
    f.set_model('vgfs', const=['qr=0', [6, he], 'q=1'])
    qs = max(f.swrc[1])
    f.ini = (qs, qa, a, m)
    f.optimize()
    if f.success:
        return (f.fitted[0], 0, *f.fitted[1:], he, 1)
    return (qs, 0, *f.ini[1:], he, 1)
