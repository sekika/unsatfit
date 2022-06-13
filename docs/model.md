# Hydraulic models in unsatfit

See also [this paper](https://doi.org/10.1002/vzj2.20168) and [models in SWRC Fit](https://seki.webmasters.gr.jp/swrc/model.html). WRF = water retention function, HCF = hydraulic conductivity function, CH = common H.

## Basic unimodal models

### Brooks and Corey (BC) model
- Brooks and Corey ([1964](https://scholar.google.com/scholar_lookup?hl=en&publication_year=1964&author=R.+H.+Brooks&author=A.+T.+Corey&title=Hydraulic+properties+of+porous+media))
- Name: bc, BC
- WRF parameters: qs, qr, hb, l
- get_init() = get_init_bc(): returns hb, l
- get_wrf() = get_wrf_bc(): returns full WRF parameters
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, q, r

### van Genuchten (VG) model
- van Genuchten ([1980](https://doi.org/10.2136/sssaj1980.03615995004400050002x))
- Name: vg, VG
- WRF parameters: qs, qr, a, m, q
- Converted parameter: n = q/(1-m) i.e. m = 1-q/n
- Note that in unsatfit, m is used as a variable instead of n, because the bound of m, 0&lt;m&lt;1 is easier to handle than the bound of n, n&gt;q, as unsatfit can make q as a variable.
- get_init() = get_init_vg(): returns a, m where q=1
- get_wrf() = get_wrf_vg(): returns full WRF parameters where q=1
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, r

Modified van Genuchten model
- Vogel et al. ([2000](https://doi.org/10.1016/S0309-1708(00)00037-3))
- Name: mvg, MVG, Modified VG
- WRF parameters: qs, qr, a, m, hs, q
- Converted parameter: n = q/(1-m) i.e. m = 1-q/n
- hs = 2 cm for 1&lt;n&lt;2 in Vogel et al., (2000)
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, r

In general, modified model can be made by calling modified_model(hs) after set_model()

### Kosugi (KO) model
- Kosugi ([1996](http://dx.doi.org/10.1029/96WR01776))
- Name: ln, KO
- WRF parameters: qs, qr, hm, sigma
- get_init() = get_init_ln(): returns hm, sigma
- get_wrf() = get_wrf_ln(): returns full WRF parameters
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, q, r

### Fredlund und Xing (FX) model
- Fredlund and Xing ([1994](http://dx.doi.org/10.1139/t94-061))
- Name: fx, FX
- WRF parameters: qs, qr, a, m, n
- get_init() = get_init_fx(): returns a, m, n
- HCF: not provided

## Bimodal models

### dual-BC model
- Seki et al. ([2022](https://doi.org/10.1002/vzj2.20168))
- Name: bc2f, DB, dual-BC
- WRF parameters: qs, qr, w1, hb1, l1, hb2, l2
- get_init() = not provided
- get_wrf() = not provided
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, q, r

#### dual-BC-CH model
- Seki et al. ([2022](https://doi.org/10.1002/vzj2.20168))
- Name: bc2, DBCH, dual-BC-CH
- WRF parameters: qs, qr, hb, hc, l1, l2
- Converted parameter: w1 = 1/(1+(hc/hb)^(l2-l1))
- get_init() = get_init_bc2(): returns hb, hc, l1, l2
- get_wrf() = get_wrf_bc2(): returns full WRF parameters where qr=0
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, q, r

### dual-VG model
- Priesack and Durner ([2006](https://doi.org/10.2136/vzj2005.0066)), equation corrected at Seki et al. ([2022](https://doi.org/10.1002/vzj2.20168))
- Name: vg2, DV, dual-VG
- WRF parameters: qs, qr, w1, a1, m1, a2, m2, q
- Converted parameter: n1 = q/(1-m1), n2 = q/(1-m2)
- get_init() = not provided
- get_wrf() = not provided
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, r

#### dual-VG-CH model
- Priesack and Durner ([2006](https://doi.org/10.2136/vzj2005.0066)), equation corrected at Seki et al. ([2022](https://doi.org/10.1002/vzj2.20168))
- Name: vg2ch, DVCH, dual-VG-CH
- WRF parameters: qs, qr, w1, a1, m1, m2, q
- Converted parameter: n1 = q/(1-m1), n2 = q/(1-m2)
- get_init() = get_init_vg2ch(): returns w1, a1, m1, a2, m2 where q=1
- get_wrf() = get_wrf_vg2ch(): returns full WRF parameters where qr=0, q=1
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, r

### dual-KO model
- Seki et al. ([2022](https://doi.org/10.1002/vzj2.20168))
- Name: ln2, DK, dual-KO
- WRF parameters: qs, qr, w1, hm1, sigma1, hm2, sigma2
- get_init() = not provided
- get_wrf() = not provided
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, q, r

### dual-KO-CH model
- Seki et al. ([2022](https://doi.org/10.1002/vzj2.20168))
- Name: ln2ch, DKCH, dual-KO-CH
- WRF parameters: qs, qr, w1, hm1, sigma1, sigma2
- get_init() = not provided
- get_wrf() = not provided
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, q, r

### VG<sub>1</sub>BC<sub>2</sub> model
- Seki et al. ([2022](https://doi.org/10.1002/vzj2.20168))
- Name: vgbc, VGBC, VG1BC2, VB
- WRF parameters: qs, qr, w1, a1, m1, hb2, l2, q
- Converted parameter: n1 = q/(1-m1)
- get_init() = not provided
- get_wrf() = not provided
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, r

HCF variation: r=1 and independent p

- Name: vgbcp2, VGBCIP, VG1BC2-IP, VB-IP
- Parameters which only appears in HCF: Ks, p1, p2

### VG<sub>1</sub>BC<sub>2</sub>-CH model
- Seki et al. ([2022](https://doi.org/10.1002/vzj2.20168))
- Name: vgbcch, VGBCCH, VG1BC2-CH, VBC
- WRF parameters: qs, qr, w1, a1, m1, l2, q
- Converted parameter: n1 = q/(1-m1)
- get_init() = get_init_vgbcch(): returns w1, a1, m1, l2 where qr=0, q=1
- get_wrf() = not provided
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, r

HCF variation: r=1 and independent p

- Name: vgbcchp2, VGBCCHIP, VG1BC2CH-IP, VBC-IP
- Parameters which only appears in HCF: Ks, p1, p2

### KO<sub>1</sub>BC<sub>2</sub> model
- Seki et al. ([2022](https://doi.org/10.1002/vzj2.20168))
- Name: kobc, KOBC, KO1BC2, KB
- WRF parameters: qs, qr, w1, hm1, sigma1, hb2, l2
- get_init() = not provided
- get_wrf() = get_wrf_kobc(): returns full WRF parameters with qr=0
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, q, r

HCF variation: r=1 and independent p

- Name: kobcp2, KOBCIP, KO1BC2-IP, KB-IP
- Parameters which only appears in HCF: Ks, p1, p2, q

### KO<sub>1</sub>BC<sub>2</sub>-CH model
- Seki et al. ([2022](https://doi.org/10.1002/vzj2.20168))
- Name: kobcch, KOBCCH, KO1BC2-CH, KBC
- WRF parameters: qs, qr, w1, hm, sigma1, l2
- get_init() = get_init_kobcch(): returns w1, hm, sigma1, l2
- get_wrf() = get_wrf_kobcch(): returns full WRF parameters with qr=0
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, q, r

HCF variation: r=1 and independent p

- Name: kobcch2, KOBCCHIP, KO1BC2-CH-IP, KBC-IP
- Parameters which only appears in HCF: Ks, p1, p2, q

## Giving pressure head of zero water content

### Peters model (Kosugi type)
- Peters ([2013](https://doi.org/10.1002/wrcr.20548))
- Name: pk, PK, Peters-KO, PE, Peters
- WRF parameters: qs, qr, w1, hm, sigma1, he
- qr=0 by definition. &theta;=0 at h=he.
- get_init() = get_init_pk(he): w1, hm, sigma1
- get_wrf() = get_wrf_pk(he): returns full WRF parameters with qr=0
- HCF: Peters (2013)
- Parameters which only appears in HCF: Ks, p, a, omega

### Fayer and Simmons model (van Genuchten type)
- Fayer and Simmons ([1995](https://doi.org/10.1029/95WR00173))
- Name: vgfs, VGFS, Fayer-VG
- WRF parameters: qs, qr, qa, a, m, he, q
- qr=0 by definition. &theta;=0 at h=he.
- q = 1 should be provided. Otherwise not calculated.
- Converted parameter: n = q/(1-m) i.e. m = 1-q/n
- get_init() = not provided
- get_wrf() = not provided
- HCF: [General HCF](hcmodel.md)
- Parameters which only appears in HCF: Ks, p, r
