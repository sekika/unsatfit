# Modified model

import numpy as np


def modified_model(self, hs):
    """Modified model introducing air entry head
    Call modified_model(hs) after set_model()

    Requirement: param starts with (qs, qr) and k_only starts with Ks
    """
    import copy
    self.hs = hs
    self.f_ht_org = copy.deepcopy(self.f_ht)
    self.f_hk_org = copy.deepcopy(self.f_hk)
    self.f_ht = self.modified_ht
    self.f_hk = self.modified_hk
    self.model_name = "Modified " + self.model_name
    self.model_description = self.model_name + \
        ' model (hs = ' + str(hs) + ') with ' + self.const_description


def modified_ht(self, p, x):
    par = list(p)
    for c in self.const_ht:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    qs, qr = par[:2]
    modify = (qs - qr) / (self.f_ht_org(p, self.hs) - qr)
    se = (self.f_ht_org(p, x) - qr) / (qs - qr)
    return np.where(x < self.hs, qs, modify * se * (qs - qr) + qr)


def modified_hk(self, p, x):
    par = list(p)
    for c in self.const:
        par = par[:c[0] - 1] + [c[1]] + par[c[0] - 1:]
    ks = par[self.model_k_only[0]]
    modify = ks / self.f_hk_org(p, self.hs)
    k = self.f_hk_org(p, x)
    return np.where(x < self.hs, ks, modify * k)
