#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
from model import model
from sample import sample

PATH = os.getcwd() + '/../'


def fig():
    f = open(PATH + 'fig.html', 'w', encoding='UTF-8')
    f.write('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Sample output of SWRC Fit</title>
  <link rel="stylesheet" type="text/css" href="swrc.css">
</head>
<body>
<h1>Sample output of SWRC Fit</h1>
<p>
This is a list of figures produced by <a href="./">SWRC Fit</a>. Sample data provided in the pulldown menu were analyzed with the default setting.
<ul>
<li>Fit &theta;<sub>r</sub> for unimodal and &theta;<sub>r</sub> = 0 for bimodal.
<li>Fit &theta;<sub>s</sub>.
</ul>
<p>One of the figures is shown randomly at the page of SWRC Fit. Note that selected models are different.
</p>
''')
    data = sample()
    for id in data:
        d = data[id]
        soil = d['Soil sample']
        texture = d['Texture']
        f.write('<h2>{0} : {1}</h2>\n<p><div align="center"><img src="img/{2}.png" alt="Sample output"></div></p>'.format(soil, texture, id))

    f.write('''
<hr>
<p>Persistent URL of this page is <a href="http://purl.org/net/swrc/fig.html">http://purl.org/net/swrc/fig.html</a>.
</p>
<p>
Author: <a href="https://sekika.github.io/toyo/en/">Katsutoshi Seki</a>
</p>
</body>
</html>
''')
    f.close()


def unitable(models):
    text = ''
    for id in models:
        m = model(id)
        text += '<tr><td>{0}<td>{1}<td>\\({2}\\)<td>&theta;<sub>s</sub> &theta;<sub>r</sub>, {3}</tr>'.format(
            id, m['html'], m['equation'], (', ').join(m['parameter']))
    text += '</table>'
    return text


def bitable(models):
    text = ''
    for id in models:
        m = model(id)
        text += '<tr><td>{0}<td>\\({1}\\)<\td>&theta;<sub>s</sub> &theta;<sub>r</sub>, {2}</tr>'.format(
            m['html'], m['equation'], (', ').join(m['parameter']))
    text += '</table>'
    return text


def ref1():
    return '''
<ul>
<li>Brooks, R.H., and A.T. Corey (1964): Hydraulic properties of porous media. Hydrol. Paper 3. Colorado State Univ., Fort Collins, CO, USA.</li>
<li>Durner, W. (1994): Hydraulic conductivity estimation for soils with heterogeneous pore structure. <i>Water Resour. Res.</i>, 30(2): 211-223. <a href="http://dx.doi.org/10.1029/93WR02676">doi:10.1029/93WR02676</a></li>
<li>Fredlund, D.G. and Xing, A. (1994): Equations for the soil-water characteristic curve. <i>Can. Geotech. J.</i>, 31: 521-532. <a href="http://dx.doi.org/10.1139/t94-061">doi:10.1139/t94-061</a></li>
<li>Kosugi, K. (1996): Lognormal distribution model for unsaturated soil hydraulic properties. <i>Water Resour. Res.</i> 32: 2697-2703. <a href="http://dx.doi.org/10.1029/96WR01776">doi:10.1029/96WR01776</a></li>
<li>Seki, K. (2007): SWRC fit - a nonlinear fitting program with a water retention curve for soils having unimodal and bimodal pore structure. <i>Hydrol. Earth Syst. Sci. Discuss.</i>, 4: 407-437. <a href="http://dx.doi.org/10.5194/hessd-4-407-2007">doi:10.5194/hessd-4-407-2007</a></li>
<li>Seki, K., Toride, N., & Th. van Genuchten, M. (2022). Closed-form hydraulic conductivity equations for multimodal unsaturated soil hydraulic properties. Vadose Zone J. 21, e20168. <a href="https://doi.org/10.1002/vzj2.20168">doi:10.1002/vzj2.20168</a></li>
<li>Seki, K., Toride, N., & Th. van Genuchten, M. (2023). Evaluation of a general model for multimodal unsaturated soil hydraulic properties. J. Hydrol. Hydromech. 71(1): 22-34. <a href="https://doi.org/10.2478/johh-2022-0039">doi:10.2478/johh-2022-0039</a>
'''


def ref2():
    return '''
<li>van Genuchten, M. (1980): A closed-form equation for predicting the hydraulic conductivity of unsaturated soils. <i>Soil Sci. Soc. Am. J.</i> 44:892-898. <a href="https://doi.org/10.2136/sssaj1980.03615995004400050002x">doi:10.2136/sssaj1980.03615995004400050002x</a></li>
</ul>
'''


def english():
    f = open(PATH + 'model.html', 'w', encoding='UTF-8')
    f.write('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Models of SWRC Fit</title>
  <link rel="stylesheet" type="text/css" href="swrc.css">
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
<p>[ English | <a href="model-ja.html">日本語</a> ]</p>

<h1>Soil hydraulic models in SWRC Fit</h1>

<p>Soil water retention curve (SWRC) is described by water retention function &theta;(h) is a function of volumetric water content, &theta; to pressure head, h. Here we denote h to be positive for unsaturated conditions, thus considering to be an equivalent suction.
Effective water content S<sub>e</sub> is defined by \\(S_e = \\frac{\\theta-\\theta_r}{\\theta_s-\\theta_r}\\), where saturated water content &theta;<sub>s</sub> and residual water content &theta;<sub>r</sub> are parameters either treated as constant or variable.
We can obtain &theta;(h) from S<sub>e</sub>(h) by &theta;(h) = (&theta;<sub>s</sub> - &theta;<sub>r</sub>)S<sub>e</sub>(h) + &theta;<sub>r</sub></p>

<p><a href="./">SWRC Fit</a> simultaneously fits measured SWRC data to multiple S<sub>e</sub>(h) functions described as follows and determine the parameters of the functions.</p>

<h2>Unimodal models</h2>
<table border="1"><tr><td>Abbr.<td>Model<td>Equation<td>Parameters</tr>
''')
    f.write(unitable(model('unimodal')))
    f.write('''

<ul>
<li>In KO model, Q(x) is the complementary cumulative normal distribution function, defined by Q(x)=1-&Phi;(x), in which &Phi;(x) is a normalized form of the <a href="http://mathworld.wolfram.com/NormalDistributionFunction.html">cumulative normal distribution function</a>, and can be computed from complementary error function erfc(x) = 1-erf(x) as shown in the table.</li>
<li>In FX model, e is <a href="https://en.wikipedia.org/wiki/E_(mathematical_constant)">Napier's constant</a>.</li>
<li>Citations are shown in reference section.</li>
</ul>

<p>Here is SWRC for the sample data, clay loam (UNSODA 3033) with unimodal models, with all variables including &theta;<sub>s</sub> and &theta;<sub>r</sub> are optimized.
Fitted parameters, coefficient of determination (R<sub>2</sub>) and <a href="https://en.wikipedia.org/wiki/Akaike_information_criterion">AIC</a> can be shown in table by executing calculation with SWRC Fit.</p>

<div align="center"><img src="img/unimodal.png" alt="Unimodal models"></div>

<h2>Multimodal models</h2>

<p>Multimodal water retention function is defined as a linear superposition of subfunctions S<sub>i</sub>(h) as follows (<a href="https://doi.org/10.1002/vzj2.20168">Seki et al., 2022</a>).
\\[ S(h) = \\Sigma_{i=1}^k w_i S_i(h) \\]
where k is the number of subfunctions, and w<sub>i</sub> are weighting factors with 0&lt;w<sub>i</sub>&lt;1 and &Sigma;w<sub>i</sub> = 1.
Unimodal models are k=1, and bimodal models are k=2.</p>

<p>The multimoodal model is denoted by subscripting the number of the subfunction.
For example, VG<sub>1</sub>BC<sub>2</sub> model denotes VG subfunction for S<sub>1</sub>(h) and BC subfunction for S<sub>2</sub>(h).
Combinations of the same subfunctions (e.g., BC<sub>1</sub>BC<sub>2</sub>BC<sub>3</sub>...) are referred to as the multimodels (e.g., multi-BC).
The multi-VG model is the same as Durner (1994) model, and multi-KO model is the same as Seki (2007) model.
Multimodels consisting of only two similar subfunctions are referred to as dual-models, such as the dual-BC for BC<sub>1</sub>BC<sub>2</sub>.</p>

<h2>Bimodal models</h2>
<p>As explained in the previous section, there are some possible combinations of bimodal models, where following models are implemented in SWRC Fit.</p>
<table border="1"><tr><td>Model<td>Equation<td>Parameters</tr>
''')
    bimodal = model('bimodal')
    ch = []
    noch = []
    for m in bimodal:
        if 'CH' in m:
            ch.append(m)
        else:
            noch.append(m)
    f.write(bitable(noch))
    f.write('''

<p>Here is SWRC for the sample data, silty loam (UNSODA 2760) with bimodal models and VG model for comparison.
Fixed parameter &theta;<sub>r</sub> = 0 is used for bimodal models, while all variables are optimized for VG model.</p>

<div align="center"><img src="img/bimodal.png" alt="Bimodal models"></div>

<p>See also <a href="https://acsess.onlinelibrary.wiley.com/doi/10.1002/vzj2.20168#vzj220168-fig-0001">Figure 1 in Seki et al., 2022</a>.</p>

<h2>CH variation</h2>

<p>CH (common head) variation for multimodal model of BC, VG, KO subfunctions is defined in <a href="https://doi.org/10.1002/vzj2.20168">Seki et al. (2022)</a> as
\\[H = h_{b_i} = \\alpha_i^{-1} = h_{m_i} \\]
where following models are implemented in SWRC Fit.</p>
<table border="1"><tr><td>Model<td>Equation<td>Parameters</tr>
''')
    f.write(bitable(ch))
    f.write('''
<p>Here is SWRC for the sample data, sand (UNSODA 4440) with CH variations of bimodal models and VG model for comparison.
Fixed parameter &theta;<sub>r</sub> = 0 is used for bimodal models, while all variables are optimized for VG model.
&theta;<sub>r</sub> is optimized at 0.074 for VG model.</p>

<div align="center"><img src="img/dual-ch.png" alt="dual-CH models"></div>

<p>See also <a href="https://acsess.onlinelibrary.wiley.com/doi/10.1002/vzj2.20168#vzj220168-fig-0002">Figure 2 in Seki et al., 2022</a>.</p>

<h2>Hydraulic conductivity functions</h2>

<p>For water retention functions except for FX model, closed-form hydraulic conductivity equations with generalized Mualem's equation are available (<a href="https://doi.org/10.1002/vzj2.20168">Seki et al., 2022</a>). The equations are useful for practical applications as shown in <a href="https://doi.org/10.2478/johh-2022-0039">Seki et al. (2023)</a>. Use <a href="https://sekika.github.io/unsatfit/">unsatfit</a> for fitting with those functions.</p>

<h2>Note for notation</h2>

<p>In the old version of SWRC Fit, KO model was denoted as LN model, dual-VG model was denoted as DB model, and dual-KO was denoted as BL model. The notation was changed to match Seki et al. (2022).</p>

<h2>Reference</h2>
''')
    f.write(ref1())
    f.write(ref2())
    f.write('''
<hr>
<p>Persistent URL of this page is <a href="http://purl.org/net/swrc/model.html">http://purl.org/net/swrc/model.html</a>.
</p>
<p>
Author: <a href="https://sekika.github.io/toyo/en/">Katsutoshi Seki</a>
</p>
</body>
</html>
''')
    f.close


