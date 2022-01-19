# Sample code of unsatfit

Put [water retention curve](https://github.com/sekika/unsatfit/blob/main/docs/sample/ht3393.csv) and [unsaturated hydraulic conductivity curve](https://github.com/sekika/unsatfit/blob/main/docs/sample/hk3393.csv) of UNSODA 3393 in the same directory as [this sample code](https://github.com/sekika/unsatfit/blob/main/docs/sample/VG-Mualem.py) and run it with Python 3. You get the optimized parameters for van Genuchten (VG) - Mualem equation as

    Modified VG model (hs = 2) with qs = 0.355 qr = 0.000 a = 0.00531 m = 0.107 q = 1.000 r = 2.000 
    Hydraulic conductivity parameters
    Ks = 3.84e-01 p = -5.366 R2 = 0.992

where qs and qr means &theta;<sub>s</sub> and &theta;<sub>r</sub> respectively, and R2 q means R<sup>2</sup> for &theta; of water retention curve and R2 logK means R<sup>2</sup> for log(K) of hydraulic conductivity curve. Modified model of [Vogel et al. (2000)](https://doi.org/10.1016/S0309-1708(00)00037-3) is used because n<2, as specified in the sample code. Following figure is produced.

![VG-Mualem](sample/VG-Mualem.png "VG-Mualem")
