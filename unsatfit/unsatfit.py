class Fit:
    """Fit water retention and unsaturated hydraulic conductivity functions

    unsatfit is a Python library for optimizing parameters of functions of
    soil hydraulic properties (water retention function and unsaturated
    hydraulic conductivity function).

    See document at https://sekika.github.io/unsatfit/

    PyPI: https://pypi.org/project/unsatfit/
    Source: https://github.com/sekika/unsatfit
    Author: Katsutoshi Seki
    License: MIT License

    Reference

    Seki, K., Toride, N., & Th. van Genuchten, M. (2022) Closed-form hydraulic
        conductivity equations for multimodal unsaturated soil hydraulic properties.
        Vadose Zone J. 21, e20168. https://doi.org/10.1002/vzj2.20168
    """

    from ._init_model import init_model, set_model, get_init_not_defined, get_wrf_not_defined  # type: ignore
    from ._init_bound import init_bound  # type: ignore
    from ._init_lsq import init_lsq  # type: ignore
    from ._init_fig import init_fig  # type: ignore

    from ._model_bc import init_model_bc, bound_bc, bc, bc_se, bc_k, get_init_bc, get_wrf_bc  # type: ignore
    from ._model_vg import init_model_vg, bound_vg, vg, vg_se, vg_k, get_init_vg, get_wrf_vg, bound_mvg, mvg, mvg_se, mvg_k  # type: ignore
    from ._model_ko import init_model_ln, bound_ln, ln, ln_se, ln_k, get_init_ln, get_wrf_ln  # type: ignore
    from ._model_fx import init_model_fx, bound_fx, fx, fx_se, get_init_fx, get_wrf_fx  # type: ignore
    from ._model_dual_bc import init_model_bc2, bound_bc2f, bc2f, bc2f_se, bc2f_k, get_init_bc2f, get_wrf_bc2f, bound_bc2, bc2, bc2_se, bc2_k, get_init_bc2, get_wrf_bc2, bc2ca_k  # type: ignore
    from ._model_dual_vg import init_model_vg2, bound_vg2, vg2, vg2_se, vg2_k, get_init_vg2, get_wrf_vg2, bound_vg2ch, vg2ch, vg2ch_se, vg2ch_k, get_init_vg2ch, get_wrf_vg2ch, vg2chca_k  # type: ignore
    from ._model_dual_ko import init_model_ln2, bound_ln2, ln2, ln2_se, ln2_k, get_init_ln2, get_wrf_ln2, bound_ln2ch, ln2ch, ln2ch_se, ln2ch_k, get_init_ln2ch, get_wrf_ln2ch  # type: ignore
    from ._model_vgbc import init_model_vgbc, bound_vgbc, vgbc, vgbc_se, vgbc_k, get_init_vgbc, get_wrf_vgbc, bound_vgbcp2, vgbcp2_k, bound_vgbcch, vgbcch, vgbcch_se, vgbcch_k, get_init_vgbcch, get_wrf_vgbcch, bound_vgbcchp2, vgbcchp2, vgbcchp2_k  # type: ignore
    from ._model_kobc import init_model_kobc, bound_kobc, kobc, kobc_se, kobc_k, get_init_kobc, get_wrf_kobc, bound_kobcp2, kobcp2_k, bound_kobcch, kobcch, kobcch_se, kobcch_k, get_init_kobcch, get_wrf_kobcch, bound_kobcchp2, kobcchp2_k, kobcchca_k  # type: ignore
    from ._model_fs import init_model_fs, bound_vgfs, vgfs, vgfs_se, vgfs_k, get_init_vgfs, get_wrf_vgfs  # type: ignore
    from ._model_pe import init_model_pe, bound_pk, pk, pk_se, pk_k, get_init_pk, get_wrf_pk  # type: ignore
    from ._model_modified import modified_model, modified_ht, modified_hk  # type: ignore

    from ._optimize import optimize, multi_ini, format, residual_ht, residual_ln_hk, residual_log10_hk, f_r2_ht, f_r2_ln_hk, p_ht, total_cost  # type: ignore
    from ._figure import set_scale, add_curve, clear_curves, h_0to1, plot  # type: ignore
    from ._contour import contour, label  # type: ignore
    from ._pore_size import f_pore, f_pore_log, f_dtdh  # type: ignore

    from ._test import test, test_confirm  # type: ignore

    def __init__(self):
        self.debug = False
        self.swrc = self.unsat = []  # Set empty data
        self.init_model()  # Define soil hydraulic models
        self.init_bound()  # Boundary conditions
        self.init_lsq()   # Parameters for least square optimization
        self.init_fig()   # Parameters for figure

    def version(self):
        """get version"""
        import configparser
        import os
        inifile = configparser.ConfigParser()
        here = os.path.abspath(os.path.dirname(__file__))
        inifile.read(os.path.join(here, 'data/system.ini'))
        return inifile.get('system', 'version')

    def linear_regress(self, x, y):
        """Linear regression y = ax"""
        import numpy as np
        return np.dot(x, y) / (x**2).sum()
