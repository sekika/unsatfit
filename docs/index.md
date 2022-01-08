# unsatfit

unsatfit is a Python library for optimizing parameters of functions of soil hydraulic properties (water retention function and unsaturated hydraulic conductivity function). It was developed to write the following paper, and unsatfit determined the parameters of hydraulic properties and drew figures in this paper.

Seki, K., Toride, N., & Th. van Genuchten, M. (2021) [Closed-form hydraulic conductivity equations for multimodal unsaturated soil hydraulic properties.](https://doi.org/10.1002/vzj2.20168) Vadose Zone J. 2021; e20168.

## Install

```
python3 -m pip install unsatfit
```

[PyPI Project page](https://pypi.org/project/unsatfit/)

## Sample code

```
import unsatfit
f = unsatfit.Fit() # Create instance for fitting
f.set_model('VG', const=[[10, 1]]) # Set model and constant parameters (q=1)
f.swrc = (h, theta) # Data of soil water retention
f.unsat = (h, K) # Data of unsaturated hydraulic conductivity
a, m = f.get_init_vg() # Get initial paramter
f.ini = (max(theta), 0, a, m, max(K), 0.5, 2) # Set initial paramter
f.b_qr = (0, 0.05) # Set lower and upper bound
f.optimize() # Optimize
print(f.fitted) # Show result as an array
print(f.message)  # Show result
f.show_fig = True
f.plot()  # Draw a graph
f.contour('a', 'm')  # Draw contour of RMSE for a and m
```

## SWRC Fit

SWRC Fit is a web interface which uses unsatfit and determines parameters for water retention function. Source code is in the [repository](https://github.com/sekika/unsatfit/tree/main/swrcfit).

- [SWRC Fit](https://seki.webmasters.gr.jp/swrc/)

[GNU Octave version of SWRC Fit](https://github.com/sekika/swrcfit/blob/master/doc/en/README.md) is no longer maintained but the code is available.

## About unsatfit
* Author: [Katsutoshi Seki](https://scholar.google.com/citations?user=Gs_ABawAAAAJ)
* License: MIT License
