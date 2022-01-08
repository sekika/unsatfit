import numpy as np


class Fit:
    """Fit water retention and unsaturated hydraulic conductivity functions

    Sample usage:

        f = unsatfit.Fit() # Create instance for fitting
        f.set_model('vg', const=[[10, 1]]) # Set model and constant parameters
        f.swrc = (h, theta) # Data of soil water retention
        f.unsat = (h, K) # Data of unsaturated hydraulic conductivity
        a, m = f.get_init_vg() # Get initial paramter
        f.ini = (max(theta), 0, a, m, max(K), 0.5, 2) # Set initial paramter
        f.b_qr = (0, 0.05) # Set lower and upper bound
        f.optimize() # Optimize
        print(f.fitted) # Show result as an array
        print(f.message)  # Show result
        f.show_fig = True
        f.plot()  # Draw a graph
        f.contour('a', 'm')  # Draw contour of RMSE for a and m

        See also the code of test() function

    Models:

        bc    : Brooks and Corey (BC) with generalized Mualem model
        vg    : van Genuchten (VG) with generalized Mualem model
        ln    : Kosugi model (KO) with generalized Mualem model
        bc2   : dual-BC-CH (common H) with generalized Mualem model
        bc2f  : dual-BC with generalized Mualem model
        vg2   : dual-VG with generalized Mualem model
        vg2ch : dual-VG-CH with generalized Mualem model
        ln2   : dual-KO with generalized Mualem model
        vgbc  : VG1BC2 with generalized Mualem model
        vgbcp2: VG1BC2 with r=1 and independent p1, p2
        vgbcch: VG1BC2-CH with generalized Mualem model
        vgbcchp2: VG1BC2-CH with r=1 and independent p1, p2
        kobcch: KO1BC2-CH with generalized Mualem model
        kobcchp2: KO1BC2-CH with r=1 and independent p1, p2
        vgfs  : van Genuchten - Fayer and Simmons model with generalized Mualem model
        fx    : Fredlund und Xing model (SWRC only)

        See list of parameters in __init_model()

    Methods:

        optimize()     : optimize
        plot()         : plot
        add_curve()    : add a curve for plot
        clear_curves() : clear curves
        contour(x,y)   : Draw contour of RMSE for x and y in parameter name

        test()         : (for development) test integrity of the code

        Methods to get initial paramteres for SWRC

        get_init_bc()  : get (hb, lambda) for BC model
        get_init_vg()  : get (alpha, m) for VG model. m=1-q/n
        get_init_ln()  : get (hm, sigma) for Kosugi model.
        get_init_bc2() : get (hm, hc, l1, l2) for dual-BC model.
                         w1 = 1/(1+(hc/hb)^(l2-l1))

    Instance properties:

        See
        __init_bound() for boundary conditions
        __init_lsq()   for least square optimization
        __init_fig()   for figure options

    """

# Definition of hydraulic models

    def __init_model(self):
        self.model = {
            'bc': {
                # Water retention and hydraulic conductivity functions
                'function': (self.bc, self.bc_k),
                # Bound of paramters
                'bound': self.bound_bc,
                # Name of parameters
                'param': ['qs', 'qr', 'hb', 'l', 'Ks', 'p', 'q', 'r'],
                # Index of parameters (starting from 0) used only for K function
                'k-only': [4, 5, 6, 7]
            },
            'bc2': {
                'function': (self.bc2, self.bc2_k),
                'bound': self.bound_bc2,
                'param': ['qs', 'qr', 'hb', 'hc', 'l1', 'l2', 'Ks', 'p', 'q', 'r'],
                'k-only': [6, 7, 8, 9]
            },
            'bc2f': {
                'function': (self.bc2f, self.bc2f_k),
                'bound': self.bound_bc2f,
                'param': ['qs', 'qr', 'w1', 'hb1', 'l1', 'hb2', 'l2', 'Ks', 'p', 'q', 'r'],
                'k-only': [7, 8, 9, 10]
            },
            'vg': {
                'function': (self.vg, self.vg_k),
                'bound': self.bound_vg,
                'param': ['qs', 'qr', 'a', 'm', 'Ks', 'p', 'q', 'r'],
                'k-only': [4, 5, 7]
            },
            'vg2': {
                'function': (self.vg2, self.vg2_k),
                'bound': self.bound_vg2,
                'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'a2', 'm2', 'Ks', 'p', 'q', 'r'],
                'k-only': [7, 8, 10]
            },
            'vg2ch': {
                'function': (self.vg2ch, self.vg2ch_k),
                'bound': self.bound_vg2ch,
                'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'm2', 'Ks', 'p', 'q', 'r'],
                'k-only': [6, 7, 9]
            },
            'ln': {
                'function': (self.ln, self.ln_k),
                'bound': self.bound_ln,
                'param': ['qs', 'qr', 'hm', 'sigma', 'Ks', 'p', 'q', 'r'],
                'k-only': [4, 5, 6, 7],
            },
            'ln2': {
                'function': (self.ln2, self.ln2_k),
                'bound': self.bound_ln2,
                'param': ['qs', 'qr', 'w1', 'hm1', 'sigma1', 'hm2', 'sigma2', 'Ks', 'p', 'q', 'r'],
                'k-only': [7, 8, 9, 10]
            },
            'ln2ch': {
                'function': (self.ln2ch, self.ln2ch_k),
                'bound': self.bound_ln2ch,
                'param': ['qs', 'qr', 'w1', 'hm1', 'sigma1', 'sigma2', 'Ks', 'p', 'q', 'r'],
                'k-only': [6, 7, 8, 9]
            },
            'vgbc': {
                'function': (self.vgbc, self.vgbc_k),
                'bound': self.bound_vgbc,
                'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'hb2', 'l2', 'Ks', 'p', 'q', 'r'],
                'k-only': [7, 8, 10]
            },
            'vgbcp2': {
                'function': (self.vgbc, self.vgbcp2_k),
                'bound': self.bound_vgbcp2,
                'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'hb2', 'l2', 'Ks', 'p1', 'p2', 'q'],
                'k-only': [7, 8, 9]
            },
            'vgbcch': {
                'function': (self.vgbcch, self.vgbcch_k),
                'bound': self.bound_vgbcch,
                'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'l2', 'Ks', 'p', 'q', 'r'],
                'k-only': [6, 7, 9]
            },
            'vgbcchp2': {
                'function': (self.vgbcchp2, self.vgbcchp2_k),
                'bound': self.bound_vgbcchp2,
                'param': ['qs', 'qr', 'w1', 'a1', 'm1', 'l2', 'Ks', 'p1', 'p2', 'q'],
                'k-only': [6, 7, 8]
            },
            'kobcch': {
                'function': (self.kobcch, self.kobcch_k),
                'bound': self.bound_kobcch,
                'param': ['qs', 'qr', 'w1', 'hm', 'sigma1', 'l2', 'Ks', 'p', 'q', 'r'],
                'k-only': [6, 7, 8, 9]
            },
            'kobcchp2': {
                'function': (self.kobcch, self.kobcchp2_k),
                'bound': self.bound_kobcchp2,
                'param': ['qs', 'qr', 'w1', 'hm', 'sigma1', 'l2', 'Ks', 'p1', 'p2', 'q'],
                'k-only': [6, 7, 8, 9]
            },
            'vgfs': {
                'function': (self.vgfs, self.vgfs_k),
                'bound': self.bound_vgfs,
                'param': ['qs', 'qr', 'qa', 'a', 'm', 'he', 'Ks', 'p', 'q', 'r'],
                'k-only': [6, 7, 9]
            },
            'fx': {
                'function': (self.fx, False),
                'bound': self.bound_fx,
                'param': ['qs', 'qr', 'a', 'm', 'n'],
                'k-only': []
            }
        }
        self.output_format = {
            'qs': '.3f', 'qr': '.3f', 'qa': '.3f', 'w1': '.3f', 'a': '.5f', 'a1': '.3f', 'a2': '.5f',
            'm': '.3f', 'n': '.3f', 'm1': '.3f', 'm2': '.3f', 'hm': '.2f', 'hm1': '.2f', 'hm2': '.2f',
            'sigma': '.3f', 'sigma1': '.3f', 'sigma2': '.3f', 'hb': '.2f', 'hb1': '.2f', 'hb2': '.2f',
            'hc': '.2f', 'l': '.3f', 'l1': '.3f', 'l2': '.5f', 'he': '.2f',
            'Ks': '.2e', 'p': '.3f', 'p1': '.3f', 'p2': '.3f', 'q': '.3f', 'r': '.3f'
        }
        self.r2_format = '.3f'
        # Define alias for model name
        self.model['BC'] = self.model['bc']
        self.model['VG'] = self.model['vg']
        self.model['KO'] = self.model['ln']
        self.model['FX'] = self.model['fx']
        self.model['DB'] = self.model['dual-BC'] = self.model['bc2f']
        self.model['DBCH'] = self.model['dual-BC-CH'] = self.model['bc2']
        self.model['VGBC'] = self.model['VG1BC2'] = self.model['vgbc']
        self.model['VGBCP2'] = self.model['VG1BC2-p1p2'] = self.model['vgbcp2']
        self.model['VGBCCH'] = self.model['VG1BC2-CH'] = self.model['vgbcch']
        self.model['VGBCCHP2'] = self.model['VG1BC2-CH-p1p2'] = self.model['vgbcchp2']
        self.model['DV'] = self.model['dual-VG'] = self.model['vg2']
        self.model['DVCH'] = self.model['dual-VG-CH'] = self.model['vg2ch']
        self.model['DK'] = self.model['dual-KO'] = self.model['ln2']
        self.model['KOBCCH'] = self.model['KO1BC2-CH'] = self.model['kobcch']
        self.model['KOBCCHP2'] = self.model['KO1BC2-CH-p1p2'] = self.model['kobcchp2']
        self.model['VSFS'] = self.model['Fayer-VG'] = self.model['vgfs']


