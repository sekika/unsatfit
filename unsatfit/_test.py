def test(self):
    import numpy as np
    from .unsatfit import Fit
    f = Fit()
    # Test data from UNSODA 3393
    f.swrc = (np.array([10, 28, 74, 160, 288, 640, 1250, 2950, 6300, 10600, 15800]), np.array(
        [0.36, 0.35, 0.34, 0.33, 0.32, 0.3, 0.28, 0.26, 0.24, 0.22, 0.2]))
    f.unsat = (np.array([10, 28, 74, 160, 288, 640, 1250, 2950, 6300, 10600]), np.array(
        [0.384, 0.0988, 0.0293, 0.0137, 0.00704, 0.00315, 0.00085, 0.000206, 0.000101, 0.00006]) / 60 / 60 / 24)
    f.ini = (max(f.unsat[1]), 1.5)  # Initial values of Ks and p
    f.set_model('Brooks and Corey', const=[f.get_wrf_bc(), 'q=1', 'r=2'])
    f.test_confirm(829)
    f.set_model('van Genuchten', const=[f.get_wrf_vg(), 'r=2'])
    f.modified_model(2)
    f.test_confirm(922)
    f.set_model('Kosugi', const=[f.get_wrf_ln(), 'q=1', 'r=2'])
    f.test_confirm(954)
    f.set_model('dual-VG-CH', const=[f.get_wrf_vg2ch(), 'r=2'])
    f.test_confirm(893)
    f.set_model('KO1BC2-CH', const=[f.get_wrf_kobcch(), 'q=1', 'r=2'])
    f.test_confirm(966)
    f.set_model('KO1BC2', const=[f.get_wrf_kobc(), 'q=1', 'r=2'])
    f.modified_model(2)
    f.test_confirm(955)


def test_confirm(self, expect):
    self.optimize()
    result = int((self.r2_ht + self.r2_ln_hk) * 500)
    assert abs(expect - result) < 2, 'Test failed for {0}. Expected: {1} Actual: {2}\nResult: {3}'.format(
        self.model_name, expect, result, self.message)
