# unsatfit

unsatfit is a Python library for optimizing parameters of functions of soil hydraulic properties (water retention function and hydraulic conductivity function) where equations are explained in the following paper.

* Seki, K., Toride, N., & Th. van Genuchten, M. (2022) [Closed-form hydraulic conductivity equations for multimodal unsaturated soil hydraulic properties.](https://doi.org/10.1002/vzj2.20168) Vadose Zone J. 21; e20168.

The proposed equations are useful for practical applications as shown in the following paper.

* Seki, K., Toride, N., & Th. van Genuchten, M. (2023) [Evaluation of a general model for multimodal unsaturated soil hydraulic properties.](https://doi.org/10.2478/johh-2022-0039) J. Hydrol. Hydromech. 71(1): 22-34.

## User manual

A [user manual](https://doi.org/10.34428/0002000817) is available.

See [install](install.md) and [sample code](code.md) for a quick start.

If you encounter any issues, feel free to ask [questions](feedback.md).

## Example output

This is an example output of this program; water retention curve (top) and hydraulic conductivity curve (bottom) of Gilat loam fitted with KBC (KO<sub>1</sub>BC<sub>2</sub>-CH) model.

![KBC](sample/KBC.png "KBC")

For more examples, see Fig. 6 and Appendix in Seki et al. ([2023](http://www.uh.sav.sk/Portals/16/vcpdf.asp?ID=2081&Article=2023_71_1_Seki_22.pdf)).

## History

- 2006-07-28: Created SWRC Fit 1.0 ([土壌の物理性](https://js-soilphysics.com/downloads/pdf/105067.pdf) version). See [History](https://github.com/sekika/swrcfit/blob/master/ChangeLog) and [source code](https://github.com/sekika/swrcfit/tree/master/archive) of the Octave version.
- 2007-02-27: Released SWRC Fit 1.1 ([HESSD](http://dx.doi.org/10.5194/hessd-4-407-2007) version) and the launched the web version.
- 2016-09-10: Released [SWRC Fit 3.0](https://github.com/sekika/swrcfit/releases/tag/v3.0); implemented the FX model was at the request of a geotechnical engineer.
- 2016-09-15: Presented SWRC Fit at the Japanese society meeting [地盤工学研究発表会](https://researchmap.jp/sekik/presentations/14140472/attachment_file.pdf).
- 2018-09-27: Released [SWRC Fit 3.1](https://github.com/sekika/swrcfit/releases/tag/v3.1) (final Octave version).
- 2021-08-13: SWRC Fit was recommended at [土壌の物理性](https://doi.org/10.34467/jssoilphysics.148.0_45).
- 2021-11-24: A [paper](https://doi.org/10.1002/vzj2.20168) written with unsatfit was published at VZJ.
- 2022-01-04: Relased unsatfit 4.0, including a new version of SWRC Fit.
- 2022-10-29: Presented at the Japanese society of Soil Physics meeting [土壌物理学会](https://sekika.github.io/toyo/abs/jssp2022.html).
- 2023-02-04: A [paper](https://doi.org/10.2478/johh-2022-0039) introducing unsatfit was published in JHH.
- 2023-08-30: Presented improvements to dual-VG fitting at the JSIDRE meeting [農業農村工学会](https://researchmap.jp/sekik/presentations/43218823/attachment_file.pdf).
- 2023-12-21: Improvements to dual-VG fitting were published on [土壌の物理性](https://doi.org/10.34467/jssoilphysics.155.0_35) in Japanese.
- 2024-03-13: The [user manual for SWRC Fit and unsatfit](https://doi.org/10.34428/0002000817) was published in JTUNS.
- 2024-05-14: [hystfit](https://sekika.github.io/hystfit/), a tool for calculating SWRC hysteresis, was released.
- 2024-06-04: Released unsatfit 5.2; SWRC Fit now includes output options for parameter uncertainty, added at the [user's request](https://github.com/sekika/unsatfit/discussions/6).
- 2024-10-20: Received the **JSSP award** ([土壌物理学会賞](https://js-soilphysics.com/prz)) from the Japanese Society of Soil Physics for the [paper of dual-VG fitting](https://doi.org/10.34467/jssoilphysics.155.0_35).
- 2024-11-13: Presented a [poster](https://researchmap.jp/sekik/presentations/48434771/attachment_file.pdf) on hysteresis and [hystfit](https://sekika.github.io/hystfit/) at [ASA, CSSA, SSSA meeting](https://researchmap.jp/sekik/presentations/48434771); took a [photo with Rien van Genuchten](https://sekika.github.io/toyo/photos/RVG.html).
- 2025-03-11: Provided [sample code for drawing water retention curves](code-wrc.md) after [discussion](https://github.com/sekika/unsatfit/discussions/8).
- 2025-03-29: Released unsatfit 5.3; at [user's request](https://github.com/sekika/unsatfit/discussions/9), initialization functions (get_init and get_wrf) are now available for all [models](model.md). Expanded [WRF Sample codes](code-wrc.md).
- 2025-05-08: [Presented](https://researchmap.jp/sekik/presentations/50028303) on multimodal soil hydraulic models and unsatfit at Rien van Genuchten conference.
- 2025-08-13: Released [unsatfit 5.4](https://pypi.org/project/unsatfit/#history) ([update](https://github.com/sekika/unsatfit/commits/main/unsatfit)); added functions for [pore-size distribution](reference.md#pore-size-distribution) analysis.
- 2025-08-13: Released [pdfgridcat](https://pypi.org/project/pdfgridcat/), a tool for arranging multiple figures like [this](https://sekika.github.io/unsatfit/sample-wrc/pdf/unsoda-dual.pdf).

[Update of this document](https://github.com/sekika/unsatfit/commits/main/docs)
