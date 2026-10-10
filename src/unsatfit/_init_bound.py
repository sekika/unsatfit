def init_bound(self):
    """Set initial bound of parameters

    Each bound is set as tuple of (minimum, maximum)
    """
    import numpy as np
    self.b_qs = self.b_qr = (0, np.inf)
    self.b_qa = self.b_w1 = self.b_m = (0, 1)
    self.b_a = self.b_a1 = self.b_a2 = self.b_hm = self.b_hm1 = self.b_hm2 = self.b_sigma = self.b_he = (
        0, np.inf)
    self.b_hb = self.b_hb2 = self.b_hc = self.b_hs = self.b_lambda = self.b_lambda1 = self.b_lambda2 = (
        0, np.inf)
    self.b_fxa = self.b_fxm = self.b_fxn = (0, np.inf)
    self.b_ks = self.b_p = self.b_q = self.b_r = (0, np.inf)
