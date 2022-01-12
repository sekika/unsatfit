import numpy as np
import pandas as pd
import unsatfit

# Filename
DATA_SWRC = 'ht3393.csv'
DATA_HCC = 'hk3393.csv'
FIG = 'VG-Mualem.png'
# Read csv data
ht = pd.read_csv(DATA_SWRC, comment='#')
h_t = np.array(ht['h'])
theta = np.array(ht['theta'])
ht = pd.read_csv(DATA_HCC, comment='#')
h_k = np.array(ht['h'])
k = np.array(ht['K'])
# Optimize parameters
f = unsatfit.Fit() # Create instance for fitting
f.swrc = (h_t, theta) # Data of soil water retention
f.unsat = (h_k, k) # Data of unsaturated hydraulic conductivity
wrf = f.get_wrf_vg() # Get water retention paramters
f.set_model('VG', const=[wrf]) # Set model and constant parameters
f.ini = (max(k), 2, 2) # Set initial paramter
f.b_Ks = (max(k)*0.9, max(k)*2) # Set bound for Ks
f.optimize() # Optimize
ks, p, r = f.fitted  # Get result
print(f.message)  # Show result
# Save figure
f.label_head = 'Matric head (cm)'
f.label_theta = 'Volumetric water content'
f.label_k = 'Hydraulic conductivity (cm/s)'
f.data_legend = 'UNSODA 3393'
f.line_legend = 'VG-Mualem with p={0:.2} r={1:.2}'.format(p, r)
f.legend_loc = 'center right'
f.save_fig = True
f.filename = FIG
f.plot()
