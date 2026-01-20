#!/usr/bin/env python3
import numpy as np
import pandas as pd
import unsatfit

MODEL = 'VVP'
HE = 6.3e6  # pressure head of zero water content
MIN_H = 0.1
MAX_N = 15

# Read data from csv file
ht = pd.read_csv('swrc.csv')
h_t = np.array(ht['h'])
theta = np.array(ht['theta'])
# Get optimized WRF parameters
qs = max(theta)
f = unsatfit.Fit()
f.set_model(MODEL, const=[f'qs={qs}', 'qr=0', f'he={HE}', 'q=1'])
f.swrc = (h_t, theta)
f.b_a1 = f.b_a2 = f.b_a3 = (0, 1 / MIN_H)
f.b_m = (0, 1 - 1 / MAX_N)
f.ini = f.get_init(HE)
f.optimize()
w1, a1, m1, ww2, a2, m2 = f.fitted
w2 = (1-w1) * ww2
n1, n2 = [1 / (1 - m) for m in (m1, m2)]
print(f'{MODEL} model with qs={qs:.3} qr = 0 he={HE}')
print(f'w1 = {w1:.3f} 1/α1 = {1/a1:.3g} n1 = {n1:.3f} w2 = {w2:.3f} 1/α2 = {1/a2:.0f} n2 = {n2:.3f}')
print(f'R2 = {f.r2_ht:.5} AIC = {f.aic_ht:.5}')
f.save_fig = True
f.filename = MODEL + '.svg'
f.plot()
