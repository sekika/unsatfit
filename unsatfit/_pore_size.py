# Pore size distribution


def f_pore(self, p, r, C=0.149, epsilon=1e-8):
    """
    Pore-size distribution function dθ/dr

    Note that figure should be drawn with normal scale.
    For using log-scale of pore-size, use f_pore_log.

    Parameters:
    -----------
    p : dict or array-like
        parameter of water retention function
    r : numpy.ndarray
        pore size
    C : float
        constant for relationship h = C/r
        unit dependent. 0.149 cm^2
    epsilon: float
        increment of numerical differentiation

    Returns:
    --------
    numpy.ndarray
        dθ/dr
    """
    h = C / r
    return -C / (r**2) * self.f_dtdh(p, h, epsilon=epsilon)


def f_pore_log(self, p, r, C=0.149, epsilon=1e-8):
    """
    Pore-size distribution function dθ/d(ln r)

    Parameters:
    -----------
    p : dict or array-like
        parameter of water retention function
    r : numpy.ndarray
        pore size
    C : float
        constant for relationship h = C/r
        unit dependent. 0.149 cm^2
    epsilon: float
        increment of numerical differentiation

    Returns:
    --------
    numpy.ndarray
        dθ/d(ln r)
    """
    h = C / r
    return -h * self.f_dtdh(p, h, epsilon=epsilon)


def f_dtdh(self, p, h, epsilon=1e-8):
    """
    dθ/dh calculated with numerical differentiation,
            using 4-point central difference formula

    Parameters:
    -----------
    p : dict or array-like
        parameter of water retention function
    h : numpy.ndarray
        pressure head
    epsilon: float
        increment of numerical differentiation

    Returns:
    --------
    numpy.ndarray
        dθ/dh
    """
    theta_values = [self.f_ht(p, h + k * epsilon) for k in [-2, -1, 1, 2]]
    return sum(
        k * theta for k, theta in zip([1, -8, 8, -1], theta_values)) / (12 * epsilon)
