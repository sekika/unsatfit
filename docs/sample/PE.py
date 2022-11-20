#!/usr/bin/env python3
import numpy as np
import pandas as pd
import unsatfit

MODEL = 'PE'
HB = 2  # hb value of the modified model
H0 = 6.3e6  # Se=0 at h=H0

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
qs, qr, w1, hm, sigma1, he = wrf = f.get_wrf_pk(H0)
# Set HCF model
model = MODEL
f.set_model(model, const=[wrf])
# Set modified model when sigma1 > 2
if sigma1 > 2:
    model = 'M' + MODEL
    f.modified_model(HB)  # Change to modified model
# Show model description to optimize HCF function
print(f.model_description)
# Set initial parameters
p = (1, 2, 4, 6)  # Initial values of p
a = (1.5,)  # Initial value of a (positive)
omega = (1e-5, 1e-3)  # Initial values of omeaga
f.ini = ((max(k),), p, a, omega)
# Set bound of parameters
f.b_p = (0.3, 10)  # Minimum and maximum of p
f.b_a = (0.5, 3.5)  # Minimum and maximum of a (positive)
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
ks, p, a, omega = f.fitted  # Fitted parameters
# Show optimized HCF parameters and R2
print('Hydraulic conductivity parameters and R2')
print(f.message)
# Set figure options
f.label_head = 'Pressure head'
f.label_theta = 'Volumetric water content'
f.label_k = 'Hydraulic conductivity'
f.legend_loc = 'upper right'  # Location of the legend
f.data_legend = 'Measured'
f.line_legend = '{0} p={1:.1f} a=-{2:.1f} $\omega$={3:.1e}'.format(
    model, p, a, omega)
# Save figure
f.save_fig = True
# PDF file can be produced by changing from '.png' to '.pdf'
f.filename = MODEL + '.png'
f.plot()  # Draw figure
