#!/usr/bin/env python3
import numpy as np
import pandas as pd
import unsatfit

MODEL = 'DK'

# Read data from csv file
ht = pd.read_csv('swrc.csv')
h_t = np.array(ht['h'])
theta = np.array(ht['theta'])
# Get optimized WRF parameters
f = unsatfit.Fit()
f.set_model(MODEL, const=['qr=0'])
f.swrc = (h_t, theta)
# Set initial parameters
f.ini = (max(theta), *f.get_init())
# Optimize
f.optimize()
if not f.success:
    print(f.message)  # Show error message
    exit(1)
# Show optimized parameters
print(f'{MODEL} model with qr = 0')
print(f.message)
err = [f"{x:.3}" for x in f.perr]
print(f'1-sigma uncertainty: {", ".join(err)}')
print(f'R2 = {f.r2_ht:.5} AIC = {f.aic_ht:.5} Corrected AIC = {f.aicc_ht:.5}')
print(f'Correlation matrix\n{f.cor}')
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
f.line_legend = f'{MODEL}'
# Save figure
f.save_fig = True
# PDF file can be produced by changing from '.png' to '.pdf'
f.filename = MODEL + '.png'
f.plot()  # Draw figure
