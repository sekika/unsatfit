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


def find_pore_extreme(self, p, epsilon=1e-6):
    """
    Find inflection points of θ(h; p) on the log-h axis by solving d²θ/d(ln h)² = 0, then
    classify them into local maxima/minima and store the results in self.pore_maxima and
    self.pore_minima.

    Method:
    - Evaluate dθ/dln h = h * dθ/dh (d1_cdiff) using a high-order centered finite difference
    with a relative step (epsilon).
    - Evaluate d²θ/d(ln h)² (d2_cdiff) by differentiating d1_cdiff with the same scheme.
    - Build a geometric grid over [min(self.swrc[0]) / 2, max(self.swrc[0])] to detect sign
    changes (or near-zero crossings) of d²θ/d(ln h)² and form brackets.
    - Refine each bracket with Brent’s method (scipy.optimize.root_scalar) to locate roots.
    - Classify each root r as:
    - maximum if dθ/dln h(r) > dθ/dln h(1.1 r),
    - minimum if dθ/dln h(r) < dθ/dln h(1.1 r).

    Parameters:
    - p (array-like): Parameter vector consumed by self.f_ht.
    - epsilon (float, optional): Relative step for the centered finite-difference stencil
    (default: 1e-6). Smaller values increase round-off sensitivity; larger values increase
    discretization error.

    Requirements:
    - self.f_ht(p, h) must exist, accept scalar/array h, and be vectorized.
    - self.swrc must provide (h, θ) data with finite bounds to define the search interval.

    Returns:
    - None. Populates:
    - self.pore_maxima: list[float], locations h* of local maxima on the log-h axis.
    - self.pore_minima: list[float], locations h* of local minima on the log-h axis.

    Raises:
    - ValueError: If the h range inferred from self.swrc is invalid (non-finite or lo >= hi).

    Side effects:
    - Overwrites/creates self.pore_maxima and self.pore_minima.

    Notes:
    - Uses a 5-point-like centered finite difference for the first derivative on a relative
    step and applies it again to obtain the second derivative in log-scale.
    - Root finding uses a 512-point geometric grid, a scale-aware zero threshold, and
    fixed tolerances (xtol=rtol=1e-6, maxiter=100).
    - The number of minima/maxima depends on the model/data. Downstream plotting expects
    exactly two minima when pore segmentation is enabled.

    Example:
        self.find_pore_extreme(self.fitted)
    """
    import numpy as np
    from scipy.optimize import root_scalar

    def diff(f, p, h, epsilon=1e-8):
        h = np.asarray(h, dtype=float)
        t_m2 = f(p, h * (1 - 2 * epsilon))
        t_m1 = f(p, h * (1 - epsilon))
        t_p1 = f(p, h * (1 + epsilon))
        t_p2 = f(p, h * (1 + 2 * epsilon))
        return (t_m2 - 8 * t_m1 + 8 * t_p1 - t_p2) / (12 * epsilon * h)

    def d1_cdiff(p, h, epsilon=1e-6):
        """ Multiply h for converting to log scale """
        return h * diff(self.f_ht, p, h, epsilon)

    def d2_cdiff(p, h, epsilon=1e-6):
        return diff(d1_cdiff, p, h, epsilon)

    # Build initial grid only to form sign-change brackets
    grid_n = 512
    xtol = 1e-6
    rtol = 1e-6
    lo = min(self.swrc[0]) / 2
    hi = max(self.swrc[0])
    if not np.isfinite(lo) or not np.isfinite(hi) or lo >= hi:
        raise ValueError("Invalid h range.")
    xs = np.geomspace(lo, hi, grid_n)
    # Vectorized second derivative on the grid
    g2_vals = d2_cdiff(p, xs, epsilon)
    # Robust zero threshold (scale-aware)
    eps_zero = 1e-12 * (1.0 + np.nanmax(np.abs(g2_vals)))
    sign = np.sign(np.where(np.abs(g2_vals) < eps_zero, 0.0, g2_vals))
    # Collect brackets where sign changes or hits zero
    brackets = []
    for i in range(len(xs) - 1):
        s1, s2 = sign[i], sign[i + 1]
        if s1 == 0.0 or s1 * s2 < 0.0:
            brackets.append((xs[i], xs[i + 1]))
    # Scalar wrapper for root_scalar

    def g2_scalar(h):
        return float(d2_cdiff(p, np.array([h]), epsilon)[0])
    # Refine each bracket with Brent's method
    roots = []
    for a, b in brackets:
        try:
            sol = root_scalar(
                g2_scalar,
                bracket=[
                    a,
                    b],
                method='brentq',
                xtol=xtol,
                rtol=rtol,
                maxiter=100)
        except ValueError:
            continue
        if sol.converged:
            r = sol.root
            roots.append(r)
    # Retrieve maxima and minima of pore-size distribution
    self.pore_maxima, self.pore_minima = [], []
    for r in roots:
        inc = d1_cdiff(p, r, epsilon=1e-6) - \
            d1_cdiff(p, r * 1.1, epsilon=1e-6)
        if inc < 0:
            self.pore_maxima.append(r)
        elif inc > 0:
            self.pore_minima.append(r)
