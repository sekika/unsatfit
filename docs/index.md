# unsatfit

unsatfit is a Python library for optimizing parameters of functions of soil hydraulic properties (water retention function and unsaturated hydraulic conductivity function). It was developed to write the following paper, and unsatfit determined the parameters of hydraulic properties and drew figures in this paper.

Seki, K., Toride, N., & Th. van Genuchten, M. (2021) [Closed-form hydraulic conductivity equations for multimodal unsaturated soil hydraulic properties.](https://doi.org/10.1002/vzj2.20168) Vadose Zone J. 2021; e20168.

## Contents

- [Models](model.md)
- [Sample code](code.md)

## Install

```
python3 -m pip install unsatfit
```

[PyPI Project page](https://pypi.org/project/unsatfit/)

## SWRC Fit

SWRC Fit is a web interface which uses unsatfit and determines parameters for water retention function. Source code is in the [repository](https://github.com/sekika/unsatfit/tree/main/swrcfit).

- [SWRC Fit](https://seki.webmasters.gr.jp/swrc/)

[GNU Octave version of SWRC Fit](https://github.com/sekika/swrcfit/blob/master/doc/en/README.md) is no longer maintained but the code is available.

## About unsatfit
* Author: [Katsutoshi Seki](https://scholar.google.com/citations?user=Gs_ABawAAAAJ)
* License: MIT License
