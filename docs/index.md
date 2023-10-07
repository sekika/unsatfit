# unsatfit

unsatfit is a Python library for optimizing parameters of functions of soil hydraulic properties (water retention function and hydraulic conductivity function) where equations are explained in the following paper.

* Seki, K., Toride, N., & Th. van Genuchten, M. (2022) [Closed-form hydraulic conductivity equations for multimodal unsaturated soil hydraulic properties.](https://doi.org/10.1002/vzj2.20168) Vadose Zone J. 21; e20168.

The proposed equations are useful for practical applications as shown in the following paper.

* Seki, K., Toride, N., & Th. van Genuchten, M. (2023) [Evaluation of a general model for multimodal unsaturated soil hydraulic properties.](https://doi.org/10.2478/johh-2022-0039) J. Hydrol. Hydromech. 71(1): 22-34.

## User manual

A [user manual](https://arxiv.org/abs/2302.00472) is available.

See [install](install.md) and [sample code](code.md) for a quick start.

## Example output

This is an example output of this program; water retention curve (top) and hydraulic conductivity curve (bottom) of Gilat loam fitted with KBC (KO<sub>1</sub>BC<sub>2</sub>-CH) model.

![KBC](sample/KBC.png "KBC")

For more examples, see Fig. 6 and Appendix in Seki et al. ([2023](http://www.uh.sav.sk/Portals/16/vcpdf.asp?ID=2081&Article=2023_71_1_Seki_22.pdf)).

## History

- 2006-07-28: SWRC Fit 1.0 ([土壌の物理性](https://js-soilphysics.com/downloads/pdf/105067.pdf) version) was created. 
- 2007-02-27: SWRC Fit 1.1 ([HESSD](http://dx.doi.org/10.5194/hessd-4-407-2007) version) was released.
- 2016-09-15: Presented SWRC Fit at Japanese society meeting [地盤工学研究発表会](https://researchmap.jp/sekik/presentations/14140472/attachment_file.pdf).
- 2018-09-27: SWRC Fit 3.1 (last Octave version) was [released](https://github.com/sekika/swrcfit/releases/tag/v3.1). [History of the Octave version](https://github.com/sekika/swrcfit/blob/master/ChangeLog).
- 2021-08-13: SWRC Fit was recommended at [土壌の物理性](https://doi.org/10.34467/jssoilphysics.148.0_45).
- 2021-11-24: [Paper](https://doi.org/10.1002/vzj2.20168) written with unsatfit was published at VZJ.
- 2022-01-04: unsatfit 4.0 was released with new version of SWRC Fit.
- 2022-10-29: Presented at Japanese society meeting [土壌物理学会](https://sekika.github.io/toyo/abs/jssp2022.html).
- 2023-02-02: [User manual](https://arxiv.org/abs/2302.00472) was published on arXiv.
- 2023-02-04: [Paper](https://doi.org/10.2478/johh-2022-0039) introducing unsatfit was published at JHH.
- 2023-08-30: Improvement of dual-VG fitting was presented at Japanese society meeting [農業農村工学会](https://researchmap.jp/sekik/presentations/43218823/attachment_file.pdf).
- 2023-10-07: [unsatfit 5.1](https://pypi.org/project/unsatfit/#history) was released ([update](https://github.com/sekika/unsatfit/commits/main/unsatfit)).

[Update of this document](https://github.com/sekika/unsatfit/commits/main/docs)
