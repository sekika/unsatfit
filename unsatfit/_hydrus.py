import math
import numpy as np
import sys


def save_template(self, filename="model.tpl"):
    """
    Save a PEST template file for the current hydraulic model.

    This function writes a template (`.tpl`) file in which model parameters
    are represented by PEST placeholders. The template can be used by PEST
    to generate input files during inverse analysis.

    Parameters
    ----------
    filename : str, optional
        Output filename for the template file (default: "model.tpl").

    Output
    ------
    Writes a text file containing:
        - the PEST template header ("ptf #"),
        - the model name,
        - parameter placeholders in the order required by the model.
    """
    with open(filename, "w") as out:
        print('ptf #', file=out)
        print(self.model_name, file=out)
        model = self.model[self.model_name]
        for param in model['param']:
            print(f'# {param:10} #', file=out)


def save_input(self, filename="model.inp", hc_param=[]):
    """
    Save a model input file (`model.inp`) containing parameter values.

    This function writes the model name and parameter values in the format
    required by unsatfit and HYDRUS workflows. Parameters are written in the
    order defined by the selected hydraulic model.

    Parameters
    ----------
    filename : str, optional
        Output filename for the input file (default: "model.inp").
    hc_param : list of float, optional
        Hydraulic conductivity (HCF) parameters to be used when only water
        retention (WRF) parameters are fitted (`self.ht_only == True`).
        Values must be provided in the required order.

    Output
    ------
    Writes a text file containing:
        - the model name (first line),
        - parameter values (one per line, in model-defined order).

    Notes
    -----
    - If `self.ht_only` is True, missing HCF parameters must be provided via
      `hc_param`, otherwise execution stops with an error.
    - Constant parameters are written using predefined values.
    """
    with open(filename, "w") as out:
        print(self.model_name, file=out)
        model = self.model[self.model_name]
        if self.ht_only:
            wrf = hcf = 0
            for param in model['param']:
                if param in self.param_ht:
                    print(self.fitted[wrf], file=out)
                    wrf += 1
                elif param in self.param_const:
                    print(dict(zip(self.param_const, self.value_const))[
                        param], file=out)
                else:
                    if len(hc_param) <= hcf:
                        print(
                            f'save_input(): Parameter {param} is not given. Provide it with hc_param.')
                        sys.exit(1)
                    print(hc_param[hcf], file=out)
                    hcf += 1
        else:
            i = 0
            for param in model['param']:
                if param in self.param:
                    print(self.fitted[i], file=out)
                    i += 1
                else:
                    print(dict(zip(self.param_const, self.value_const))[
                        param], file=out)


def load_input(self, filename="model.inp"):
    """
    Load model parameters from a `model.inp` file.

    This function reads a model input file and assigns parameter values
    to the current instance. The model type and parameter order are inferred
    from the file content.

    Parameters
    ----------
    filename : str, optional
        Input filename to read (default: "model.inp").

    Input format
    ------------
    The file must contain:
        - the model name on the first line,
        - parameter values (one per line) in the required order.

    Effects
    -------
    - Sets `self.parameters` as a dictionary of parameter values.
    - Updates the model configuration via `set_model`.
    - Sets `self.ht_only` to False.
    """
    with open(filename) as f:
        model = f.readline().strip()
        value = [float(x) for x in f.read().splitlines() if x]
        self.parameters = dict(zip(self.model[model]['param'], value))
        self.ht_only = False
        const = []
        i = 1
        for c in value:
            const.append([i, c])
            i += 1
        self.set_model(model, const=const)


def save_mater(self, filename="Mater.in"):
    """
    Generate a HYDRUS lookup-table file (`Mater.in`) from the current model.

    This function evaluates the water retention function (WRF),
    hydraulic conductivity function (HCF), and capacity function over a
    pressure head range, and writes them in HYDRUS lookup-table format.

    Parameters
    ----------
    filename : str, optional
        Output filename for the lookup table (default: "Mater.in").

    Output
    ------
    Writes a HYDRUS-compatible `Mater.in` file containing:
        - number of data points,
        - columns of water content (theta), pressure head (h),
          hydraulic conductivity (K), and capacity (C).

    Notes
    -----
    - The pressure head range is generated by `lin_h()`.
    - The number of points is controlled by `self.points`.
    """
    h = self.lin_h()
    theta = self.f_ht([], h)
    k = self.f_hk([], h)
    c = -self.f_dtdh([], h, epsilon=1e-8)
    with open(filename, "w") as out:
        print('iCap (=1: input capacity; =0: otherwise)', file=out)
        print('1', file=out)
        print('NTab', file=out)
        print(len(theta), file=out)
        print('theta        h          K           C', file=out)
        for point in zip(theta, h, k, c):
            print(
                f'{point[0]:.5f} {-point[1]:.4E} {point[2]:.4E} {point[3]:.4E}', file=out)


def lin_h(self):
    """
    Generate a pressure head array for lookup-table evaluation.

    This function creates a logarithmically spaced array of pressure head
    values used to compute hydraulic properties for the `Mater.in` file.
    The range is determined based on model parameters and user-defined bounds.

    Returns
    -------
    numpy.ndarray
        Array of pressure head values.

    Notes
    -----
    - The range is defined by `self.min_h` and `self.max_h`.
    - The number of points is given by `self.points`.
    """
    param = self.model[self.model_name]['param']

    def h(h2):
        h1 = np.array([self.min_h,])
        qs = self.parameters['qs']
        while self.f_ht([], h2) < qs * 0.999:
            h2 /= 2
        if h2 < self.min_h:
            return 2**np.linspace(math.log2(self.min_h),
                                  math.log2(self.max_h), num=self.points)
        hp = 2**np.linspace(math.log2(h2),
                            math.log2(self.max_h), num=self.points - 1)
        return np.concatenate((h1, hp))
    for key in ['hb', 'hb1', 'hm', 'hm1']:
        if key in param:
            return h(self.parameters[key])
    for key in ['a', 'a1']:
        if key in param:
            return h(1 / self.parameters[key])
    return 2**np.linspace(math.log2(self.min_h),
                          math.log2(self.max_h), num=self.points)
