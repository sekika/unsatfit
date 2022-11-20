#!/usr/bin/env python3
import numpy as np
import pandas as pd
import unsatfit

MODEL = 'VG'
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
qs, qr, a, m, q = wrf = f.get_wrf_vg()
n = q/(1-m)  # n is calculated from optimized m
# Set HCF model
model = MODEL
f.set_model(model, const=[wrf, 'r=2'])
# Set modified model when sigma1 > 2
if n < 1.1:
    model = 'M' + MODEL
    f.modified_model(HB)  # Change to modified model
# Show model description to optimize HCF function
print(f.model_description)
print('Therefore n = {0:.3f}'.format(n))
# Set initial parameters
p = (1, 2, 4, 6)  # Initial values of p
f.ini = ((max(k),), p)
# Set bound of parameters
f.b_p = (-1, 6)  # Minimum and maximum of p
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
ks, p = f.fitted  # Fitted parameters
# Show optimized HCF parameters and R2
print('Hydraulic conductivity parameters and R2')
print(f.message)
# Set figure options
f.label_head = 'Pressure head'
f.label_theta = 'Volumetric water content'
f.label_k = 'Hydraulic conductivity'
f.legend_loc = 'upper right'  # Location of the legend
f.data_legend = 'Measured'
f.line_legend = '{0} p={1:.1f}'.format(model, p)
# Save figure
f.save_fig = True
# PDF file can be produced by changing from '.png' to '.pdf'
f.filename = MODEL + '.png'
f.plot()  # Draw figure
