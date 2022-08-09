# Sample code of unsatfit

Easiest way to start learning how to use unsatfit is to run sample codes as instructed in this page. You can optimize parameters of WRF (water retention function) and HCF (hydraulic conductivity function) of [various available models](model.md) to measured data set. You can test with sample data provided. If you study Python and read the sample code, you will be able to use unsatfit flexibly according to your demand. For optimizing only WRF parameters, please use [SWRC Fit](swrcfit.md).

## <strong>VGM</strong> (van Genuchten - Mualem) model
- [Install Python 3 and unsatfit](install.md). Install [pandas](https://pypi.org/project/pandas/) by `python -m pip install pandas`.
- Prepare datafile as csv (comma-separated values) format for (h, &theta;) data in the filename “swrc.csv” with a header of “h, theta”. See [sample data of clay (Unsoda 2362)](https://raw.githubusercontent.com/sekika/unsatfit/main/docs/sample/clay2362/swrc.csv).
- Prepare (h, K) data in the filename “hcc.csv” with a header of “h, K”. See [sample (h, K) data of clay (Unsoda 2362)](https://raw.githubusercontent.com/sekika/unsatfit/main/docs/sample/clay2362/hcc.csv).
- Download a [sample code for VGM model](https://github.com/sekika/unsatfit/blob/main/docs/sample/VGM.py).
- Read the sample code and edit initial parameters, bound of parameters and figure setting as written in the comment of the sample code if necessary. For more figure options, see  __init_fig() function in the [source code of unsatfit](https://github.com/sekika/unsatfit/blob/main/unsatfit/unsatfit.py).
- Run the sample code at the same directory with data files (swrc.csv and hcc.csv). For running the code on Mac or unix-like system, edit the first line ([shebang](https://en.wikipedia.org/wiki/Shebang_(Unix))) and mark the file executable by <code>chmod +x VGM.py</code>. For running on Windows, please refer to [Python on Windows FAQ](https://docs.python.org/3/faq/windows.html).
- It first optimizes WRF parameters (&theta;<sub>s</sub>, &theta;<sub>r</sub>, a, n) of VG model, and then optimizes HCF parameters (K<sub>s</sub>, p) of VG Mualem model, or modified VG model (h<sub>b</sub>=2) [Vogel et al. (2000)](https://doi.org/10.1016/S0309-1708(00)00037-3) when n &gt; 1.1.
- Fitted parameters are shown at the standard output, where qs and qr means &theta;<sub>s</sub> and &theta;<sub>r</sub> respectively, and R2 q means R<sup>2</sup> for &theta; of water retention curve and R2 logK means R<sup>2</sup> for log(K) of hydraulic conductivity curve. Note that the program is unit independent, meaning that the unit of the parameters depends on the unit of the input data. Unit of pressure head is assumed as cm for a (cm<sup>-1</sup>) and h<sub>b</sub>.
- Figure file is produced as VG.png. For use in papers, pdf file can be produced as instructed in the sample code.

Result with [sample data of clay (Unsoda 2362)](https://github.com/sekika/unsatfit/tree/main/docs/sample/clay2362) is shown below.

<img src="sample/VG-2362.png" width="300" />

Result with [sample data of Gilat loam](https://github.com/sekika/unsatfit/tree/main/docs/sample/gilat) is shown below. In this case, bimodal model is appropriate, as shown below.

<img src="sample/VG-gilat.png" width="300" />

## Bimodal model with general HCF

[Bimodal model](https://seki.webmasters.gr.jp/swrc/model.html) with [general HCF](hcmodel.md) (Seki et al., [2022](https://doi.org/10.1002/vzj2.20168)) can represent water retention and hydraulic  conductivity of various types of soil in a wide range of pressure head, as verified in our paper which is in review process. You can conduct the same fitting as written in the paper by using the following sample codes.

## <strong>KBC</strong> (<strong>KO<sub>1</sub>BC<sub>2</sub>-CH</strong>) model (&theta;<sub>r</sub>=0, r=1)
- Use [sample code for KBC model](https://github.com/sekika/unsatfit/blob/main/docs/sample/KBC.py). See instruction in the VGM model above.
- It first optimizes WRF parameters (&theta;<sub>s</sub>, w, H, &sigma;<sub>1</sub>, &lambda;<sub>2</sub>) of KBC model (&theta;<sub>r</sub>=0), and then optimizes general HCF parameters (K<sub>s</sub>, p, q) of KBC model (r=1), or modified KBC model (h<sub>b</sub>=2, r=1) when &sigma;<sub>1</sub> &gt; 2.
- Result with [sample data of Gilat loam](https://github.com/sekika/unsatfit/tree/main/docs/sample/gilat) is shown below.

<img src="sample/KBC.png" width="300" />

## <strong>DVC</strong> (<strong>dual-VG-CH</strong>) model (&theta;<sub>r</sub>=0, q=1)
- Use [sample code for DVC model](https://github.com/sekika/unsatfit/blob/main/docs/sample/DVC.py). See instruction in the VGM model above.
- It optimizes WRF parameters (&theta;<sub>s</sub>, w, a, n<sub>1</sub>, n<sub>2</sub>)  , and then optimizes general HCF parameters (K<sub>s</sub>, p, r) of DVC model or modified DVC model (h<sub>b</sub>=2) when n<sub>1</sub> or n<sub>2</sub> is smaller than 1.1.
- Result with [sample data of Gilat loam](https://github.com/sekika/unsatfit/tree/main/docs/sample/gilat) is shown below.

<img src="sample/DVC.png" width="300" />

## <strong>DBC</strong> (<strong>dual-BC-CH</strong>) model (&theta;<sub>r</sub>=0, r=1)
- Use [sample code for DBC model](https://github.com/sekika/unsatfit/blob/main/docs/sample/DBC.py). See instruction in the VGM model above.
- It optimizes WRF parameters (&theta;<sub>s</sub>, w, &lambda;<sub>1</sub>, &lambda;<sub>2</sub>), and then optimizes general HCF parameters (K<sub>s</sub>, p, q) of DBC model.
- Result with [sample data of Gilat loam](https://github.com/sekika/unsatfit/tree/main/docs/sample/gilat) is shown below.

<img src="sample/DBC.png" width="300" />

## <strong>Peters</strong> model (&theta;<sub>r</sub>=0, h<sub>0</sub>=6.3&times;10<sup>6</sup>)
- Use [sample code for Peters model](https://github.com/sekika/unsatfit/blob/main/docs/sample/PE.py). See instruction in the VGM model above.
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
