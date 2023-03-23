# Reference

It is all about Fit class of unsatfit.

## Methods

For optimization.
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
<dd>Get initial estimate of water retention parameters except qs and qr. To be accessed after set_model. See <a href="model.html">models</a> for function names by specifying a model.</dd>
<dt>get_wrf()</dt>
<dd>Get water retention parameters. To be accessed after set_model. See <a href="model.html">models</a> for function names by specifying a model.</dd>
<dt>modified_model(hs)</dt>
<dd>Change the hydraulic model to modified model with hs value by <a href="https://doi.org/10.1016/S0309-1708(00)00037-3)">Vogel et al. (2000)</a>.</dd>
</dl>

For figures etc.
<dl>
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

## Properties for settings

<dl>
<dt>swrc</dt>
<dd>(h, &theta;) dataset; h and &theta; as list respectively</dd>
<dt>unsat</dt>
<dd>(h, K) dataset (optimize only WRF when empty list [] is provided)</dd>
<dt>ini</dt>
<dd>Initial parameters. When it is a list (or tuple) of parameters, such as [a, b, c], the set of parameters is used as initial parameters. When it is a nested list, such as [[a1, a2, a3], [b1, b2]], all combination of the initial parameters is used.</dd>
</dl>

- For boundary conditions, see [source](https://github.com/sekika/unsatfit/blob/main/unsatfit/_init_bound.py).
- For least square optimization, see [source](https://github.com/sekika/unsatfit/blob/main/unsatfit/_init_lsq.py).
- For figure options, see [source](https://github.com/sekika/unsatfit/blob/main/unsatfit/_init_fig.py).

## Properties for return values of optimize()

<dl>
<dt>fitted</dt>
<dd>Fitted parameters</dd>
<dt>message</dt>
<dd>Return message</dd>
<dt>success</dt>
<dd>True if optimization succeeded</dd>
<dt>mse_ht, mse_ln_hk</dt>
<dd>Mean squared error for &theta; and ln(K), respectively</dd>
<dt>se_ht, se_ln_hk</dt>
<dd>Standard error &sigma; for &theta; and ln(K), respectively</dd>
<dt>r2_ht, r2_ln_hk</dt>
<dd>Coefficient of determination (R<sup>2</sup>) for &theta; and ln(K), respectively</dd>
<dt>aic_ht, aic_ln_hk</dt>
<dd>AIC = 2n ln(&sigma;) + 2k for &theta; and ln(K), respectively</dd>
<dt>aicc_ht, aicc_ln_hk</dt>
<dd>Corrected AIC = AIC + 2k(k+1)/(n-k-1) for &theta; and ln(K), respectively</dd>
</dl>
