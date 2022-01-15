# Quick reference

It is all about Fit class of unsatfit.

## Methods

<dl>
<dt>set_model(model, const=[])</dt>
<dd>Set hydraulic model for model with constant parameters of const.</dd>
<dt>optimize()</dt>
<dd>Optimize parameteres.</dd>
<dt>f_ht(p, x)</dt>
<dd>Water retention function with free parameters p and pressure heads x. To be accessed after set_model.</dd>
<dt>f_hk(p, x)</dt>
<dd>Hydraulic conductivity with free parameters p and pressure heads x. To be accessed after set_model.</dd>
<dt>get_init()</dt>
<dd>Get initial estimate of water retention parameters except qs and qr. To be accessed after set_model. See [models](model.md) for function names for each model.</dd>
<dt>get_wrf()</dt>
<dd>Get water retention parameters. To be accessed after set_model. See [models](model.md) for function names for each model.</dd>
<dt>plot()</dt>
<dd>Plot a figure.</dd>
<dt>add_curve()</dt>
<dd>Add a curve for plot.</dd>
<dt>clear_curves()</dt>
<dd>Clear curves.</dd>
<dt>contour(x,y)</dt>
<dd>Draw contour of RMSE for x and y in parameter name.</dd>
<dt>test()</dt>
<dd>Test integrity of the code for development.</dd>
</dl>

## Properties

- For boundary conditions, see __init_bound() in the [source](https://github.com/sekika/unsatfit/blob/main/unsatfit/unsatfit.py).
- For least square optimization, see __init_lsq() in the [source](https://github.com/sekika/unsatfit/blob/main/unsatfit/unsatfit.py).
- For figure options, see  __init_fig() in the [source](https://github.com/sekika/unsatfit/blob/main/unsatfit/unsatfit.py).
