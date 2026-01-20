#!/usr/bin/env python3
import numpy as np
import pandas as pd
import unsatfit

MODELS = ['dual-VG', 'tri-VG', 'BVV', 'VVP']
HE = 6.3e6  # pressure head of zero water content
KS = 3.29 # Constant saturated hydraulic conductivity
MIN_H = 0.1
MAX_N = 15
SATURATED_H = 0.1

# Read data from csv file
ht = pd.read_csv('swrc.csv')
h_t = np.array(ht['h'])
theta = np.array(ht['theta'])
hk = pd.read_csv('hcc.csv')
h_k = np.array(hk['h'])
k = np.array(hk['K'])
# Add saturated point to h-K data
h_k = np.concatenate(([SATURATED_H], h_k))
k = np.concatenate(([KS], k))
f = unsatfit.Fit()
f.swrc = (h_t, theta)
f.unsat = (h_k, k)
# Set parameters for isothermal vapor hydraulic conductivity
f.temperature = 20  # temperature in degree Celcius
f.convert_h = 0.01  # convert pressure head to m H2O
f.convert_theta = 1  # convert water content to volumetric fraction
f.convert_k = 0.01 / 86400  # convert hydraulic conductivity to m/s
# Set initial parameters
p = (1, 2, 4, 6)  # Initial values of p
r = (0.5, 1, 2)  # Initial values of r
f.ini = (p, r)
# Set bound of parameters
f.b_hb = (MIN_H, np.inf)
f.b_a1 = f.b_a2 = f.b_a3 = (0, 1 / MIN_H)
f.b_m = (0, 1 - 1 / MAX_N)
f.b_p = (0.3, 10)  # Minimum and maximum of p
f.b_r = (0.1, 2.5)  # Minimum and maximum of q
# Set figure options
f.min_x_log = 0.1
f.max_x = 6.3E6
f.min_y2 = 10**(-8)
f.label_head = 'Pressure head'
f.label_theta = 'Volumetric water content'
f.label_k = 'Hydraulic conductivity (cm / d)'
f.legend_loc = 'upper right'  # Location of the legend
f.data_legend = 'Measured'
# Save figure
f.save_fig = True
# PDF file can be produced by changing from '.svg' to '.pdf'
f.filename = 'trimodal.svg'

for model in MODELS:
    if model == 'dual-VG':
        wrf = (max(theta), 0, *f.get_init_vg2(), 1)
        f.set_model(model, const=[wrf, f'Ks={KS}'], k_vapor=True)
    elif model == 'tri-VG':
        wrf = (max(theta), 0, *f.get_init_vg3(), 1)
        f.set_model(model, const=[wrf, f'Ks={KS}'], k_vapor=True)
    elif model == 'BVV':
        wrf = (max(theta), 0, *f.get_init_bvv(), 1)
        f.set_model(model, const=[wrf, f'Ks={KS}'], k_vapor=True)
    else:
        wrf = (max(theta), 0, *f.get_init_vvp(HE), HE, 1)
        f.set_model(model, const=[wrf, f'Ks={KS}', 'a=1.5'], k_vapor=True)
    print(f.model_description)
    f.optimize()
    if not f.success:
        print(f.message)
        exit(1)
    p, r = f.fitted
    # Show optimized HCF parameters and R2
    print(f'Hydraulic conductivity parameters (Ks={KS}) and R2')
    print(f.message)
    f.line_legend = f'{model}'
    if model == MODELS[-1]:
        f.plot()
    else:
        f.add_curve()
