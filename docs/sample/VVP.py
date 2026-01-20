#!/usr/bin/env python3
import numpy as np
import pandas as pd
import unsatfit

MODEL = 'VVP'
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
# Set parameters for isothermal vapor hydraulic conductivity
f = unsatfit.Fit()
f.temperature = 20  # temperature in degree Celcius
f.convert_h = 0.01  # convert pressure head to m H2O
f.convert_theta = 1  # convert water content to volumetric fraction
f.convert_k = 0.01 / 86400  # convert hydraulic conductivity to m/s
# Get optimized WRF parameters
f.swrc = (h_t, theta)
f.unsat = (h_k, k)
f.b_a1 = f.b_a2 = f.b_a3 = (0, 1 / MIN_H)
f.b_m = (0, 1 - 1 / MAX_N)
w1, a1, m1, ww2, a2, m2 = f.get_init_vvp(HE)
wrf = (max(theta), 0, w1, a1, m1, ww2, a2, m2, HE, 1)
w2 = (1-w1) * ww2
n1, n2 = [1 / (1 - m) for m in (m1, m2)]
# Set HCF model with isothermal vapor hydraulic conductivity at 20C
model = MODEL
f.set_model(model, const=[wrf, f'Ks={KS}', 'a=1.5'], k_vapor=True)
# Show model description to optimize HCF function
print(f.model_description)
print(f'Therefore w2 = {w2:.3f} n1 = {n1:.3f} n2 = {n2:.3f}')
# Set initial parameters
p = (1, 2, 4, 6)  # Initial values of p
r = (0.5, 1, 2)  # Initial values of r
f.ini = (p, r)
# Set bound of parameters
f.b_p = (0.3, 10)  # Minimum and maximum of p
f.b_r = (0.1, 2.5)  # Minimum and maximum of q
# Optimize
f.optimize()
if not f.success:
    print(f.message)  # Show error message
    exit(1)
p, r = f.fitted  # Fitted parameters
# Show optimized HCF parameters and R2
print(f'Hydraulic conductivity parameters (Ks={KS}) and R2')
print(f.message)
# Set figure options
f.min_x_log = 0.1
f.max_x = HE
f.min_y2 = 10**(-8)
f.label_head = 'Pressure head'
f.label_theta = 'Volumetric water content'
f.label_k = 'Hydraulic conductivity (cm / d)'
f.legend_loc = 'upper right'  # Location of the legend
f.data_legend = 'Measured'
f.line_legend = f'{model} p={p:.1f} r={r:.1f}'
# Save figure
f.save_fig = True
# PDF file can be produced by changing from '.svg' to '.pdf'
f.filename = MODEL + '.svg'
f.plot()  # Draw figure