# Test

    def test(self):
        f = Fit()
        # Test data from UNSODA 3393
        f.swrc = (np.array([10, 28, 74, 160, 288, 640, 1250, 2950, 6300, 10600, 15800]), np.array(
            [0.36, 0.35, 0.34, 0.33, 0.32, 0.3, 0.28, 0.26, 0.24, 0.22, 0.2]))
        unsat = (np.array([10, 28, 74, 160, 288, 640, 1250, 2950, 6300, 10600]), np.array(
            [0.384, 0.0988, 0.0293, 0.0137, 0.00704, 0.00315, 0.00085, 0.000206, 0.000101, 0.00006])/60/60/24)
        qs = max(f.swrc[1])
        ks = max(unsat[1])
        a, m = f.get_init_vg()
        f.set_model('ln', const=[[1, qs], [2, 0]])
        hm, s = f.get_init_ln()
        f.ini = (hm, 3)
        f.b_sigma = (0, 3)
        f.optimize()
        hm, s = f.fitted
        hb, hc, l1, l2 = f.get_init_bc2()
        w1 = 1/(1+(hc/hb)**(l2-l1))
        f.set_model('bc2f', const=[[1, qs], [2, 0]])
        f.ini = (w1, hb, l1, hb*100, l2)
        f.optimize()
        wbc2, hb1, l1f, hb2, l2f = f.fitted
        f.set_model('vg2', const=[[1, qs], [2, 0], [10, 1]])
        f.ini = (0.5, 0.1, m, 0.0005, m)
        f.optimize()
        wvg2, a1, m1, a2, m2 = f.fitted
        f.set_model('vgfs', const=[[1, qs], [2, 0], [6, 10**7], [9, 1]])
        f.ini = ((1-wvg2)*qs, a1, m1)
        f.optimize()
        qa, fsa, fsm = f.fitted
        f.set_model('ln2', const=[[1, qs], [2, 0]])
        s1 = 2
        s2 = 1.2 * (1/(1-m2)-1)**(-0.8)
        f.ini = (wvg2, 1/a1, s1, 1/a2, s2)
        f.optimize()
        wln2, hm1, s1, hm2, s2 = f.fitted
        f.unsat = unsat
        f.set_model('vg', const=[[7, 1]])
        f.ini = (qs, 0, a, m, ks, 2, 1)
        f.optimize()
        f.test_confirm('VG', 965648)
        f.set_model('ln', const=[[1, qs], [2, 0], [8, 1]])
        f.ini = (hm, s, ks, 5, 1)
        f.optimize()
        f.test_confirm('LN', 945102)
        f.set_model('bc2', const=[[1, qs], [2, 0], [
            3, hb], [4, hc], [5, l1], [6, l2]])
        f.ini = (ks, 0.5, 1, 1)
        f.optimize()
        f.test_confirm('dual-BC-CH', 958167)
        f.set_model('bc2f', const=[[1, qs], [2, 0], [
            3, wbc2], [4, hb1], [5, l1f], [6, hb2], [7, l2f]])
        f.ini = (ks, 0.5, 1, 1)
        f.optimize()
        f.test_confirm('dual-BC', 930806)
        f.set_model('vg2', const=[[1, qs], [2, 0], [3, wvg2], [
            4, a1], [5, m1], [6, a2], [7, m2], [10, 1]])
        f.ini = (ks, 0.5, 2)
        f.optimize()
        f.test_confirm('dual-VG', 901827)
        f.set_model('vgfs', const=[[1, qs], [2, 0], [3, qa], [
            4, fsa], [5, fsm], [6, 10**7], [9, 1], [10, 2]])
        f.ini = (ks, 0.5)
        f.optimize()
        f.test_confirm('FS', 929316)
        f.set_model('ln2', const=[[1, qs], [2, 0], [3, wln2], [4, hm1], [
            5, s1], [6, hm2], [7, s2], [9, 2], [11, 1.5]])
        f.ini = (ks, 1)
        f.optimize()
        f.test_confirm('dual-LN', 995779)
        f.set_model('vgbc', const=[[1, qs], [2, 0], [3, wvg2], [
            4, a1], [5, m1], [6, hb2], [7, l2], [10, 1]])
        f.ini = (ks, 0.5, 1)
        f.optimize()
        f.test_confirm('VG-BC', 980322)

    def test_confirm(self, case, expect):
        result = int((self.r2_ht + self.r2_ln_hk) * 500000)
        assert expect == result, 'Test failed for {0}. Expected: {1} Actual: {2}\nResult: {3}'.format(
            case, expect, result, self.message)

