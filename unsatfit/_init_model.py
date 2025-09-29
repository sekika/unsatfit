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
    self.init_model_tri_vg()
    self.init_model_bvv()
    self.init_model_vvp()
    self.init_model_k_vapor()
    self.output_format = {
        'qs': '.3f', 'qr': '.3f', 'qa': '.3f', 'w1': '.3f', 'ww2': '.3f', 'a': '.3', 'a1': '.3', 'a2': '.3', 'a3': '.3',
        'm': '.3f', 'n': '.3f', 'm1': '.3f', 'm2': '.3f', 'm3': '.3f', 'hm': '.2f', 'hm1': '.2f', 'hm2': '.2f',
        'sigma': '.3f', 'sigma1': '.3f', 'sigma2': '.3f', 'hb': '.2f', 'hb1': '.2f', 'hb2': '.2f', 'hf': '.3f',
        'hc': '.2f', 'l': '.3', 'l1': '.3', 'l2': '.3', 'he': '.2f',
        'Ks': '.2e', 'p': '.3f', 'p1': '.3f', 'p2': '.3f', 'q': '.3f', 'q1': '.3f', 'q2': '.3f', 'r': '.3f', 'omega': '.3'
    }
    self.r2_format = '.3f'


def set_model(self, model, const=[], k_vapor=False):
    """Set model

    Parameters:

        model: name of the model
        const: constant parameters of the model. For example
            [[1,0.5], [2,0], [3,0.2]] sets 1st parameter as 0.5, 2nd parameter as 0 and 3rd parameter as 0.2
            [[1,0.5], 'qr=0']] sets 1st parameter as 0.5 and qr as 0
            [wrf, 'r=1'] where wrf is a tuple of all WRF parameters, sets the WRF parameters and r as 1
        k_vapor: if using isothermal vapor hydraulic conductivity
            When True, self.k_vapor() is added to hydraulic conductivity.
            Several parameters need to be set when using this feature.
            See comment in k_vapor() function.
    """
    self.model_name = model
    model = self.model[model]
    self.f_ht, self.f_hk = model['function']
    if k_vapor:
        def k_vapor(p, h):
            theta = self.f_ht(p, h)
            theta_s = self.f_ht(p, 0)
            k = model['function'][1](p, h)
            return k + self.model_k_vapor(h, theta, theta_s)
        self.f_hk = k_vapor
    self.b_func = model['bound']
    self.param = model['param']
    self.model_k_only = model['k-only']
    if 'sort_param' in model:
        self.sort_param = model['sort_param']
    else:
        self.sort_param = None
    # Set get_init() and get_wrf() functions
    self.set_get_init_wrf()
    # Organize parameters
    self.organize_parameters(const)


def set_get_init_wrf(self):
    """Set get_init() and get_wrf() functions"""
    model = self.model[self.model_name]

    def get_init_not_defined():
        print('get_init function not defined for {0} model'.format(
            self.model_name))
        exit(1)
    if 'get_init' in model:
        self.get_init = model['get_init']
    else:
        self.get_init = get_init_not_defined

    def get_wrf_not_defined():
        print('get_wrf function not defined for {0} model'.format(
            self.model_name))
        exit(1)
    if 'get_wrf' in model:
        self.get_wrf = model['get_wrf']
    else:
        self.get_wrf = get_wrf_not_defined


def organize_parameters(self, const):
    """Organize parameters"""
    # Recostruct const to allow alternative expressions
    model = self.model[self.model_name]
    self.reconstruct_const(const)
    # Calculate self.p_k_only
    self.k_only()
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
        self.param_const.append(model['param'][i[0] - 1])
        self.value_const.append(float(i[1]))
    self.const_description = self.format(
        self.param_const, ShowR2=False).format(*self.value_const)
    self.model_description = self.model_name + \
        ' model with ' + self.const_description


