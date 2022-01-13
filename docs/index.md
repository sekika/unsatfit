# unsatfit

unsatfit is a Python library for optimizing parameters of functions of soil hydraulic properties (water retention function and unsaturated hydraulic conductivity function). It was developed to write the following paper, and unsatfit determined the parameters of hydraulic properties and drew figures in this paper.

Seki, K., Toride, N., & Th. van Genuchten, M. (2021) [Closed-form hydraulic conductivity equations for multimodal unsaturated soil hydraulic properties.](https://doi.org/10.1002/vzj2.20168) Vadose Zone J. 2021; e20168.

## Install

```
python3 -m pip install unsatfit
```

[PyPI Project page](https://pypi.org/project/unsatfit/)

## Sample code

Put [water retention curve](https://github.com/sekika/unsatfit/blob/main/docs/sample/ht3393.csv) and [unsaturated hydraulic conductivity curve](https://github.com/sekika/unsatfit/blob/main/docs/sample/hk3393.csv) of UNSODA 3393 in the same directory as [this sample code](https://github.com/sekika/unsatfit/blob/main/docs/sample/VG-Mualem.py) and run it with Python 3. You get the optimized parameters for VG-Mualem equation as

    Water retention parameters with m=1-1/n (q=1)
    qs = 0.355 qr = 0.000 a = 0.00531 m = 0.107
    Hydraulic conductivity parameters
    Ks = 8.88e-01 p = 0.895 r = 1.447 R2 q = 0.992 R2 logK = 0.973

where qs and qr means &theta;<sub>s</sub> and &theta;<sub>r</sub> respectively, and R2 q means R<sup>2</sup> for &theta; of water retention curve and R2 logK means R<sup>2</sup> for log(K) of hydraulic conductivity curve. Following figure is produced.

![VG-Mualem](sample/VG-Mualem.png "VG-Mualem")

## SWRC Fit

SWRC Fit is a web interface which uses unsatfit and determines parameters for water retention function. Source code is in the [repository](https://github.com/sekika/unsatfit/tree/main/swrcfit).

- [SWRC Fit](https://seki.webmasters.gr.jp/swrc/)

[GNU Octave version of SWRC Fit](https://github.com/sekika/swrcfit/blob/master/doc/en/README.md) is no longer maintained but the code is available.

## About unsatfit
* Author: [Katsutoshi Seki](https://scholar.google.com/citations?user=Gs_ABawAAAAJ)
* License: MIT License
