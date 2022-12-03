# Initialize and set models

def init_model(self):
    self.model = {}
    self.init_model_bc()
    self.init_model_vg()
    self.init_model_ln()
    self.init_model_fx()
    self.init_model_bc2()
    self.init_model_vg2()
    self.init_model_ln2()
    self.init_model_vgbc()
    self.init_model_kobc()
    self.init_model_fs()
    self.init_model_pe()
    self.output_format = {
        'qs': '.3f', 'qr': '.3f', 'qa': '.3f', 'w1': '.3f', 'a': '.3', 'a1': '.3', 'a2': '.3',
        'm': '.3f', 'n': '.3f', 'm1': '.3f', 'm2': '.3f', 'hm': '.2f', 'hm1': '.2f', 'hm2': '.2f',
        'sigma': '.3f', 'sigma1': '.3f', 'sigma2': '.3f', 'hb': '.2f', 'hb1': '.2f', 'hb2': '.2f',
        'hc': '.2f', 'l': '.3', 'l1': '.3', 'l2': '.3', 'he': '.2f',
        'Ks': '.2e', 'p': '.3f', 'p1': '.3f', 'p2': '.3f', 'q': '.3f', 'q1': '.3f', 'q2': '.3f', 'r': '.3f', 'omega': '.3'
    }
    self.r2_format = '.3f'


def set_model(self, model, const=[]):
    """Set model

    Parameters:

        model: name of the model
        const: constant parameters of the model. For example
               [[1,0.5], [2,0], [3,0.2]] sets 1st parameter as 0.5, 2nd parameter as 0 and 3rd parameter as 0.2
               [[1,0.5], 'qr=0']] sets 1st parameter as 0.5 and qr as 0
               [wrf, 'r=1'] where wrf is a tuple of all WRF parameters, sets the WRF parameters and r as 1
    """
    self.model_name = model
    self.f_ht, self.f_hk = self.model[model]['function']
    self.b_func = self.model[model]['bound']
    self.param = self.model[model]['param']
    self.model_k_only = self.model[model]['k-only']
    # get_init and get_wrf functions
    if 'get_init' in self.model[model]:
        self.get_init = self.model[model]['get_init']
    else:
        self.get_init = self.get_init_not_defined
    if 'get_wrf' in self.model[model]:
        self.get_wrf = self.model[model]['get_wrf']
    else:
        self.get_wrf = self.get_wrf_not_defined
    # Recostruct const to allow alternative expressions
    reconst = []
    for i in const:
        if '=' in str(i):  # expression like 'q=1'
            p, value = i.split('=')
            if p not in self.param:
                print('Parameter {0} not in this model'.format(p))
                exit(1)
            reconst.append([self.param.index(p) + 1, float(value)])
        elif len(i) > 2:  # tuple or list of all water retention parameters
            p = list(range(len(self.param)))
            for j in self.model_k_only:
                p.remove(j)
            if len(p) == len(i):
                k = 0
                for j in p:
                    reconst.append([j + 1, i[k]])
                    k += 1
            else:
                print(
                    '{0} parameters required for water retention function, but {1} parameters {2} given.'.format(len(p), len(i), i))
                exit()
        else:  # expression like [2, 0]
            reconst.append(i)
    self.const = sorted(reconst)
    # print(self.model_description)
    # Calculate self.p_k_only from self.model_k_only by eliminating constant
    # Note: when it is (0,1,3) where 2 is constant, it should be arranged to
    # (0,1,2)
    k_only = set(self.model_k_only)
    for c in sorted(self.const, reverse=True):
        if c[0] - 1 in sorted(k_only):
            k_only.remove(c[0] - 1)
        else:
            for i in sorted(k_only):
                if i > c[0] - 1:
                    k_only.remove(i)
                    k_only.add(i - 1)
    self.p_k_only = sorted(list(k_only), reverse=True)
    # Calculate self.const_ht by eliminating K-only parameters
    self.const_ht = []
    for c in self.const:
        if c[0] - 1 not in self.model_k_only:
            self.const_ht.append(
                [c[0] - sum(1 for x in self.model_k_only if x < c[0] - 1), c[1]])
    # Calculate self.param and self.param_ht
    self.param_ht = self.param
    for i in sorted(self.model_k_only, reverse=True):
        self.param_ht = self.param_ht[:i] + self.param_ht[i + 1:]
    for c in sorted(self.const_ht, reverse=True):
        self.param_ht = self.param_ht[:c[0] - 1] + self.param_ht[c[0]:]
    for c in sorted(self.const, reverse=True):
        self.param = self.param[:c[0] - 1] + self.param[c[0]:]
    # Model description
    self.param_const = []
    self.value_const = []
    for i in self.const:
        self.param_const.append(self.model[model]['param'][i[0] - 1])
        self.value_const.append(float(i[1]))
    self.const_description = self.format(
        self.param_const, ShowR2=False).format(*self.value_const)
    self.model_description = self.model_name + \
        ' model with ' + self.const_description


def get_init_not_defined(self):
    print('get_init function not defined for {0} model'.format(
        self.model_name))
    exit(1)


def get_wrf_not_defined(self):
    print('get_wrf function not defined for {0} model'.format(
        self.model_name))
    exit(1)