def reconstruct_const(self, const):
    """Reconstruct the list of parameter constraints for the model.

    The method interprets the input `const` (a list of constraints) in
    three possible formats and converts them into a standardized list
    of `[parameter_index, value]` pairs:

    1. String assignments (e.g., "q=1"):
       - Splits into parameter name and value.
       - Checks that the parameter exists in `self.param`.
       - Converts to `[index, float(value)]`.

    2. Full parameter list/tuple (longer than 2 elements):
       - Assumes the list provides values for all water retention
         parameters except those in `self.model_k_only`.
       - Matches given values to the correct parameter indices.
       - Errors out if the number of values does not match expectations.

    3. Explicit index/value pairs (e.g., `[2, 0]`):
       - Directly added to the reconstructed constraints.

    Finally, the reconstructed constraints are sorted and stored in
    `self.const`.

    Parameters
    ----------
    const : list
        A list of constraints expressed either as strings, full parameter
        lists, or explicit index/value pairs.

    Raises
    ------
    SystemExit
        If a parameter is not found in `self.param` or the number of
        provided values does not match the required number of parameters.
    """
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


def k_only(self):
    """Compute the reindexed positions of k-only parameters after removing constants.

    Reads:
        - self.model_k_only (list[int]):
            0-based indices of parameters that belong to the k-only group in the
            full parameter vector.
        - self.const (list[list]):
            Each element is [i, _] where i is a 1-based index of a parameter
            that is fixed (constant).

    Procedure:
        1) Drop any indices from self.model_k_only that are listed as constants.
        2) For each remaining index k, subtract the number of constant indices
            that are strictly less than k (counting duplicates if present).
            This yields the index k would have after removing all constant
            positions from the full parameter vector.
        3) Store the resulting indices in descending order in self.p_k_only.

    Produces:
        - self.p_k_only (list[int]):
            Reindexed positions of k-only parameters in the reduced (constants-removed)
            parameter vector, sorted in descending order.
    """
    # Convert 1-based constant indices to 0-based and sort ascending
    const0 = sorted([c[0] - 1 for c in self.const])
    # Remove entries that are constants from model_k_only
    remain = [k for k in self.model_k_only if k not in const0]
    # Re-map each remaining index to its position after removing all constants
    res = []
    for k in remain:
        # Count how many constant positions occur strictly before k
        shift = 0
        for c in const0:
            if c < k:
                shift += 1
        # New index after removing the preceding constants
        res.append(k - shift)
    # Store in descending order as required
    self.p_k_only = sorted(res, reverse=True)


def test_k_only(self):
    self.test_k_only_unit('VG', (1, 2), [5, 3, 2])
    self.test_k_only_unit('VG', (1, 2, 3), [4, 2, 1])
    self.test_k_only_unit('VG', (1, 2, 3, 7), [3, 2, 1])
    self.test_k_only_unit('VG', (1, 2, 3, 4), [3, 1, 0])
    self.test_k_only_unit('VG', (7,), [6, 5, 4])
    self.test_k_only_unit('VG', (1, 2, 8), [3, 2])
    self.test_k_only_unit('VG', (1, 2, 3, 4, 6), [2, 0])
    self.test_k_only_unit('VG', (1, 3, 4, 6), [3, 1])
    self.test_k_only_unit('VG', (1, 3, 4, 5), [3, 1])


def test_k_only_unit(self, model, const, result):
    import json
    import sys
    from .unsatfit import Fit
    const_par = []
    for c in const:
        const_par.append([c, 0])
    f = Fit()
    f.swrc = (1, 2, 3)
    f.unsat = (2, 3, 4)
    f.set_model(model, const=const_par)
    f.k_only()
    if json.dumps(f.p_k_only) == json.dumps(result):
        if self.debug:
            print(
                f'success: model_k_only = {f.model_k_only} const = {const} p_k_only = {f.p_k_only}')
    else:
        print(
            f'Test failed with test_k_only_unit().\nk_only = {f.model_k_only} const = {const} p_k_only = {f.p_k_only} expected {result}')
        sys.exit()
