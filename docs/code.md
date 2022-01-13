# Sample code of unsatfit

Put [water retention curve](https://github.com/sekika/unsatfit/blob/main/docs/sample/ht3393.csv) and [unsaturated hydraulic conductivity curve](https://github.com/sekika/unsatfit/blob/main/docs/sample/hk3393.csv) of UNSODA 3393 in the same directory as [this sample code](https://github.com/sekika/unsatfit/blob/main/docs/sample/VG-Mualem.py) and run it with Python 3. You get the optimized parameters for VG-Mualem equation as

    Water retention parameters with m=1-1/n (q=1)
    qs = 0.355 qr = 0.000 a = 0.00531 m = 0.107
    Hydraulic conductivity parameters
    Ks = 8.88e-01 p = 0.895 r = 1.447 R2 q = 0.992 R2 logK = 0.973

where qs and qr means &theta;<sub>s</sub> and &theta;<sub>r</sub> respectively, and R2 q means R<sup>2</sup> for &theta; of water retention curve and R2 logK means R<sup>2</sup> for log(K) of hydraulic conductivity curve. Following figure is produced.

![VG-Mualem](sample/VG-Mualem.png "VG-Mualem")
