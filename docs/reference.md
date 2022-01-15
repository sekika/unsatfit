# Quick reference

It is all about Fit class of unsatfit.

## Methods

<dl>
<dt>set_model(model, const=[])
<dd>Set hydraulic model for model with constant parameters of const.
<dt>optimize()
<dd>Optimize parameteres.
<dt>f_ht(p, x)
<dd>Water retention function with free parameters p and pressure heads x. To be accessed after set_model.
<dt>f_hk(p, x)
<dd>Hydraulic conductivity with free parameters p and pressure heads x. To be accessed after set_model.
<dt>get_init()
<dd>Get initial estimate of water retention parameters except qs and qr. To be accessed after set_model. See [models](model.md) for function names for each model.
<dt>get_wrf()
<dd>Get water retention parameters. To be accessed after set_model. See [models](model.md) for function names for each model.
<dt>plot()
<dd>Plot a figure.
<dt>add_curve()
<dd>Add a curve for plot.
<dt>clear_curves()
<dd>Clear curves.
<dt>contour(x,y)
<dd>Draw contour of RMSE for x and y in parameter name.
<dt>test()
<dd>Test integrity of the code for development.
</dl>

## Properties

* For boundary conditions, see __init_bound() in the [source](https://github.com/sekika/unsatfit/blob/main/unsatfit/unsatfit.py).
* For least square optimization, see __init_lsq() in the [source](https://github.com/sekika/unsatfit/blob/main/unsatfit/unsatfit.py).
* For figure options, see  __init_fig() in the [source](https://github.com/sekika/unsatfit/blob/main/unsatfit/unsatfit.py).
