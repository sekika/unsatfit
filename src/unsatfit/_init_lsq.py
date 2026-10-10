def init_lsq(self):
    """Set initial parameters for least square optimization

    Parameters are passed to scipy.optimize.least_squares
    See description at
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html
    """
    self.lsq_method = 'trf'  # 'trf' and 'dogbox' can be selected. 'lm' is not possible as it has no bounds
    self.lsq_jac = '2-point'  # 2-point’, ‘3-point’, ‘cs’
    # Loss function. ‘linear’, ‘soft_l1’, ‘huber’, ‘cauchy', ‘arctan’
    self.lsq_loss = 'linear'
    self.lsq_verbose = 0  # Level of algorithm’s verbosity. (0, 1, 2)
    # ftol changes stepwise in this order
    self.lsq_ftol = [0.1, 0.01, 1e-3, 1e-4, 1e-6, 1e-8]
    # ftol for initial estimation of mutiple initial parameter sets
    self.lsq_ftol_global = [1, 0.1]
    self.lsq_max_nfev = 1000  # Number of evaluation
