#!/usr/bin/env python3
import numpy as np
import pandas as pd
import unsatfit
import requests
import sys

MODELS = ['dual-BC', 'dual-VG', 'dual-KO']
UNSODA_DATA = "https://sekika.github.io/file/unsoda/unsoda.json"
# Bound of theta_s / max(theta)
BOUND_THETA_S = (0.95, 1.5)
# Upper limit of n_1, n_2
MAX_N = 8
# Lower limit of sigma_1, sigma_2
MIN_SIGMA = 0.2

# Get UNSODA data
# See https://sekika.github.io/file/unsoda/
response = requests.get(UNSODA_DATA)
response.raise_for_status()
unsoda = response.json()
h_t = unsoda["lab_drying_h-t"]
for id in h_t:
    texture = unsoda['general'][id]['texture']
    h = np.array(h_t[id][0])
    theta = np.array(h_t[id][1])
    if len(h) < 7:
        continue
    f = unsatfit.Fit()
    # Set figure options
    f.fig_width = 4.3
    f.fig_height = 3.2
    f.top_margin = 0.05
    f.bottom_margin = 0.17
    f.left_margin = 0.17
    f.right_margin = 0.05
    f.label_head = 'Pressure head'
    f.label_theta = 'Volumetric water content'
    f.legend_loc = 'upper right'  # Location of the legend
    f.legend_opacity = 0.8
    # Save figure
    f.save_fig = True
    print(f'======== UNSODA {id} {texture} ========')
    f.swrc = (h, theta)
    f.filename = f'unsoda{id}.pdf'
    minAIC = 99999
    f.max_y1 = max(theta) * 1.2
    if max(theta) * 0.6 > min(theta):
        f.legend_loc = 'upper right'
    else:
        f.legend_loc = 'lower right'
    for model in MODELS:
        if model in ['dual-VG']:
            const = ['qr=0', 'q=1']
            f.b_q = (0, 1 - 1/MAX_N)
        if model in ['dual-BC', 'dual-KO']:
            const = ['qr=0']
        f.b_m = (0, 1 - 1/MAX_N)
        f.b_sigma = (MIN_SIGMA, np.inf)
        f.set_model(model, const=const)
        f.b_qs = (max(theta) * x for x in BOUND_THETA_S)
        f.ini = (max(theta), *f.get_init())
        f.optimize()
        f.max_y1 = max(f.max_y1, f.fitted[0] * 1.2)
        if not f.success:
            print(f.message)
            sys.exit()
        print(f'===== {model} model with {",".join(const)} =====')
        print(f.message)
        if f.perr is not None:
            err = [f"{x:.3}" for x in f.perr]
            print(f'1-sigma uncertainty: {", ".join(err)}')
        if f.aicc_ht is None:
            print(
                f'R2 = {f.r2_ht:.5} AIC = {f.aic_ht:.5}')
        else:
            print(
                f'R2 = {f.r2_ht:.5} AIC = {f.aic_ht:.5} Corrected AIC = {f.aicc_ht:.5}')
            if f.aicc_ht < minAIC:
                minAIC = f.aicc_ht
                model_minAIC = model
        f.data_legend = f'UNSODA {id}'
        f.line_legend = f'{model}'
        if model == MODELS[-1]:
            f.plot()
        else:
            f.add_curve()

    # Show the model with the smallest corrected AIC
    print('===== Comparison =====')
    print(f'{model_minAIC} model has the smallest corrected AIC.')
