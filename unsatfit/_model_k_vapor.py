# Isothermal vapor hydraulic conductivity
import numpy as np


def init_model_k_vapor(self):
    # Physical parameters
    self.temperature = 20  # temperature in degree Celcius
    self.water_density = 1000  # water density in kg / m^3
    self.gravity = 9.81  # gravitational acceleration in m / s^2
    # Conversion factors of input data
    self.convert_h = 0.01  # convert pressure head to m H2O
    self.convert_theta = 1  # convert water content to volumetric fraction
    self.convert_k = 0.01  # convert hydraulic conductivity to m/s


def model_k_vapor(self, h, theta, theta_s):
    """Isothermal vapor hydraulic conductivity

    as a function of h, θ, θs, defined in Saito et al. (2006)
    https://doi.org/10.2136/vzj2006.0007

    === How to use (example code) ===

    import unsatfit
    f = unsatfit.Fit()
    # Set temperature and conversion factors of input data
    f.temperature = 20  # temperature in degree Celcius
    f.convert_h = 0.01  # convert pressure head to m H2O
    f.convert_theta = 1  # convert water content to volumetric fraction
    f.convert_k = 0.01  # convert hydraulic conductivity to m/s
    # Set "k_vapor=True" when using set_model()
    # Then vapor component is added to hydraulic conductivity function
    f.set_model('DVC', const=[f.get_wrf_vg2ch()], k_vapor=True)
    """
    # Physical constant in SI unit
    water_mole = 0.018015  # kg / mol
    gas_constant = 8.314462  # J / mol K
    # Conversion
    centigrade_offset = 273.15
    t = self.temperature + centigrade_offset
    h = h * self.convert_h
    theta_s = theta_s * self.convert_theta
    theta = theta * self.convert_theta
    # Calculation
    sat_vap_density = 0.001 * \
        np.exp(31.3716 - 6014.79 / t - 0.00792495 * t) / t
    diff_water_air = 0.0000214 * (t / centigrade_offset) ** 2
    air_porosity = theta_s - theta
    tortuosity = air_porosity ** (7 / 3) / (theta_s ** 2)
    vapor_diffusivity = tortuosity * air_porosity * diff_water_air
    mgrt = water_mole * self.gravity / (gas_constant * t)  # Mg/RT
    relative_humidity = np.exp(-h * mgrt)
    k = vapor_diffusivity * sat_vap_density / \
        self.water_density * mgrt * relative_humidity
    k = k / self.convert_k
    return k
