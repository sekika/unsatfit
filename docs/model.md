# Hydraulic models in unsatfit

See also [this paper](https://doi.org/10.1002/vzj2.20168) and [models in SWRC Fit](https://seki.webmasters.gr.jp/swrc/model.html). WRF = water retention function, HCF = hydraulic conductivity function, CH = common H.

## Basic unimodal models

### Brooks and Corey (BC) model
- Name: bc, BC
- WRF parameters: qs, qr, hb, l
- get_init() = get_init_bc(): returns hb, l
- get_wrf() = get_wrf_bc(): returns full WRF parameters
- HCF: Generalized mualem model
- Paramters which only appears in HCF: ks, p, q, r

### van Genuchten (VG) model
- Name: vg, VG
- WRF parameters: qs, qr, a, m, q
- Converted parameter: m = q/(n-1) i.e. n = 1-q/m
- get_init() = get_init_vg(): returns a, m where q=1
- get_wrf() = get_wrf_vg(): returns full WRF parameters where q=1
- HCF: Generalized mualem model
- Paramters which only appears in HCF: ks, p, r

### Kosugi (KO) model
- Name: ln, KO
- WRF parameters: qs, qr, hm, sigma
- get_init() = get_init_ln(): returns hm, sigma
- get_wrf() = get_wrf_ln(): returns full WRF parameters
- HCF: Generalized mualem model
- Paramters which only appears in HCF: ks, p, q, r

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
- Paramters which only appears in HCF: ks, p, q, r

#### dual-BC-CH model
- Name: bc2, DBCH, dual-BC-CH
- WRF parameters: qs, qr, hb, hc, l1, l2
- Converted parameter: w1 = 1/(1+(hc/hb)^(l2-l1))
- get_init() = get_init_bc2(): returns hb, hc, l1, l2
- get_wrf() = not provided
- HCF: Generalized mualem model
- Paramters which only appears in HCF: ks, p, q, r

