# dual-KO model
import numpy as np


def init_model_ln2(self):
    self.model['DK'] = self.model['dual-KO'] = self.model['ln2'] = {
        'function': (self.ln2, self.ln2_k),
        'bound': self.bound_ln2,
        'param': ['qs', 'qr', 'w1', 'hm1', 'sigma1', 'hm2', 'sigma2', 'Ks', 'p', 'q', 'r'],
        'k-only': [7, 8, 9, 10]
    }
    self.model['DKCH'] = self.model['dual-KO-CH'] = self.model['ln2ch'] = {
        'function': (self.ln2ch, self.ln2ch_k),
        'bound': self.bound_ln2ch,
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
