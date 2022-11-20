#!/usr/bin/env python3
import numpy as np
import pandas as pd
import unsatfit

MODEL = 'KBC'
HB = 2  # hb value of the modified model

# Read data from csv file
ht = pd.read_csv('swrc.csv')
h_t = np.array(ht['h'])
theta = np.array(ht['theta'])
ht = pd.read_csv('hcc.csv')
h_k = np.array(ht['h'])
k = np.array(ht['K'])
# Get optimized WRF parameters
f = unsatfit.Fit()
f.swrc = (h_t, theta)
f.unsat = (h_k, k)
qs, qr, w1, hm, s1, l2 = wrf = f.get_wrf_kobcch()
# Set HCF model
model = MODEL
f.set_model(model, const=[wrf, 'r=1'])
# Set modified model when sigma1 > 2
if s1 > 2:
    model = 'M' + MODEL
    f.modified_model(HB)  # Change to modified model
# Show model description to optimize HCF function
print(f.model_description)
# Set initial parameters
p = (1, 2, 4, 6)  # Initial values of p
q = (0.5, 1, 2)  # Initial values of q
f.ini = ((max(k),), p, q)
# Set bound of parameters
f.b_p = (0.3, 10)  # Minimum and maximum of p
f.b_q = (0.1, 2.5)  # Minimum and maximum of q
# Set bound of Ks
max_k = max(k) * 2
if min(h_k) > 1:
    max_k = max_k * (min(h_k)) ** 2
f.b_ks = (max(k) * 0.95, max_k)
# Optimize
f.optimize()
if not f.success:
    print(f.message)  # Show error message
    exit(1)
ks, p, q = f.fitted  # Fitted parameters
# Show optimized HCF parameters and R2
print('Hydraulic conductivity parameters and R2')
print(f.message)
# Set figure options
f.label_head = 'Pressure head'
f.label_theta = 'Volumetric water content'
f.label_k = 'Hydraulic conductivity'
f.legend_loc = 'upper right'  # Location of the legend
f.data_legend = 'Measured'
f.line_legend = '{0} p={1:.1f} q={2:.1f}'.format(model, p, q)
# Save figure
f.save_fig = True
# PDF file can be produced by changing from '.png' to '.pdf'
f.filename = MODEL + '.png'
f.plot()  # Draw figure