def japanese():
    f = open(PATH + 'model-ja.html', 'w', encoding='UTF-8')
    f.write('''
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SWRC Fit のモデル</title>
  <link rel="stylesheet" type="text/css" href="swrc.css">
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
<p>[ <a href="model.html">English</a> | 日本語 ]</p>

<h1>SWRC Fit の土壌水分保持関数</h1>

<p>土壌水分保持曲線 (SWRC) は体積含水率θの圧力水頭hによる関数である水分保持関数 &theta;(h) によってあらわされる（<a href="https://toyo.repo.nii.ac.jp/?action=repository_uri&item_id=8838&file_id=22&file_no=1">関, 2017</a>）。ここで h は不飽和で正の値とするサクション（負圧）である。
有効水分量 S<sub>e</sub> は \\(S_e = \\frac{\\theta-\\theta_r}{\\theta_s-\\theta_r}\\) と定義される。
ここで、飽和含水率θ<sub>s</sub>と残留含水率θ<sub>r</sub>は定数とすることも変数とすることもできる。
S<sub>e</sub>(h) から θ(h) を θ(h) = (θ<sub>s</sub> - θ<sub>r</sub>)S<sub>e</sub>(h) + θ<sub>r</sub> によって得ることができる。</p></p>

<p><a href="./?lang=ja">SWRC Fit</a> では、SWRC の測定値を以下に記述されている複数のS<sub>e</sub>(h)関数で非線形回帰してパラメータを決定することができる。</p>

<h2>基本モデル（ユニモーダルモデル）</h2>
<table border="1"><tr><td>略記<td>モデル<td>式<td>パラメータ</tr>
''')
    f.write(unitable(model('unimodal')))
    f.write('''
<ul>
<li>KOモデルの相補累積分布関数 Q(x) は、&Phi;(x)を<a href="https://ja.wikipedia.org/wiki/%E7%B4%AF%E7%A9%8D%E5%88%86%E5%B8%83%E9%96%A2%E6%95%B0">累積分布関数</a>としたときに
Q(x)=1-&Phi;(x) とあらわされる関数であり、<a href="https://ja.wikipedia.org/wiki/%E7%B4%AF%E7%A9%8D%E5%88%86%E5%B8%83%E9%96%A2%E6%95%B0">誤差関数</a> erf(x) の補関数 erfc(x) = 1-erf(x) から表のように計算される</li>
<li>FX モデルの e はネイピア数である。</li>
<li>文献リストは文末に示す。</li>
</ul>

<p>SWRC Fit のサンプルデータ clay loam (UNSODA 3033) から得られた土壌水分保持曲線(SWRC)を示す。θ<sub>s</sub>とθ<sub>r</sub>を含むすべてのデータを最適化した。最適化されたパラメータ、決定係数(R<sup>2</sup>)、<a href="https://ja.wikipedia.org/wiki/%E8%B5%A4%E6%B1%A0%E6%83%85%E5%A0%B1%E9%87%8F%E8%A6%8F%E6%BA%96">AIC</a>の一覧表はサンプルデータから計算を実行することで見ることができる。</p>

<div align="center"><img src="img/unimodal.png" alt="Unimodal models"></div>

<h2>線型和モデル（マルチモデル）</h2>

<p>線形和水分保持関数は基本モデルをサブ関数S<sub>i</sub>(h)としてその線形和で定義される (<a href="https://doi.org/10.1002/vzj2.20168">Seki et al., 2022</a>; <a href="https://researchmap.jp/sekik/presentations/36027912/attachment_file.pdf">関ら, 2021</a>)。
\\[ S(h) = \\Sigma_{i=1}^k w_i S_i(h) \\]
k はサブ関数の数、w<sub>i</sub> は重み係数で 0&lt;w<sub>i</sub>&lt;1, &Sigma;w<sub>i</sub> = 1 である。
ユニモーダルモデルは k=1 バイモーダルモデルは k=2 である。</p>

<p>線形和モデルはサブ関数の番号を下付き文字で表記することであらわす。たとえば、VG<sub>1</sub>BC<sub>2</sub>モデルはVGサブ関数を S<sub>1</sub>(h)、BCサブ関数をS<sub>2</sub>(h)とする。BC<sub>1</sub>BC<sub>2</sub>BC<sub>3</sub>... のような同じサブ関数の組み合わせは multi-BC モデルのように表記して multi-モデルと呼ぶ。multi-VG モデルは Durner (1994) のモデルと同じで、 multi-KO モデルは Seki (2007) と同じである。2つの同じ関数を組み合わせた multi-モデルは dual-モデルであり、たとえば dual-BC は BC<sub>1</sub>BC<sub>2</sub> である。</p>

<h2>二重モデル（バイモーダルモデル）</h2>
<p>このようにバイモーダルモデルにはいくつかの組み合わせが考えられるが、SWRC Fit では以下のモデルが実装されている。</p>
<table border="1"><tr><td>モデル<td>式<td>パラメータ</tr>
''')
    bimodal = model('bimodal')
    ch = []
    noch = []
    for m in bimodal:
        if 'CH' in m:
            ch.append(m)
        else:
            noch.append(m)
    f.write(bitable(noch))
    f.write('''

<p>特に、日本の土壌では団粒が発達した土壌においてはバイモーダルモデルが有効であり、バイモーダルモデルの回帰には特段の工夫がされている(<a href="https://doi.org/10.34467/jssoilphysics.155.0_35">関ら, 2023</a>)。</p>

<p>サンプルデータ silty loam (UNSODA 2760) のSWRCを示す。上記のバイモーダルモデルと、比較のためにVGモデルを示している。バイモーダルモデルではθ<sub>r</sub> = 0 と固定し、VGモデルではすべてのパラメータを自由変数としている。</p>

<div align="center"><img src="img/bimodal.png" alt="Bimodal models"></div>

<p><a href="https://acsess.onlinelibrary.wiley.com/doi/10.1002/vzj2.20168#vzj220168-fig-0001">Seki et al. (2022) の Figure 1</a> には、熊本黒ボク土のバイモーダルモデルによるSWRCと透水性曲線が示されている。同じ図は関ら (2021) にも示されている。</p>

<h2>CHモデル</h2>

<p>BC, VG, KOサブ関数に対する線形和モデルに対する CHモデルが <a href="https://doi.org/10.1002/vzj2.20168">Seki et al. (2022)</a>において
\\[H = h_{b_i} = \\alpha_i^{-1} = h_{m_i} \\]
と定義されている。この中で、次の関数が SWRC Fit に実装されている。</p>
<table border="1"><tr><td>モデル<td>式<td>パラメータ</tr>
''')
    f.write(bitable(ch))
    f.write('''
<p>サンプルデータ sand (UNSODA 4440) のSWRCを示す。上記のCHモデルと、比較のためにVGモデルを示している。CHモデルではθ<sub>r</sub> = 0 と固定し、VGモデルではすべてのパラメータを自由変数としている。VGモデルではθ<sub>r</sub>=0.074と最適化された。</p>

<div align="center"><img src="img/dual-ch.png" alt="dual-CH models"></div>

<p><a href="https://acsess.onlinelibrary.wiley.com/doi/10.1002/vzj2.20168#vzj220168-fig-0002">Seki et al. (2022) の Figure 2</a> には、浜岡砂丘砂のCHモデルによるSWRCと透水性曲線が示されている。同じ図は関ら (2021) にも示されている。</p>

<h2>透水性関数</h2>

<p>FX モデル以外のモデルに対しては、一般化Mualem式による不飽和透水係数の閉形式解が得られている (<a href="https://doi.org/10.1002/vzj2.20168">Seki et al., 2022</a>; <a href="https://researchmap.jp/sekik/presentations/36027912/attachment_file.pdf">関ら, 2021</a>; <a href="https://www.jstage.jst.go.jp/article/jssoilphysics/154/0/154_19/_article/-char/ja/">関・取出, 2023</a>)。それが実用的な式であることは<a href="https://doi.org/10.2478/johh-2022-0039">Seki et al. (2023)</a>が示している。<a href="https://sekika.github.io/unsatfit/">unsatfit</a>によって透水性関数のフィッティングが可能である。</p>

<h2>モデルの略記について</h2>

<p>SWRC Fit の旧バージョンでは、KOモデルをLNモデル、dual-VGモデルをDBモデル、dual-KOモデルBLモデルと表記していたが、Seki et al. (2022) の表記にあわせて変更した。</p>

<h2>文献</h2>
''')
    f.write(ref1())
    f.write('''
<li>関勝寿 (2017): <a href="https://toyo.repo.nii.ac.jp/?action=repository_uri&item_id=8838&file_id=22&file_no=1">水分特性曲線の回帰プログラム SWRC Fit (1)−水分特性モデル−</a>. 東洋大学紀要自然科学篇 61: 41-65.
<li>関勝寿, 取出伸夫, M.Th. van Genuchten (2021): <a href="https://researchmap.jp/sekik/presentations/36027912/attachment_file.pdf">線形和水分保持関数に対するMualemモデルの不飽和透水係数</a>. 2021年度土壌物理学会大会 講演要旨集 pp.30-31.
<li>関勝寿, 取出伸夫 (2023): 一般化透水モデルによる不飽和透水係数の閉形式解. 土壌の物理性 154: 19-27. <a href="https://doi.org/10.34467/jssoilphysics.154.0_19">doi:10.34467/jssoilphysics.154.0_19</a>
<li>関勝寿, 岩田幸良, 柳井洋介, 亀山幸司 (2023): 団粒構造が発達した土壌の水分特性曲線の回帰手法の改良 ーdual-van Genuchtenモデルのパラメータ決定の自動化に向けた取り組みー</a>. 土壌の物理性 155: 35-44. <a href="https://doi.org/10.34467/jssoilphysics.155.0_35">doi:10.34467/jssoilphysics.155.0_35</a>
''')
    f.write(ref2())
    f.write('''
<hr>
<p>このページの恒久的な URL (PURL) は <a href="http://purl.org/net/swrc/model.html">http://purl.org/net/swrc/model.html</a> です。
</p>
<p>
著者: <a href="https://sekika.github.io/toyo/">関 勝寿</a>
</p>
</body>
</html>
''')
    f.close


def main():
    """Make html"""
    fig()
    english()
    japanese()


if __name__ == '__main__':
    main()
