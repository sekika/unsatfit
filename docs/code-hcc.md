# Sample code for optimizing WRF and HCF

Easiest way to start learning how to use unsatfit is to run sample codes as instructed in this page. You can optimize parameters of WRF (water retention function) and HCF (hydraulic conductivity function) of [various available models](model.md) to measured data set. You can test with sample data provided in this page. For optimizing only WRF parameters, please refer to [this page](code-wrc.md).

**List of sample codes**

* Models
    * [VGM (van Genuchten - Mualem) model](#vgm-van-genuchten---mualem-model) with full instruction
    * [Bimodal model with general HCF](#bimodal-model-with-general-hcf)
        * [KBC (KO<sub>1</sub>BC<sub>2</sub>-CH) model](#kbc-ko1bc2-ch-model-θr0-r1)
        * [DVC (dual-VG-CH) model](#dvc-dual-vg-ch-model-θr0-q1)
        * [DBC (dual-BC-CH) model](#dbc-dual-bc-ch-model-θr0-r1)
    * [Peters model](#peters-model-θr0)
* [Multiple curves](#multiple-curves)
* [Contour plot](#contour-plot)

## VGM (van Genuchten - Mualem) model
{% raw %}
$$\begin{cases}
\theta(h) &=& (\theta_s - \theta_r)S(h) + \theta_r\\
K(h) &=& K_s {S(h)}^p \bigl[1-(1-S(h)^{1/m})^m\bigr]^2\\
\end{cases}$$

where

$$\begin{eqnarray}
S(h) &=& \biggl[\dfrac{1}{1+(ah)^n}\biggr]^m\\
m &=& 1-1/n
\end{eqnarray}
$$
{% endraw %}
- [Install Python 3 and unsatfit](install.md). Install [pandas](https://pypi.org/project/pandas/) by `python -m pip install pandas`.
- Prepare datafile as csv (comma-separated values) format for (h, &theta;) data in the filename “swrc.csv” with a header of “h, theta”. See [sample data of clay (Unsoda 2362)](https://raw.githubusercontent.com/sekika/unsatfit/main/docs/sample/clay2362/swrc.csv).
- Prepare (h, K) data in the filename “hcc.csv” with a header of “h, K”. See [sample (h, K) data of clay (Unsoda 2362)](https://raw.githubusercontent.com/sekika/unsatfit/main/docs/sample/clay2362/hcc.csv).
- Download a [sample code for VGM model](https://github.com/sekika/unsatfit/blob/main/docs/sample/VGM.py).
- Read the sample code and edit initial parameters, bound of parameters and figure setting as written in the comment of the sample code if necessary. For more figure options, see [source code of unsatfit](https://github.com/sekika/unsatfit/blob/main/unsatfit/_init_fig.py).
- Run the sample code at the same directory with data files (swrc.csv and hcc.csv). For running the code on Mac or unix-like system, edit the first line ([shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))) and mark the file executable by <code>chmod +x VGM.py</code>. For running on Windows, please refer to [Python on Windows FAQ](https://docs.python.org/3/faq/windows.html).
- It first optimizes WRF parameters (&theta;<sub>s</sub>, &theta;<sub>r</sub>, a, n) of VG model, and then optimizes HCF parameters (K<sub>s</sub>, p) of VG Mualem model, or modified VG model (h<sub>b</sub>=2) [Vogel et al. (2000)](https://doi.org/10.1016/S0309-1708(00)00037-3) when n &gt; 1.1. h<sub>b</sub> value can be changed as HB value in the sample code.
- Fitted parameters are shown at the standard output, where qs and qr means &theta;<sub>s</sub> and &theta;<sub>r</sub> respectively, and R2 q means R<sup>2</sup> for &theta; of water retention curve and R2 logK means R<sup>2</sup> for log(K) of hydraulic conductivity curve.
- Note that the program is unit independent, meaning that the unit of the parameters depends on the unit of the input data. Unit of pressure head is assumed as cm for a (cm<sup>-1</sup>) and h<sub>b</sub>.
- Figure file is produced as VG.png. For use in papers, pdf file can be produced as instructed in the sample code.
- See [Reading data from Excel](excel.md) if you wish.

Result with [sample data of clay (Unsoda 2362)](https://github.com/sekika/unsatfit/tree/main/docs/sample/clay2362) is shown below.

<img src="sample/VG-2362.png" width="300" />

Result with [sample data of Gilat loam](https://github.com/sekika/unsatfit/tree/main/docs/sample/gilat) is shown below. In this case, bimodal model is appropriate, as shown below.

<img src="sample/VG-gilat.png" width="300" />

## Bimodal model with general HCF

[Bimodal model](https://seki.webmasters.gr.jp/swrc/model.html) with [general HCF](hcmodel.md) (Seki et al., [2022](https://doi.org/10.1002/vzj2.20168)) can represent water retention and hydraulic  conductivity of various types of soil in a wide range of pressure head, as verified in Seki et al., [2023](https://doi.org/10.2478/johh-2022-0039). You can conduct the same fitting as written in the paper by using the following sample codes.

## KBC (KO<sub>1</sub>BC<sub>2</sub>-CH) model (&theta;<sub>r</sub>=0, r=1)
{% raw %}
$$\begin{cases}
\theta(h) &=& \theta_s S(h)\\
K(h) &=& K_s {S(h)}^p \gamma^{-1} \Biggl[ b_1 Q \biggl[\dfrac{\ln(h/H)}{\sigma_1} + q\sigma_1\biggr]+ b_2 (h/H)^{-\lambda_2 - q} \Biggr]
\end{cases}$$

where

$$\begin{eqnarray}
S(h) &=& \begin{cases}w S_1(h) + (1-w)\left(h/H\right)^{-\lambda_2}  & (h>H)\\
w S_1(h) + 1-w & (h \le H)\end{cases}\\
S_1(h) &=& Q \biggl[\dfrac{\ln(h/H)}{\sigma_1}\biggr]\\
Q(x) &=& \frac{1-\mathrm{erf}(x/\sqrt{2})}{2}\\
b_1 &=& w \exp\biggl(\frac{q^2 \sigma_1^2}{2}\biggr)\\
b_2 &=& (1-w)\biggl(\frac{q}{\lambda_2} + 1\biggr)^{-1}\\
\gamma &=& b_1+b_2
\end{eqnarray}
$$
{% endraw %}
- Use [sample code for KBC model](https://github.com/sekika/unsatfit/blob/main/docs/sample/KBC.py). See instruction in the VGM model above.
- It first optimizes WRF parameters (&theta;<sub>s</sub>, w, H, &sigma;<sub>1</sub>, &lambda;<sub>2</sub>) of KBC model (&theta;<sub>r</sub>=0), and then optimizes general HCF parameters (K<sub>s</sub>, p, q) of KBC model (r=1), or modified KBC model (h<sub>b</sub>=2, r=1) when &sigma;<sub>1</sub> &gt; 2.
- Result with [sample data of Gilat loam](https://github.com/sekika/unsatfit/tree/main/docs/sample/gilat) is shown below.

<img src="sample/KBC.png" width="300" />

## DVC (dual-VG-CH) model (&theta;<sub>r</sub>=0, q=1)
{% raw %}
$$\begin{cases}
\theta(h) &=& \theta_s S(h)\\
K(h) &=& K_s {S(h)}^p \bigl[w\Gamma_1(h) + (1-w)\Gamma_2(h)\bigr]^r\\
\end{cases}$$

where

$$\begin{eqnarray}
S(h) &=& w\bigl[1+(ah)^{n_1}\bigr]^{-m_1} + (1-w)\bigl[1+(ah)^{n_2}\bigr]^{-m_2}\\
m_i&=&1-1/{n_i}\\
\Gamma_i(h) &=& 1-\biggl[1-\big[1+(ah)^{n_i}\bigr]^{-1}\biggr]^{m_i}
\end{eqnarray}
$$
{% endraw %}
- Use [sample code for DVC model](https://github.com/sekika/unsatfit/blob/main/docs/sample/DVC.py). See instruction in the VGM model above.
- It optimizes WRF parameters (&theta;<sub>s</sub>, w, a, n<sub>1</sub>, n<sub>2</sub>)  , and then optimizes general HCF parameters (K<sub>s</sub>, p, r) of DVC model or modified DVC model (h<sub>b</sub>=2) when n<sub>1</sub> or n<sub>2</sub> is smaller than 1.1.
- Result with [sample data of Gilat loam](https://github.com/sekika/unsatfit/tree/main/docs/sample/gilat) is shown below.

<img src="sample/DVC.png" width="300" />

## DBC (dual-BC-CH) model (&theta;<sub>r</sub>=0, r=1)
{% raw %}
$$\begin{eqnarray}
\theta(h) &=& \theta_s S(h)\\
K(h) &=& \begin{cases}K_s {S(h)}^p \gamma^{-1} \bigl[ wB_1 \Gamma_1(h) + (1-w)B_2 \Gamma_2(h) \bigr] & (h>H)\\ K_s & (h \le H)\end{cases}\\
\end{eqnarray}$$

where

$$\begin{eqnarray}
S(h) &=& \begin{cases}w \left(h / H\right)^{-\lambda_1} + (1-w)\left(h / H\right)^{-\lambda_2}  & (h>H)\\ 1 & (h \le H)\end{cases}\\
B_i &=& \biggl(\frac{q}{\lambda_i} + 1\biggr)^{-1}\\
\gamma &=& wB_1+(1-w)B_2\\
\Gamma_i(h) &=& \left(h / H\right)^{-\lambda_i-q}
\end{eqnarray}
$$
{% endraw %}
- Use [sample code for DBC model](https://github.com/sekika/unsatfit/blob/main/docs/sample/DBC.py). See instruction in the VGM model above.
- It optimizes WRF parameters (&theta;<sub>s</sub>, w, &lambda;<sub>1</sub>, &lambda;<sub>2</sub>), and then optimizes general HCF parameters (K<sub>s</sub>, p, q) of DBC model.
- Result with [sample data of Gilat loam](https://github.com/sekika/unsatfit/tree/main/docs/sample/gilat) is shown below.

<img src="sample/DBC.png" width="300" />

# Peters model (&theta;<sub>r</sub>=0)
{% raw %}
$$\begin{cases}
\theta(h) &=& \theta_s S(h)\\
K(h) &=& K_s \bigl[ (1-\omega)K_1(h)+\omega K_2(h) \bigr]\\
\end{cases}$$

where

$$\begin{eqnarray}
S(h) &=& w S_1(h) + (1-w)S_2(h)\\
S_1(h) &=& Q \biggl[\dfrac{\ln(h/H)}{\sigma}\biggr]\\
Q(x) &=& \frac{1-\mathrm{erf}(x/\sqrt{2})}{2}\\
S_2(h) &=& \begin{cases}\dfrac{L(h_0)-L(h)}{L(h_0)-L(H)}  & (h>H)\\
1 & (h \le H)\end{cases}\\
L(h) &=& \ln(1+h/H)\\
K_1(h) &=& {S_1(h)}^p \Biggl[ Q \biggl[\dfrac{\ln(h/H)}{\sigma} + \sigma \biggr] \Biggr]^2\\
K_2(h) &=& \begin{cases}(h/H)^a  & (h>H)\\
1 & (h \le H)\end{cases}\\
\end{eqnarray}
$$
{% endraw %}
- Use [sample code for Peters model](https://github.com/sekika/unsatfit/blob/main/docs/sample/PE.py). See instruction in the VGM model above.
- h<sub>0</sub>=6.3&times;10<sup>6</sup> is constant and can be edited as H0 value in the sample code.
- It optimizes WRF parameters (&theta;<sub>s</sub>, w, H, &sigma;), and then optimizes general HCF parameters (K<sub>s</sub>, p, a, &omega;) of Peters model or modified Peters model (h<sub>b</sub>=2) when &sigma; &gt; 2.
- Result with [sample data of Gilat loam](https://github.com/sekika/unsatfit/tree/main/docs/sample/gilat) is shown below.

<img src="sample/PE.png" width="300" />

## Multiple curves
- Use [sample code for multiple curves](https://github.com/sekika/unsatfit/blob/main/docs/sample/multi.py). See instruction in the VGM model above.
- Draw DBC, DVC, KBC and Peters model in the same figure.
- Result with [sample data of Gilat loam](https://github.com/sekika/unsatfit/tree/main/docs/sample/gilat) is shown below.

<img src="sample/multi.png" width="300" />

## Contour plot
- Use [sample code for contour plot](https://github.com/sekika/unsatfit/blob/main/docs/sample/contour.py). See instruction in the VGM model above.
- It draws a contour plot of (p, q) for RMSE of estimated log<sub>10</sub>(K) for KBC (r=1) optimization.
- Result with [sample data of Gilat loam](https://github.com/sekika/unsatfit/tree/main/docs/sample/gilat) is shown below.

![contour](sample/contour.png "contour")

## Isothermal vapor conductivity
- Use [sample code for multiple curves with vapor condictivity](https://github.com/sekika/unsatfit/blob/main/docs/sample/multi-v.py). It sets some converting parameters of units and temperature. Please read the source code.
- Result with [sample data of Gilat loam](https://github.com/sekika/unsatfit/tree/main/docs/sample/gilat) is shown below.

<img src="sample/multi-v.png" width="300" />

## Trimodal models
These samples codes use same models and fitting setup as in Figure 1 of Seki et al. ([2026](https://researchmap.jp/sekik/published_papers/51967432/attachment_file.pdf)). Constant parameters (e.g., Ks = 3.29 cm / day for the IL sandstone in Figure 1) and unit-conversion parameters for isothermal vapor hydraulic conductivity are provided in the source.

- [tri-VG model](https://github.com/sekika/unsatfit/blob/main/docs/sample/tri-VG.py)
- [BVV model](https://github.com/sekika/unsatfit/blob/main/docs/sample/BVV.py)
- [VVP model](https://github.com/sekika/unsatfit/blob/main/docs/sample/VVP.py)
- [dual-VG and trimodal models](https://github.com/sekika/unsatfit/blob/main/docs/sample/trimodal.py)

Result for the last code with [IL sandstone](https://github.com/sekika/unsatfit/tree/main/docs/sample/IL) is shown.

<img src="sample/trimodal.png" width="300" />
