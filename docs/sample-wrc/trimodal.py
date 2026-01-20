#!/usr/bin/env python3
import numpy as np
import pandas as pd
import unsatfit

MODELS = ['tri-VG', 'BVV', 'VVP']
HE = 6.3e6  # pressure head of zero water content

# Read data from csv file
ht = pd.read_csv('swrc.csv')
h_t = np.array(ht['h'])
theta = np.array(ht['theta'])
qs = max(theta)
f = unsatfit.Fit()
f.swrc = (h_t, theta)
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
f.data_legend = 'Measured'
# Save figure
f.save_fig = True
# PDF file can be produced by changing from '.svg' to '.pdf'
f.filename = 'trimodal.svg'

minAIC = 99999
for model in MODELS:
    if model in ['tri-VG', 'BVV']:
        const = [f'qs={qs}', 'qr=0', 'q=1']
        f.set_model(model, const=const)
        f.ini = f.get_init()
    if model in ['VVP']:
        const = [f'qs={qs}', 'qr=0', f'he={HE}', 'q=1']
        f.set_model(model, const=const)
        f.ini = f.get_init(HE)
    f.optimize()
    if not f.success:
        print(f.message)
        exit(1)
    print(f'===== {model} model with {",".join(const)} =====')
    print(f.message)
    err = [f"{x:.3}" for x in f.perr]
    print(f'1-sigma uncertainty: {", ".join(err)}')
    print(f'R2 = {f.r2_ht:.5} AIC = {f.aic_ht:.5} Corrected AIC = {f.aicc_ht:.5}')
    if f.aicc_ht < minAIC:
        minAIC = f.aicc_ht
        model_minAIC = model
    f.line_legend = f'{model}'
    if model == MODELS[-1]:
        f.plot()
    else:
        f.add_curve()

# Show the model with the smallest corrected AIC
print('===== Comparison =====')
print(f'{model_minAIC} model has the smallest corrected AIC.')
