# unsatfit

unsatfit is a Python library for optimizing parameters of [functions of soil hydraulic properties](https://doi.org/10.1002/vzj2.20168) (water retention function and unsaturated hydraulic conductivity function).

## Install

python3 -m pip install unsatfit

## Sample code

```
f = unsatfit.Fit() # Create instance for fitting
f.set_model('vg', const=[[10, 1]]) # Set model and constant parameters
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

SWRC Fit is a web interface which uses unsatfit and determines parameters for water retention function.

- [SWRC Fit](https://seki.webmasters.gr.jp/swrc/)
