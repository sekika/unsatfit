"""Regression tests for tri-VG initialization with saturation data."""

import unittest
from unittest.mock import patch

import numpy as np

from unsatfit import Fit


class TriVGInitializationTest(unittest.TestCase):
    def make_fit(self, positive_points, include_zero=True):
        f = Fit()
        h = np.logspace(-1, 5, positive_points)
        if include_zero:
            h = np.r_[0, h]
        f.set_model('tri-VG', const=['qs=1', 'qr=0', 'q=1'])
        parameters = (0.3, 1, 0.6, 0.5, 0.01, 0.5, 0.0001, 0.4)
        f.swrc = (h, f.f_ht(parameters, h))
        return f

    def check_polynomial_input(self, include_zero):
        f = self.make_fit(13, include_zero)
        h, theta = f.swrc
        polyfit = np.polyfit

        def checked_polyfit(x, y, degree):
            self.assertTrue(np.all(np.isfinite(x)))
            np.testing.assert_allclose(x, np.log10(h[h > 0]))
            np.testing.assert_allclose(y, (theta / max(theta))[h > 0])
            return polyfit(x, y, degree)

        with patch('numpy.polyfit', side_effect=checked_polyfit) as polynomial:
            parameters = f.get_init_vg3()
        polynomial.assert_called_once()
        self.assertEqual(len(parameters), 8)
        self.assertTrue(np.all(np.isfinite(parameters)))
        np.testing.assert_array_equal(f.swrc[0], h)
        np.testing.assert_array_equal(f.swrc[1], theta)

    def test_zero_head_excluded_from_polynomial(self):
        self.check_polynomial_input(include_zero=True)

    def test_positive_heads(self):
        self.check_polynomial_input(include_zero=False)

    def test_too_few_positive_heads_use_fallback(self):
        f = self.make_fit(9)
        with patch('numpy.polyfit') as polynomial:
            parameters = f.get_init_vg3()
        polynomial.assert_not_called()
        self.assertEqual(len(parameters), 8)
        self.assertTrue(np.all(np.isfinite(parameters)))


if __name__ == '__main__':
    unittest.main()
