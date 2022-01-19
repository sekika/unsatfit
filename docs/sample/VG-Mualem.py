import numpy as np
import pandas as pd
import unsatfit

### Specify file names ###
DATA_SWRC = 'ht3393.csv'
DATA_HCC = 'hk3393.csv'
FIG = 'VG-Mualem.png'
### Read data from csv file ###
ht = pd.read_csv(DATA_SWRC, comment='#')
h_t = np.array(ht['h'])
theta = np.array(ht['theta'])
ht = pd.read_csv(DATA_HCC, comment='#')
h_k = np.array(ht['h'])
k = np.array(ht['K']) / 24 / 3600
### Optimize parameters ###
f = unsatfit.Fit()  # Create instance for fitting
f.swrc = (h_t, theta)  # Data of soil water retention
f.unsat = (h_k, k)  # Data of unsaturated hydraulic conductivity
wrf = f.get_wrf_vg()  # Get water retention paramters
model = 'VG-Mualem'
f.set_model('VG', const=[wrf, 'r=2'])  # Set model and constant parameters
n = 1/(1-wrf[3])
if n < 2:
    f.modified_model(2)
    model = 'Modified VGM'
print(f.model_description)
f.ini = (max(k), 1.5)  # Set initial paramter
f.b_ks = (max(k), max(k)*5)  # Set bound for Ks
f.b_p = (-10, 10)
f.optimize()  # Optimize
if not f.success:
    print(f.message)
    exit(1)
ks, p = f.fitted  # Get result
print('Hydraulic conductivity parameters')
print(f.message)  # Show result
### Save figure ###
f.label_head = 'Matric head (cm)'
f.label_theta = 'Volumetric water content'
f.label_k = 'Hydraulic conductivity (cm/s)'
f.data_legend = 'Silt loam (UNSODA 3393)'
f.line_legend = '{0} p={1:.2f}'.format(model, p)
f.legend_loc = 'center right'
f.save_fig = True
f.filename = FIG
f.plot()
