# Sample code of unsatfit

Put [water retention curve](https://github.com/sekika/unsatfit/blob/main/docs/sample/ht3393.csv) and [unsaturated hydraulic conductivity curve](https://github.com/sekika/unsatfit/blob/main/docs/sample/hk3393.csv) of UNSODA 3393 in the same directory as [this sample code](https://github.com/sekika/unsatfit/blob/main/docs/sample/VG-Mualem.py) and run it with Python 3. You get the optimized parameters for van Genuchten (VG) - Mualem equation as

    Water retention parameters with m=1-1/n (q=1)
    qs = 0.355 qr = 0.000 a = 0.00531 m = 0.107
    Modified VG model with hs=2cm is used because n<2
    Hydraulic conductivity parameters
    Ks = 9.84e-01 p = 0.002 R2 q = 0.992 R2 logK = 0.868

where qs and qr means &theta;<sub>s</sub> and &theta;<sub>r</sub> respectively, and R2 q means R<sup>2</sup> for &theta; of water retention curve and R2 logK means R<sup>2</sup> for log(K) of hydraulic conductivity curve. Modified model of [Vogel et al. (2000)](https://doi.org/10.1016/S0309-1708(00)00037-3) is used because n<2, as specified in the sample code. Following figure is produced.

![VG-Mualem](sample/VG-Mualem.png "VG-Mualem")