# Initialization

    def __init__(self):
        self.debug = False
        self.swrc = self.unsat = []  # Set empty data
        self.__init_model()  # Define soil hydraulic models
        self.__init_bound()  # Boundary conditions
        self.__init_lsq()   # Parameters for least square optimization
        self.__init_fig()   # Parameters for figure

    def set_model(self, model, const=[]):
        self.model_name = model
        self.f_ht, self.f_hk = self.model[model]['function']
        self.b_func = self.model[model]['bound']
        self.param = self.model[model]['param']
        self.model_k_only = self.model[model]['k-only']
        self.const = sorted(const)
        # Calculate self.p_k_only from self.model_k_only by eliminating constant
        # Note: when it is (0,1,3) where 2 is constant, it should be arranged to (0,1,2)
        k_only = set(self.model_k_only)
        for c in sorted(self.const, reverse=True):
            if c[0]-1 in sorted(k_only):
                k_only.remove(c[0]-1)
            else:
                for i in sorted(k_only):
                    if i > c[0]-1:
                        k_only.remove(i)
                        k_only.add(i-1)
        self.p_k_only = sorted(list(k_only), reverse=True)
        # Calculate self.const_ht by eliminating K-only parameters
        self.const_ht = []
        for c in self.const:
            if c[0]-1 not in self.model_k_only:
                self.const_ht.append(
                    [c[0]-sum(1 for x in self.model_k_only if x < c[0]-1), c[1]])
        # Calculate self.param and self.param_ht
        self.param_ht = self.param
        for i in sorted(self.model_k_only, reverse=True):
            self.param_ht = self.param_ht[:i] + self.param_ht[i+1:]
        for c in sorted(self.const_ht, reverse=True):
            self.param_ht = self.param_ht[:c[0]-1] + self.param_ht[c[0]:]
        for c in sorted(self.const, reverse=True):
            self.param = self.param[:c[0]-1] + self.param[c[0]:]

    def __init_bound(self):
        self.b_qs = self.b_qr = (0, np.inf)
        self.b_qa = self.b_w1 = self.b_m = (0, 1)
        self.b_a = self.b_a1 = self.b_a2 = self.b_hm = self.b_hm1 = self.b_hm2 = self.b_sigma = self.b_he = (
            0, np.inf)
        self.b_hb = self.b_hb2 = self.b_hc = self.b_lambda = self.b_lambda1 = self.b_lambda2 = (
            0, np.inf)
        self.b_fxa = self.b_fxm = self.b_fxn = (0, np.inf)
        self.b_ks = self.b_p = self.b_q = self.b_r = (0, np.inf)

    def bound_bc(self):
        return [self.b_qs, self.b_qr, self.b_hb, self.b_lambda, self.b_ks, self.b_p, self.b_q, self.b_r]

    def bound_vg(self):
        return [self.b_qs, self.b_qr, self.b_a, self.b_m, self.b_ks, self.b_p, self.b_q, self.b_r]

    def bound_ln(self):
        return [self.b_qs, self.b_qr, self.b_hm, self.b_sigma, self.b_ks, self.b_p, self.b_q, self.b_r]

# Get initial estimate

    def get_init_bc(self):  # hb and lambda
        import math
        swrc = list(zip(*self.swrc))
        swrc_sort = sorted(swrc, key=lambda x: x[0])
        swrc = list(zip(*swrc_sort))
        x, t = swrc
        y = t / max(t)
        hbi = sum(y > 0.95 + min(y) * 0.05)
        hli = sum(y > 0.15 + min(y)*0.85)
        if hbi == hli:
            hli = hli + 1
        if hbi > hli:
            hbi = hbi - 1
            hli = hbi + 1
        hb = x[hbi]
        if hb == 0:
            hb = x[2] / 10
        l = -math.log(y[hli]/y[hbi]) / math.log(x[hli]/hb)
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

    def get_init_vg(self):  # alpha and m
        x, t = self.swrc
        y = t / max(t)
        f = Fit()
        f.set_model('vg', const=[[1, 1], [2, 0], [7, 1]])
        f.swrc = (x, y)
        hb, l = f.get_init_bc()
        n = l+1
        f.ini = (1/hb, 1-1/n)
        f.optimize()
        return f.fitted

    def get_init_ln(self):  # hm and sigma
        x, t = self.swrc
        y = t / max(t)
        f = Fit()
        f.set_model('ln', const=[[1, 1], [2, 0]])
        f.swrc = (x, y)
        a, m = f.get_init_vg()
        n = 1/(1-m)
        s = 1.2*(n-1)**(-0.8)
        if s < 0.15:
            s = 0.15
        if s > 3:
            s = 3
        f.ini = (1/a, s)
        f.optimize()
        return f.fitted

    def get_init_bc2(self):  # hb, hc, l1, l2
        x, t = self.swrc
        y = t / max(t)
        f = Fit()
        f.debug = self.debug
        f.swrc = (x, y)
        hb, l = f.get_init_bc()
        min_hb = min(min(x[np.nonzero(x)]) / 5, hb/2)
        max_hb, min_hc, hc, max_hc = hb * (0.8, 0.7, 0.3, 0.1) ** (-1/l)
        f.b_hb = (min_hb, max_hb)
        f.b_hc = (min_hc, max_hc)
        i = sum(x < max_hc)
        if len(x) - i > 1:
            w = 1/(1+(hc/hb)**(-l))
            x = np.log(x[i:] / hb)
            y = -np.log(y[i:] / (1-w))
            l2 = self.linear_regress(x, y)
            if l2 < 0.01:
                l2 = 0.01
        else:
            l2 = 0
        f.set_model('bc2', const=[[1, 1], [2, 0], [3, hb], [4, hc], [6, l2]])
        f.ini = (l)
        f.optimize()
        if f.success:
            l1, = f.fitted
        else:
            l1, = l,
        f.set_model('bc2', const=[[1, 1], [2, 0]])
        f.ini = (hb, hc, l1, l2)
        f.b_lambda1 = (min(l, l1), l1+2)
        f.b_lambda2 = (0, max(l, l2))
        f.optimize()
        if f.success:
            return f.fitted
        else:
            return f.ini

    def get_init_vg2ch(self):  # w, alpha, m1, m2
        x, t = self.swrc
        y = t / max(t)
        f = Fit()
        f.debug = self.debug
        f.swrc = (x, y)
        a, m1 = f.get_init_vg()
        hb, l = f.get_init_bc()
        hc, max_hc = hb * (0.3, 0.1) ** (-1/l)
        w = 1/(1+(hc/hb)**(-l))
        i = sum(x < max_hc)
        if len(x) - i > 1:
            x = np.log(x[i:] / hb)
            y = -np.log(y[i:] / (1-w))
            l2 = self.linear_regress(x, y)
            if l2 < 0.01:
                l2 = 0.01
        else:
            l2 = 0
        n2 = l2+1
        m2 = 1-1/n2
        f.set_model('vg2ch', const=[[1, 1], [2, 0], [
                    3, w], [4, a], [6, m2], [9, 1]])
        f.ini = (m1)
        f.optimize()
        m1, = f.fitted
        f.set_model('vg2ch', const=[[1, 1], [2, 0], [9, 1]])
        f.ini = (w, a, m1, m2)
        f.optimize()
        if f.success:
            return f.fitted
        else:
            return f.ini

    # Linear regression y = ax

    def linear_regress(self, x, y):
        return np.dot(x, y)/(x**2).sum()

