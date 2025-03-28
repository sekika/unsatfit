# unsatfit

unsatfit is a Python library for optimizing parameters of functions related to soil hydraulic properties, specifically the water retention function and the unsaturated hydraulic conductivity function. The equations are explained in Seki et al. (2022) and demonstrated to be useful for practical applications in Seki et al. (2023).

## Document

For the full documentation, visit https://doi.org/10.34428/0002000817

For quick references and sample codes, visit https://sekika.github.io/unsatfit/

## Example output

This is an example output of this program: the water retention curve (top) and hydraulic conductivity curve (bottom) of Gilat loam, fitted with the KBC (KO<sub>1</sub>BC<sub>2</sub>-CH) model.

![KBC](https://sekika.github.io/unsatfit/sample/KBC.png "KBC")

## SWRC Fit

SWRC Fit is a web interface which uses unsatfit to determine parameters for water retention function.

- [SWRC Fit](https://seki.webmasters.gr.jp/swrc/)

## Reference

* Seki, K., Toride, N., & Th. van Genuchten, M. (2022) Closed-form hydraulic conductivity equations for multimodal unsaturated soil hydraulic properties. Vadose Zone J. 21; e20168. https://doi.org/10.1002/vzj2.20168
* Seki, K., Toride, N., & Th. van Genuchten, M. (2023) Evaluation of a general model for multimodal unsaturated soil hydraulic properties. J. Hydrol. Hydromech. 71(1): 22-34. https://doi.org/10.2478/johh-2022-0039
