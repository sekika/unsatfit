# Hydraulic models in unsatfit

See also [this paper](https://doi.org/10.1002/vzj2.20168) and [models in SWRC Fit](https://seki.webmasters.gr.jp/swrc/model.html). WRF = water retention function, HCF = hydraulic conductivity function, CH = common H.

## Basic unimodal models

### Brooks and Corey (BC) model
- Name: bc, BC
- WRF parameters: qs, qr, hb, l
- get_init() = get_init_bc(): returns hb, l
- get_wrf() = get_wrf_bc(): returns full WRF parameters
- HCF: Generalized mualem model
- Parameters which only appears in HCF: Ks, p, q, r

### van Genuchten (VG) model
- Name: vg, VG
- WRF parameters: qs, qr, a, m, q
- Converted parameter: n = q/(1-m) i.e. m = 1-q/n
- get_init() = get_init_vg(): returns a, m where q=1
- get_wrf() = get_wrf_vg(): returns full WRF parameters where q=1
- HCF: Generalized mualem model
- Parameters which only appears in HCF: Ks, p, r

### Kosugi (KO) model
- Name: ln, KO
- WRF parameters: qs, qr, hm, sigma
- get_init() = get_init_ln(): returns hm, sigma
- get_wrf() = get_wrf_ln(): returns full WRF parameters
- HCF: Generalized mualem model
- Parameters which only appears in HCF: Ks, p, q, r

### Fredlund und Xing (FX) model
- Name: fx, FX
- WRF parameters: qs, qr, a, m, n
- get_init() = get_init_fx(): returns a, m, n
- HCF: not provided

## Bimodal models

### dual-BC model
- Name: bc2f, DB, dual-BC
- WRF parameters: qs, qr, w1, hb1, l1, hb2, l2
- get_init() = not provided
- get_wrf() = not provided
- HCF: Generalized mualem model
- Parameters which only appears in HCF: Ks, p, q, r

#### dual-BC-CH model
- Name: bc2, DBCH, dual-BC-CH
- WRF parameters: qs, qr, hb, hc, l1, l2
- Converted parameter: w1 = 1/(1+(hc/hb)^(l2-l1))
- get_init() = get_init_bc2(): returns hb, hc, l1, l2
- get_wrf() = not provided
- HCF: Generalized mualem model
- Parameters which only appears in HCF: Ks, p, q, r

### dual-VG model
- Name: vg2, DV, dual-VG
- WRF parameters: qs, qr, w1, a1, m1, a2, m2, q
- Converted parameter: n1 = q/(1-m1), n2 = q/(1-m2)
- get_init() = not provided
- get_wrf() = not provided
- HCF: Generalized mualem model
- Parameters which only appears in HCF: Ks, p, r

#### dual-VG-CH model
- Name: vg2ch, DVCH, dual-VG-CH
- WRF parameters: qs, qr, w1, a1, m1, a2, m2, q
- Converted parameter: n1 = q/(1-m1), n2 = q/(1-m2)
- get_init() = get_init_vg2ch(): returns w1, a1, m1, a2, m2 where q=1
- get_wrf() = not provided
- HCF: Generalized mualem model
- Parameters which only appears in HCF: Ks, p, r

### dual-KO model
- Name: ln2, DK, dual-KO
- WRF parameters: qs, qr, w1, hm1, sigma1, hm2, sigma2
- get_init() = not provided
- get_wrf() = not provided
- HCF: Generalized mualem model
- Parameters which only appears in HCF: Ks, p, q, r

### dual-KO-CH model
- Name: ln2ch, DKCH, dual-KO-CH
- WRF parameters: qs, qr, w1, hm1, sigma1, sigma2
- get_init() = not provided
- get_wrf() = not provided
- HCF: Generalized mualem model
- Parameters which only appears in HCF: Ks, p, q, r

### VG<sub>1</sub>BC</sub>2</sub> model
- Name: vgbc, VGBC, VG1BC2
- WRF parameters: qs, qr, w1, a1, m1, hb2, l2, q
- Converted parameter: n1 = q/(1-m1)
- get_init() = not provided
- get_wrf() = not provided
- HCF: Generalized mualem model
- Parameters which only appears in HCF: Ks, p, r

HCF variation: r=1 and independent p

- Name: vgbcp2, VGBCP2, VG1BC2-p1p2
- Parameters which only appears in HCF: Ks, p1, p2

### VG<sub>1</sub>BC</sub>2</sub>-CH model
- Name: vgbcch, VGBCCH, VG1BC2-CH
- WRF parameters: qs, qr, w1, a1, m1, l2, q
- Converted parameter: n1 = q/(1-m1)
- get_init() = get_init_vgbcch(): returns w1, a1, m1, l2 where q=1
- get_wrf() = not provided
- HCF: Generalized mualem model
- Parameters which only appears in HCF: Ks, p, r

HCF variation: r=1 and independent p

- Name: vgbcchp2, VGBCCHP2, VG1BC2CH-p1p2
- Parameters which only appears in HCF: Ks, p1, p2

### KO<sub>1</sub>BC</sub>2</sub> model
- Name: kobc, KOBC, KO1BC2
- WRF parameters: qs, qr, w1, hm1, sigma1, hb2, l2
- get_init() = not provided
- get_wrf() = get_wrf_kobc(): returns full WRF parameters
- HCF: Generalized mualem model
- Parameters which only appears in HCF: Ks, p, q, r

HCF variation: r=1 and independent p

- Name: kobcp2, KOBCP2, KO1BC2-p1p2
- Parameters which only appears in HCF: Ks, p1, p2, q

### KO<sub>1</sub>BC</sub>2</sub>-CH model
- Name: kobcch, KOBCCH, KO1BC2-CH
- WRF parameters: qs, qr, w1, hm, sigma1, l2
- get_init() = get_init_kobcch(): returns w1, hm, sigma1, l2
- get_wrf() = not provided
- HCF: Generalized mualem model
- Parameters which only appears in HCF: Ks, p, q, r

HCF variation: r=1 and independent p

- Name: kobcch2, KOBCCHP2, KO1BC2-CH-p1p2
- Parameters which only appears in HCF: Ks, p1, p2

## Exponential decrease to zero water content

### Fayer and Simmons model (van Genuchten type)
- Name: vgfs, VGFS, Fayer-VG
- WRF parameters: qs, qr, qa, a, m, he, q
- Converted parameter: n = q/(1-m) i.e. m = 1-q/n
- get_init() = not provided
- get_wrf() = not provided
- HCF: Generalized mualem model
- Parameters which only appears in HCF: Ks, p, r