# Definition of water retention and hydraulic conductivity functions

    # Brooks and Corey model

    def bc(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return self.bc_se(p, x) * (p[0]-p[1]) + p[1]

    def bc_se(self, p, x):
        return np.where(x < p[2], 1, (x/p[2]) ** (-p[3]))

    def bc_k(self, p, x):  # Not defined yet
        p = list(p)
        for c in self.const:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return

    # dual-BC model

    def bound_bc2(self):
        return [self.b_qs, self.b_qr, self.b_hb, self.b_hc, self.b_lambda1,
                self.b_lambda2, self.b_ks, self.b_p, self.b_q, self.b_r]

    def bound_bc2f(self):
        return [self.b_qs, self.b_qr, self.b_w1, self.b_hb, self.b_lambda1, self.b_hb2,
                self.b_lambda2, self.b_ks, self.b_p, self.b_q, self.b_r]

    def bc2(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return self.bc2_se(p, x) * (p[0]-p[1]) + p[1]

    def bc2f(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return self.bc2f_se(p, x) * (p[0]-p[1]) + p[1]

    def bc2_se(self, p, x):
        w = 1/(1+(p[3]/p[2])**(p[5]-p[4]))
        s1 = (x/p[2]) ** (-p[4])
        s2 = (x/p[2]) ** (-p[5])
        return np.where(x < p[2], 1, w * s1 + (1-w) * s2)

    def bc2f_se(self, p, x):
        qs, qr, w1, hb1, l1, hb2, l2 = p
        s1 = np.where(x < hb1, 1, (x/hb1) ** (-l1))
        s2 = np.where(x < hb2, 1, (x/hb2) ** (-l2))
        return w1 * s1 + (1-w1) * s2

    def bc2_k(self, p, x):
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, hb, hc, l1, l2, ks, p, q, r = par
        w1 = 1/(1+(hc/hb)**(l2-l1))
        w1b1 = w1 / (q / l1 + 1)
        w2b2 = (1 - w1) / (q / l2 + 1)
        s1 = np.where(x < hb, 1, (x/hb) ** (-l1-q))
        s2 = np.where(x < hb, 1, (x/hb) ** (-l2-q))
        bunshi = w1b1 * s1 + w2b2 * s2
        bunbo = w1b1 + w2b2
        return ks * self.bc2_se(par[:6], x)**p * (bunshi / bunbo)**r

    def bc2f_k(self, p, x):
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, w1, hb1, l1, hb2, l2, ks, p, q, r = par
        w1b1 = w1 / hb1 ** q / (q / l1 + 1)
        w2b2 = (1 - w1) / hb2 ** q / (q / l2 + 1)
        s1 = np.where(x < hb1, 1, (x/hb1) ** (-l1-q))
        s2 = np.where(x < hb2, 1, (x/hb2) ** (-l2-q))
        bunshi = w1b1 * s1 + w2b2 * s2
        bunbo = w1b1 + w2b2
        return ks * self.bc2f_se(par[:7], x)**p * (bunshi / bunbo)**r

    # van Genuchten model

    def vg(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return self.vg_se(p[2:5], x) * (p[0]-p[1]) + p[1]

    def vg_se(self, p, x):
        a, m, q = p
        n = q/(1-m)
        return (1 + (a * x)**n)**(-m)

    def vg_k(self, p, x):
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, a, m, ks, p, q, r = par
        s = self.vg_se([a, m, q], x)
        k = ks * s**p * (1-(1-s**(1/m))**m)**r
        return k

    # dual-VG model

    def bound_vg2(self):
        return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
                self.b_a2, self.b_m, self.b_ks, self.b_p, self.b_q, self.b_r]

    def vg2(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return self.vg2_se(p, x) * (p[0]-p[1]) + p[1]

    def vg2_se(self, p, x):
        s1 = self.vg_se([p[3], p[4], p[7]], x)
        s2 = self.vg_se([p[5], p[6], p[7]], x)
        return p[2] * s1 + (1-p[2]) * s2

    def vg2_k(self, p, x):
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, w, a1, m1, a2, m2, ks, p, q, r = par
        w1a1q = w * (a1 ** q)
        w2a2q = (1-w) * (a2 ** q)
        s1 = self.vg_se([a1, m1, q], x)
        s2 = self.vg_se([a2, m2, q], x)
        bunshi = w1a1q * (1-(1-s1**(1/m1))**m1) + \
            w2a2q * (1-(1-s2**(1/m2))**m2)
        bunbo = w1a1q + w2a2q
        return ks * self.vg2_se(par[:7]+[q], x)**p * (bunshi / bunbo)**r

    # dual-VG-CH model

    def bound_vg2ch(self):
        return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
                self.b_m, self.b_ks, self.b_p, self.b_q, self.b_r]

    def vg2ch(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return self.vg2ch_se(p, x) * (p[0]-p[1]) + p[1]

    def vg2ch_se(self, p, x):
        s1 = self.vg_se([p[3], p[4], p[6]], x)
        # s2 = self.vg_se([p[4], p[5], p[6]], x)
        s2 = self.vg_se([p[3], p[5], p[6]], x)  # Fixed
        return p[2] * s1 + (1-p[2]) * s2

    def vg2ch_k(self, p, x):
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, w, a1, m1, m2, ks, p, q, r = par
        s1 = self.vg_se([a1, m1, q], x)
        s2 = self.vg_se([a1, m2, q], x)
        bunshi = w * (1-(1-s1**(1/m1))**m1) + (1-w) * (1-(1-s2**(1/m2))**m2)
        return ks * self.vg2ch_se(par[:6]+[q], x)**p * bunshi**r

    # Kosugi model

    def ln(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        qs, qr, hm, s = p
        return self.ln_se([hm, s], x) * (qs-qr) + qr

    def ln_se(self, p, x):
        from scipy.stats import norm
        # Ignore runtime warning, because divide by zero is warned when x=0
        import warnings
        warnings.simplefilter('ignore', category=RuntimeWarning)
        return 1 - norm.cdf(np.log(x / p[0])/p[1])

    def ln_k(self, p, x):
        from scipy.stats import norm
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, hm, s, ks, p, q, r = par
        qq = 1 - norm.cdf(np.log(x / hm)/s + q*s)
        return ks * self.ln_se([hm, s], x)**p * qq**r

    # dual-LN model

    def bound_ln2(self):
        return [self.b_qs, self.b_qr, self.b_w1, self.b_hm1, self.b_sigma,
                self.b_hm2, self.b_sigma, self.b_ks, self.b_p, self.b_q, self.b_r]

    def ln2(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return self.ln2_se(p, x) * (p[0]-p[1]) + p[1]

    def ln2_se(self, p, x):
        s1 = self.ln_se([p[3], p[4]], x)
        s2 = self.ln_se([p[5], p[6]], x)
        return p[2] * s1 + (1-p[2]) * s2

    def ln2_k(self, p, x):
        from scipy.stats import norm
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, w, hm1, s1, hm2, s2, ks, p, q, r = par
        w1b1 = w * np.exp((q * s1)**2 / 2) / (hm1 ** q)
        w2b2 = (1 - w) * np.exp((q * s2)**2 / 2) / (hm2 ** q)
        q1 = 1 - norm.cdf(np.log(x / hm1)/s1 + q * s1)
        q2 = 1 - norm.cdf(np.log(x / hm2)/s2 + q * s2)
        bunshi = w1b1 * q1 + w2b2 * q2
        bunbo = w1b1 + w2b2
        return ks * self.ln2_se(par[:7], x)**p * (bunshi / bunbo)**r

    # dual-LN-CH model

    def bound_ln2ch(self):
        return [self.b_qs, self.b_qr, self.b_w1, self.b_hm1, self.b_sigma,
                self.b_sigma, self.b_ks, self.b_p, self.b_q, self.b_r]

    def ln2ch(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return self.ln2ch_se(p, x) * (p[0]-p[1]) + p[1]

    def ln2ch_se(self, p, x):
        s1 = self.ln_se([p[3], p[4]], x)
        s2 = self.ln_se([p[3], p[5]], x)
        return p[2] * s1 + (1-p[2]) * s2

    def ln2ch_k(self, p, x):
        from scipy.stats import norm
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, w, hm1, s1, s2, ks, p, q, r = par
        w1b1 = w * np.exp((q * s1)**2 / 2) / (hm1 ** q)
        w2b2 = (1 - w) * np.exp((q * s2)**2 / 2) / (hm1 ** q)
        q1 = 1 - norm.cdf(np.log(x / hm1)/s1 + q * s1)
        q2 = 1 - norm.cdf(np.log(x / hm1)/s2 + q * s2)
        bunshi = w1b1 * q1 + w2b2 * q2
        bunbo = w1b1 + w2b2
        return ks * self.ln2ch_se(par[:6], x)**p * (bunshi / bunbo)**r

    # VG1BC2 model

    def bound_vgbc(self):
        return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
                self.b_hb2, self.b_lambda2, self.b_ks, self.b_p, self.b_q, self.b_r]

    def vgbc(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return self.vgbc_se(p, x) * (p[0]-p[1]) + p[1]

    def vgbc_se(self, p, x):
        qs, qr, w, a1, m1, hb2, l2, q = p
        s1 = self.vg_se([a1, m1, q], x)
        s2 = np.where(x < hb2, 1, (x/hb2) ** (-l2))
        return w * s1 + (1-w) * s2

    def vgbc_k(self, p, x):
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, w, a1, m1, hb2, l2, ks, p, q, r = par
        w1b1 = w * (a1 ** q)
        w2b2 = (1 - w) / hb2 ** q / (q / l2 + 1)
        s1 = self.vg_se([a1, m1, q], x)
        s1 = 1-(1-s1**(1/m1))**m1
        s2 = np.where(x < hb2, 1, (x/hb2) ** (-l2-q))
        bunshi = w1b1 * s1 + w2b2 * s2
        bunbo = w1b1 + w2b2
        return ks * self.vgbc_se(par[:7]+[q], x)**p * (bunshi / bunbo)**r

    # VG1BC2 model with r=1 and independent p1, p2

    def bound_vgbcp2(self):
        return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
                self.b_hb2, self.b_lambda2, self.b_ks, self.b_p, self.b_p, self.b_q]

    def vgbcp2_k(self, p, x):
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, w, a1, m1, hb2, l2, ks, p1, p2, q = par
        w1b1 = w * (a1 ** q)
        w2b2 = (1 - w) / hb2 ** q / (q / l2 + 1)
        s1 = self.vg_se([a1, m1, q], x)
        s1 = 1-(1-s1**(1/m1))**m1
        s2 = np.where(x < hb2, 1, (x/hb2) ** (-l2-q))
        se = self.vgbc_se(par[:7]+[q], x)
        bunshi = se**p1 * w1b1 * s1 + se**p2 * w2b2 * s2
        bunbo = w1b1 + w2b2
        return ks * bunshi / bunbo

    # VG1BC2-CH model

    def bound_vgbcch(self):
        return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
                self.b_lambda2, self.b_ks, self.b_p, self.b_q, self.b_r]

    def vgbcch(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return self.vgbcch_se(p, x) * (p[0]-p[1]) + p[1]

    def vgbcch_se(self, p, x):
        qs, qr, w, a1, m1, l2, q = p
        hb2 = 1/a1
        s1 = self.vg_se([a1, m1, q], x)
        s2 = np.where(x < hb2, 1, (x/hb2) ** (-l2))
        return w * s1 + (1-w) * s2

    def vgbcch_k(self, p, x):
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, w, a1, m1, l2, ks, p, q, r = par
        hb2 = 1/a1
        w1b1 = w * (a1 ** q)
        w2b2 = (1 - w) / hb2 ** q / (q / l2 + 1)
        s1 = self.vg_se([a1, m1, q], x)
        s1 = 1-(1-s1**(1/m1))**m1
        s2 = np.where(x < hb2, 1, (x/hb2) ** (-l2-q))
        bunshi = w1b1 * s1 + w2b2 * s2
        bunbo = w1b1 + w2b2
        return ks * self.vgbcch_se(par[:6]+[q], x)**p * (bunshi / bunbo)**r

    # VG1BC2-CH model with r=1 and independent p1, p2

    def bound_vgbcchp2(self):
        return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
                self.b_lambda2, self.b_ks, self.b_p, self.b_p, self.b_q]

    def vgbcchp2(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return self.vgbcch_se(p, x) * (p[0]-p[1]) + p[1]

    def vgbcchp2_k(self, p, x):
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, w, a1, m1, l2, ks, p1, p2, q = par
        hb2 = 1/a1
        w1b1 = w * (a1 ** q)
        w2b2 = (1 - w) / hb2 ** q / (q / l2 + 1)
        s1 = self.vg_se([a1, m1, q], x)
        s1 = 1-(1-s1**(1/m1))**m1
        s2 = np.where(x < hb2, 1, (x/hb2) ** (-l2-q))
        se = self.vgbcch_se(par[:6]+[q], x)
        bunshi = se**p1 * w1b1 * s1 + se**p2 * w2b2 * s2
        bunbo = w1b1 + w2b2
        return ks * bunshi / bunbo

    # KO1BC2-CH model

    def bound_kobcch(self):
        return [self.b_qs, self.b_qr, self.b_w1, self.b_hm1, self.b_sigma,
                self.b_lambda2, self.b_ks, self.b_p, self.b_q, self.b_r]

    def kobcch(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return self.kobcch_se(p, x) * (p[0]-p[1]) + p[1]

    def kobcch_se(self, p, x):
        qs, qr, w, h, sigma, l2 = p
        s1 = self.ln_se([h, sigma], x)
        s2 = np.where(x < h, 1, (x/h) ** (-l2))
        return w * s1 + (1-w) * s2

    def kobcch_k(self, p, x):
        from scipy.stats import norm
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, w, h, sigma, l2, ks, p, q, r = par
        w1b1 = w * (h ** (-q)) * np.exp((q*sigma)**2 / 2)
        w2b2 = (1 - w) / h ** q / (q / l2 + 1)
        s1 = 1 - norm.cdf(np.log(x / h)/sigma + q * sigma)
        s2 = np.where(x < h, 1, (x/h) ** (-l2-q))
        bunshi = w1b1 * s1 + w2b2 * s2
        bunbo = w1b1 + w2b2
        return ks * self.kobcch_se(par[:6], x)**p * (bunshi / bunbo)**r

    # KO1BC2-CH model with r=1 and independent p1, p2

    def bound_kobcchp2(self):
        return [self.b_qs, self.b_qr, self.b_w1, self.b_hm1, self.b_sigma,
                self.b_lambda2, self.b_ks, self.b_p, self.b_p, self.b_q]

    def kobcchp2_k(self, p, x):
        from scipy.stats import norm
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, w, h, sigma, l2, ks, p1, p2, q = par
        w1b1 = w * (h ** (-q)) * np.exp((q*sigma)**2 / 2)
        w2b2 = (1 - w) / h ** q / (q / l2 + 1)
        s1 = 1 - norm.cdf(np.log(x / h)/sigma + q * sigma)
        s2 = np.where(x < h, 1, (x/h) ** (-l2-q))
        se = self.kobcch_se(par[:6], x)
        bunshi = se**p1 * w1b1 * s1 + se**p2 * w2b2 * s2
        bunbo = w1b1 + w2b2
        return ks * bunshi / bunbo

    # van Genuchten - Fayer Simmons model

    def bound_vgfs(self):
        return [self.b_qs, self.b_qr, self.b_w1, self.b_a1, self.b_m,
                self.b_he, self.b_ks, self.b_p, self.b_q, self.b_r]

    def vgfs(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return self.vgfs_se(p, x) * (p[0]-p[1]) + p[1]

    def vgfs_se(self, p, x):
        qs, qr, qa, a, m, he, q = p
        vg = self.vg_se([a, m, q], x)
        xi = 1 - np.log(x)/np.log(he)
        xisa = xi * qa / qs
        return xisa + (1 - xisa) * vg

    def vgfs_k(self, p, x):
        par = list(p)
        for c in self.const:
            par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        qs, qr, qa, a, m, hm, ks, p, q, r = par
        if q != 1:  # Note that q should be 1
            return 1
        sa = qa/qs
        n = q/(1-m)
        beta = 1
        gse = 1-np.log(a/beta)/np.log(beta*hm)*sa - sa  # 1 - gamma Se - Se

        def gamma(x, a, m, n, hm, sa, gse):
            w = 1/(1+(a*x)**n)
            wm = 1/(1+(a*hm)**n)

            def gs(w, m):
                s = 0
                for k in range(101):
                    s += w**k / (m + 1 + k)
                return w**(m+1) * s

            def h(w, m):
                return np.log(w) - m*w + m*(m-1)*w*w/4 - m*(m-1)*(m-2)*w**3/18

            def g(w, m):
                return np.where(w > 0.9, gs(0.9, m) + h(0.1, m) - h(1-w, m), gs(w, m))

            def f(w, m):
                return (1-w)**m*(np.log((1-w)/w)-1/m)

            def i3b(w, wm, m):
                return m*((w-wm) + wm*(np.log(wm)) - w*np.log(w))

            w0 = max(10**(-10), wm)
            i1 = (1-wm)**m - (1-w)**m
            i2 = (1/x - 1/hm)/a + (1-wm)**(m-1) - (1-w)**(m-1)
            i3a = f(w0, m) - f(w, m) + g(1-w, m) - g(1-w0, m)
            i3 = np.where(w > w0, i3a + i3b(w0, wm, m), i3b(w, wm, m))
            result = i1 * a * gse + a*sa / np.log(hm) * (i2 + i3/n)
            return result
        h0 = 0.025 / a
        hc = 10**(-7)  # Typical values for h_c range from 10^-7 to 10^-20

        def f(ah, n):
            return ah**(n-1) * (np.log(ah) - 1/(n-1))

        gamma_0c = a * (gse + sa / n / np.log(hm)) * \
            ((a * h0)**(n-1) - (a * hc)**(n-1))
        gamma_0c += a * sa / np.log(hm) * (f(a*h0, n) - f(a*hc, n))
        gamma_max = gamma(h0, a, m, n, hm, sa, gse) + gamma_0c
        integral = gamma(x, a, m, n, hm, sa, gse) / gamma_max
        return ks * self.vgfs_se(par[:6]+[q], x)**p * integral**r

    # Fredlund and Xing model

    def bound_fx(self):
        return [self.b_qs, self.b_qr, self.b_fxa, self.b_fxm, self.b_fxn]

    def fx(self, p, x):
        p = list(p)
        for c in self.const_ht:
            p = p[:c[0]-1] + [c[1]] + p[c[0]-1:]
        return self.fx_se(p[2:], x) * (p[0]-p[1]) + p[1]

    def fx_se(self, p, x):
        a, m, n = p
        return (np.log(np.e + (x/a)**n))**(-m)

# Cost function

    def residual_ht(self, p, x, y):
        return self.f_ht(p, x) - y

    def residual_ln_hk(self, p, x, y):
        return np.log(self.f_hk(p, x) / y)

    def f_r2_ht(self, p, x, y):
        mse_ht = np.average(self.residual_ht(p, x, y)**2)
        return 1 - mse_ht/self.var_theta

    def f_r2_ln_hk(self, p, x, y):
        mse_ln_hk = np.average(self.residual_ln_hk(p, x, y)**2)
        return 1 - mse_ln_hk/self.var_ln_k

    def p_ht(self, p):
        p = list(p)
        for c in self.p_k_only:
            if c+2 > len(p):
                p = p[:c]
            else:
                p = p[:c] + p[c+1:]
        return p

    def total_cost(self, p, x1, y1, x2, y2):
        r2 = self.f_r2_ht(self.p_ht(p), x1, y1) + self.f_r2_ln_hk(p, x2, y2)
        return 2-r2

# Optimization

    def __init_lsq(self):
        self.lsq_method = 'trf'
        self.lsq_jac = '2-point'
        self.lsq_loss = 'linear'
        self.lsq_verbose = 0
        self.lsq_nfev_swrc = 500  # Number of evaluation for fitting SWRC only
        self.lsq_nfev_dual = 3000  # Number of evaluation for dual fitting of SWRC and K
        self.lsq_ftol_swrc = 1e-8
        self.lsq_ftol_dual = 0.001

    def format(self, param, DualFitting):
        format = ''
        count = 0
        for i in param:
            format += i + ' = {' + str(count) + ':' + \
                self.output_format[i] + '} '
            count += 1
        if DualFitting:
            format += 'R2 q = {' + str(count) + \
                ':' + self.r2_format + \
                '} R2 logK = {' + str(count+1) + ':' + self.r2_format + '}'
        else:
            format += 'R2 = {' + str(count) + ':' + self.r2_format + '}'
        return format

    def optimize(self):
        import math
        from scipy import optimize

        self.success = False

        if len(self.swrc) != 2:
            self.message = 'Error: No data of soil water retention curve.'
            return

        self.mean_theta = np.average(self.swrc[1])
        self.var_theta = np.average((self.swrc[1] - self.mean_theta)**2)
        b = self.b_func()

        for c in sorted(self.const, reverse=True):
            b = b[:c[0]-1] + b[c[0]:]

        if len(self.unsat) == 2:
            self.ht_only = False
            if min(self.unsat[1]) <= 0:
                self.message = 'Error: K should be positive.'
                return
            a = (self.swrc[0], self.swrc[1], self.unsat[0], self.unsat[1])
            cost = self.total_cost
            self.max_nfev = self.lsq_nfev_dual
            self.ftol = self.lsq_ftol_dual
            self.mean_k = np.average(self.unsat[1])
            self.var_k = np.average((self.unsat[1] - self.mean_k)**2)
            self.mean_ln_k = np.average(np.log(self.unsat[1]))
            self.var_ln_k = np.average(
                (np.log(self.unsat[1]) - self.mean_ln_k)**2)
        else:
            self.ht_only = True
            a = self.swrc
            cost = self.residual_ht
            self.max_nfev = self.lsq_nfev_swrc
            self.ftol = self.lsq_ftol_swrc
            for c in sorted(self.p_k_only, reverse=True):
                b = b[:c] + b[c+1:]

        b = tuple(zip(*b))

        if self.debug:
            print('ini = {0}\nbounds = {1}'.format(
                self.ini, b))  # for debugging

        result = optimize.least_squares(
            cost, self.ini, jac=self.lsq_jac, method=self.lsq_method, loss=self.lsq_loss,
            ftol=self.ftol, max_nfev=self.max_nfev, bounds=b, verbose=self.lsq_verbose, args=a)

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
            self.se_ht = math.sqrt(self.mse_ht)  # Standard error
            self.r2_ht = 1-self.mse_ht/self.var_theta  # Coefficient of determination
            self.aic_ht = n * np.log(self.mse_ht) + 2 * k  # AIC
            self.message = self.format(
                self.param_ht, False).format(*self.fitted, self.r2_ht)
        else:
            p = list(self.fitted)
            for c in sorted(self.p_k_only, reverse=True):
                p = p[:c] + p[c+1:]
            self.mse_ht = np.average(
                self.residual_ht(p, *self.swrc)**2)
            self.se_ht = math.sqrt(self.mse_ht)  # Standard error
            self.r2_ht = 1-self.mse_ht/self.var_theta  # Coefficient of determination
            self.aic_ht = n * np.log(self.mse_ht) + 2 * k  # AIC
            self.mse_ln_hk = np.average(
                self.residual_ln_hk(self.fitted, *self.unsat)**2)
            self.se_ln_hk = math.sqrt(self.mse_ln_hk)  # Standard error
            self.r2_ln_hk = 1-self.mse_ln_hk/self.var_ln_k  # Coefficient of determination
            self.aic_ln_hk = n * np.log(self.mse_ln_hk) + 2 * k  # AIC
            self.message = self.format(
                self.param, True).format(*self.fitted, self.r2_ht, self.r2_ln_hk)


# Figure

    def __init_fig(self):
        self.show_fig = False
        self.save_fig = False
        self.data_only = False
        self.fig_h_0to1 = False
        self.curves_ht = []
        self.curves_hk = []
        self.fig_width = 4.3  # inch
        self.fig_height = 3.2
        self.fig_height_double = 4.7
        self.top_margin = 0.05
        self.bottom_margin = 0.12
        self.left_margin = 0.17  # Space for label is needed
        self.right_margin = 0.05
        self.show_r2 = True
        self.log_x = True
        self.min_x_log = 1
        self.max_y2_log = 5
        self.curve_smooth = 200
        self.contour_smooth = 50
        self.contour_range_x = 0.3, 1.5
        self.contour_range_y = 0.5, 1.5
        self.label_head = 'Matric head'
        self.label_theta = 'Volumetric water content'
        self.label_k = 'Hydraulic conductivity'
        self.color_marker = 'black'
        self.color_line = 'black'
        self.line_style = 'dashed'
        self.legend = True
        self.legend_loc = 'center right'
        self.data_legend = 'Measured'
        self.line_legend = 'Fitted'

    def set_scale(self):
        x1, y1 = self.swrc
        if self.log_x:
            self.min_x = self.min_x_log
            try:
                self.max_x
            except AttributeError:
                self.max_x = max(x1) * 1.5
        else:
            self.min_x = min(0, min(x1) * 0.85)
            try:
                self.max_x
            except AttributeError:
                self.max_x = max(x1) * 1.05
        self.min_y1 = 0
        self.max_y1 = max(y1) * 1.15
        if not self.ht_only:
            x2, y2 = self.unsat
            self.min_y2 = min(y2) * 0.2
            self.max_y2 = max(y2) * self.max_y2_log

    def add_curve(self):
        import math
        self.set_scale()
        if self.log_x:
            x = 2**np.linspace(math.log2(self.min_x),
                               math.log2(self.max_x), num=self.curve_smooth)
        else:
            x = np.linspace(self.min_x, self.max_x, num=self.curve_smooth)
        if self.ht_only:
            self.curves_ht.append({'data': (x, self.f_ht(
                self.fitted, x)), 'color': self.color_line, 'style': self.line_style, 'legend': self.line_legend})
        else:
            self.curves_ht.append({'data': (x, self.f_ht(self.p_ht(
                self.fitted), x)), 'color': self.color_line, 'style': self.line_style, 'legend': self.line_legend})
            self.curves_hk.append({'data': (x, self.f_hk(
                self.fitted, x)), 'color': self.color_line, 'style': self.line_style, 'legend': self.line_legend})

    def clear_curves(self):
        self.curves_ht = []
        self.curves_hk = []

    def h_0to1(self, data):
        if not self.fig_h_0to1:
            return data
        x, y = data
        x = np.where(x == 0, 1, x)
        return (x, y)

    def plot(self):
        import matplotlib.pyplot as plt
        import matplotlib.ticker as ticker

        # Set subplots
        if self.ht_only:
            fig, ax1 = plt.subplots(figsize=[self.fig_width, self.fig_height])
        else:
            fig, (ax1, ax2) = plt.subplots(2, figsize=[
                self.fig_width, self.fig_height_double])
        fig.subplots_adjust(top=1-self.top_margin, bottom=self.bottom_margin, right=1 -
                            self.right_margin, left=self.left_margin, hspace=0)

        # Draw plots, curves and legends
        self.add_curve()
        ax1.plot(*self.h_0to1(self.swrc), color=self.color_marker, marker='o',
                 linestyle='', label=self.data_legend)
        if not self.data_only:
            for curve in self.curves_ht:
                ax1.plot(*curve['data'], color=curve['color'],
                         linestyle=curve['style'], label=curve['legend'])
            if not self.ht_only:
                ax2.plot(*self.h_0to1(self.unsat), color=self.color_marker,
                         marker='o', linestyle='', label='_nolegend_')
                for curve in self.curves_hk:
                    ax2.plot(*curve['data'], color=curve['color'],
                             linestyle=curve['style'], label='_nolegend_')
            fig.legend(loc=self.legend_loc)
            # plt.legend()

        # Draw scale
        if self.log_x:
            ax1.set_xscale("log")
        ax1.axis([self.min_x, self.max_x, self.min_y1, self.max_y1])
        if not self.ht_only:
            ax1.xaxis.set_major_formatter(ticker.NullFormatter())
            if self.log_x:
                ax2.loglog(base=10)
            else:
                ax2.set_yscale = ("log")
            ax2.xaxis.set_major_formatter(ticker.ScalarFormatter())
            ax2.axis([self.min_x, self.max_x, self.min_y2, self.max_y2])

        # Draw labels
        if self.ht_only:
            ax1.set_xlabel(self.label_head)
        else:
            ax2.set_xlabel(self.label_head)
        ax1.set_ylabel(self.label_theta)
        if not self.ht_only:
            ax2.set_ylabel(self.label_k)

        # Show and/or save figure
        if self.save_fig:
            plt.savefig(self.filename)
        if self.show_fig:
            plt.show()

# Contour of RMSE

    def contour(self, x_name, y_name):
        import matplotlib.pyplot as plt

        # Set data and residual function
        param = self.model[self.model_name]['param']
        if self.ht_only:
            data = self.swrc
            par = list(self.fitted)
            for c in self.const_ht:
                par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
            for i in sorted(self.model_k_only, reverse=True):
                param = param[:i] + param[i+1:]
        else:
            data = self.unsat
            par = list(self.fitted)
            for c in self.const:
                par = par[:c[0]-1] + [c[1]] + par[c[0]-1:]
        const = []
        for i in range(len(par)):
            const.append([i+1, par[i]])
        xi = param.index(x_name)
        yi = param.index(y_name)
        x = par[xi]
        y = par[yi]
        for i in sorted((xi, yi), reverse=True):
            const = const[:i] + const[i+1:]

        f = Fit()
        f.set_model(self.model_name, const=const)
        if self.ht_only:
            residual = f.residual_ht
        else:
            residual = f.residual_ln_hk

        # Make grid of (X,Y)
        x_min, x_max = self.contour_range_x
        y_min, y_max = self.contour_range_y
        x_delta = (x_max - x_min) / self.contour_smooth
        y_delta = (y_max - y_min) / self.contour_smooth
        x_grid = np.arange(x * x_min, x * x_max, x * x_delta)
        y_grid = np.arange(y * y_min, y * y_max, y * y_delta)
        X, Y = np.meshgrid(x_grid, y_grid)

        # Calculate RMSE for (X,Y) as Z
        z = []
        for yi in y_grid:
            row = []
            for xi in x_grid:
                mse = np.average(residual((xi, yi), *data)**2)
                row.append(mse ** 0.5)
            z.append(row)
        Z = np.array(z)

        # Draw contour of (X,Y,Z)
        fig, ax = plt.subplots(figsize=[self.fig_width, self.fig_height])
        fig.subplots_adjust(top=1-self.top_margin, bottom=self.bottom_margin,
                            right=1 - self.right_margin, left=self.left_margin)
        CS = ax.contour(X, Y, Z)
        ax.set_xlabel(self.label(x_name))
        ax.set_ylabel(self.label(y_name))
        ax.clabel(CS, inline=True, fontsize=10)

        if self.save_fig:
            plt.savefig(self.filename)
        if self.show_fig:
            plt.show()

    def label(self, name):
        label = '$' + name + '$'
        for i in [['q', '\\theta_'], ['hb', 'h_b'], ['hm2', 'h_{m2}'], ['hm', 'h_m'], ['Ks', 'K_s'], ['sigma', '\\sigma'], ['1', '_1'], ['2', '_2']]:
            label = label.replace(i[0], i[1])
        return label

    def version(self):
        """get version"""
        import configparser
        import os
        inifile = configparser.ConfigParser()
        here = os.path.abspath(os.path.dirname(__file__))
        inifile.read(os.path.join(here, 'data/system.ini'))
        return inifile.get('system', 'version')
