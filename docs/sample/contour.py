#!/usr/bin/env python3
import numpy as np
import pandas as pd
import unsatfit

MODEL = 'KBC'

# Read data from csv file
ht = pd.read_csv('swrc.csv')
h_t = np.array(ht['h'])
theta = np.array(ht['theta'])
hk = pd.read_csv('hcc.csv')
h_k = np.array(hk['h'])
k = np.array(hk['K'])
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
    hb = 2  # hb value of the modified model
    f.modified_model(hb)  # Change to modified model
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
f.fig_width = 3.5  # inches
f.fig_height = 2.5
f.bottom_margin = 0.2
f.contour_range_x = 0, 8/p  # min/p, max/p
f.contour_range_y = 0, 2.2/q  # min/q, max/q
f.contour_color = 'black'
f.contour_level = 14
f.contour_marker_color = 'black'
# Draw contour plot
f.save_fig = True
f.filename = 'contour.png'
f.contour('p', 'q')
