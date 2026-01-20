#!/usr/bin/env python3
import numpy as np
import pandas as pd
import unsatfit

# Read data from csv file
ht = pd.read_csv('swrc.csv')
h_t = np.array(ht['h'])
theta = np.array(ht['theta'])
hk = pd.read_csv('hcc.csv')
h_k = np.array(hk['h'])
k = np.array(hk['K'])
# Set parameters for isothermal vapor hydraulic conductivity
f = unsatfit.Fit()
f.temperature = 20  # temperature in degree Celcius
f.convert_h = 0.01  # convert pressure head to m H2O
f.convert_theta = 1  # convert water content to volumetric fraction
f.convert_k = 0.01  # convert hydraulic conductivity to m/s
# DBC model
# Get optimized WRF parameters
f.swrc = (h_t, theta)
f.unsat = (h_k, k)
qs, qr, hb, hc, l1, l2 = wrf = f.get_wrf_bc2()
w1 = 1/(1+(hc/hb)**(l2-l1))
# Set HCF model
model = 'DBC'
f.set_model(model, const=[wrf, 'r=1'], k_vapor=True) # adding vapor component
# Show model description to optimize HCF function
print(f.model_description)
print('Therefore w1 = {0:.3f}'.format(w1))
# Set initial parameters
ini_p = (1, 2, 4, 6)  # Initial values of p
ini_q = (0.5, 1, 2)  # Initial values of q
f.ini = ((max(k),), ini_p, ini_q)
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
# Show optimized HCF parameters and R2
print('Hydraulic conductivity parameters and R2')
print(f.message)
# Set figure options
f.max_x = 10**7
f.min_y2 = 10**(-14)
f.label_head = 'Pressure head'
f.label_theta = 'Volumetric water content'
f.label_k = 'Hydraulic conductivity'
f.legend_loc = 'upper right'  # Location of the legend
f.data_legend = 'Measured'
# Order of line color and style (cyclic)
f.color = ['blue', 'red', 'green', 'skyblue']
f.style = ['dotted', 'dashdot', 'dashed', 'solid']
# Add curve
f.line_legend = model
f.add_curve()

# DVC model
# Get optimized WRF parameters
qs, qr, w1, a1, m1, m2, q = wrf = f.get_wrf_vg2ch()
n1 = q/(1-m1)  # n1 is calculated from optimized m1
n2 = q/(1-m2)
# Set HCF model
model = 'DVC'
f.set_model(model, const=[wrf], k_vapor=True)
# Set modified model when sigma1 > 2
if min(n1, n2) < 1.1:
    model = 'M' + MODEL
    hb = 2  # hb value of the modified model
    f.modified_model(hb)  # Change to modified model
# Show model description to optimize HCF function
print(f.model_description)
print('Therefore n1 = {0:.3f} n2 = {1:.3f}'.format(n1, n2))
# Set initial parameters
ini_r = (0.5, 1, 2)  # Initial values of r
f.ini = ((max(k),), ini_p, ini_r)
# Optimize
f.optimize()
if not f.success:
    print(f.message)  # Show error message
    exit(1)
# Show optimized HCF parameters and R2
print('Hydraulic conductivity parameters and R2')
print(f.message)
# Add curve
f.line_legend = model
f.add_curve()

# KBC model
# Get optimized WRF parameters
qs, qr, w1, hm, s1, l2 = wrf = f.get_wrf_kobcch()
# Set HCF model
model = 'KBC'
f.set_model(model, const=[wrf, 'r=1'], k_vapor=True)
# Set modified model when sigma1 > 2
if s1 > 2:
    model = 'M' + MODEL
    hb = 2  # hb value of the modified model
    f.modified_model(hb)  # Change to modified model
# Show model description to optimize HCF function
print(f.model_description)
# Set initial parameters
f.ini = ((max(k),), ini_p, ini_q)
# Optimize
f.optimize()
if not f.success:
    print(f.message)  # Show error message
    exit(1)
# Show optimized HCF parameters and R2
print('Hydraulic conductivity parameters and R2')
print(f.message)
# Add curve
f.line_legend = model
f.add_curve()

# Peters model
# Get optimized WRF parameters
he = 6.3e6  # Constant value of h_0
qs, qr, w1, hm, sigma1, he = wrf = f.get_wrf_pk(he)
# Set HCF model
model = 'PE'
f.set_model(model, const=[wrf], k_vapor=True)
# Set modified model when sigma1 > 2
if sigma1 > 2:
    model = 'M' + MODEL
    hb = 2  # hb value of the modified model
    f.modified_model(hb)  # Change to modified model
# Show model description to optimize HCF function
print(f.model_description)
# Set initial and bound
ini_a = (1.5,)  # Initial value of a (positive)
ini_omega = (1e-5, 1e-3)  # Initial values of omeaga
f.ini = ((max(k),), ini_p, ini_a, ini_omega)
f.b_a = (0.5, 3.5)  # Minimum and maximum of a (positive)
# Optimize
f.optimize()
if not f.success:
    print(f.message)  # Show error message
    exit(1)
# Show optimized HCF parameters and R2
print('Hydraulic conductivity parameters and R2')
print(f.message)
# Draw figure
f.line_legend = model
# Save figure
f.save_fig = True
# PDF file can be produced by changing from '.png' to '.pdf'
f.filename = 'multi-v.png'
f.plot()
