# General HCF

The <strong>general HCF (hydraulic conductivity function)</strong> is defined as (Hoffmann-Riem et al, [1999](https://scholar.google.com/scholar_lookup?hl=en&publication_year=1999&pages=31-42&author=H.+Hoffmann%E2%80%90Riem&author=M.Th.+Genuchten&author=H.+Fl%C3%BChler&title=A+general+model+of+the+hydraulic+conductivity+of+unsaturated+soils))

{% raw %}
$$

\begin{equation}{K_{\rm{r}}}{\rm{\ }}\left( h \right) = \frac{{K\left( h \right)}}{{{K_{\rm{s}}}}}\ = S_e{\left( h \right)^p}\ {\left[ {\frac{{\mathop \smallint \nolimits_0^{S_e\left( h \right)} h{{\left( S_e \right)}^{ - q}}{\rm{d}}S_e\ }}{{\mathop \smallint \nolimits_0^1 h{{\left( S_e \right)}^{ - q}}{\rm{d}}S_e\ }}\ } \right]^r}\end{equation}
$$
{% endraw %}

where h is the pressure head (positive for unsaturated conditions), K is the unsaturated hydraulic conductivity, K<sub>s</sub> is the saturated hydraulic conductivity, K<sub>r</sub> is the relative hydraulic conductivity, and where p, q, and r are HCF parameters as explained below. S<sub>e</sub> is effective saturation, defined by $$S_e = \frac{\theta-\theta_r}{\theta_s-\theta_r}$$, where &theta; is the volumetric water content, and &theta;<sub>r</sub> and &theta;<sub>s</sub> are the residual and saturated water contents, respectively.

As the HCF includes integral of the function h(S<sub>e</sub>), it is convenient when a closed-form expression of the integrated function is obtained for a specified <strong>WRF (water retention function)</strong> &theta;(h) or S<sub>e</sub>(h), as shown in [this page](https://seki.webmasters.gr.jp/swrc/model.html); otherwise numerical integration or approximation is required. Most of the [HCF in unsatfit](model.md) are closed-form expression of general HCF derived from respective WRF.

## HCF parameters

The general HCF expresses different type of models with HCF parameters, p, q, r as follows.

- <strong>Burdine</strong> ([1953](https://doi.org/10.2118/225-G)) model for p=2, q=2, r=1.
- <strong>Mualem</strong> ([1976](https://doi.org/10.1029/WR012i003p00513)) model for p=0.5, q=1, r=2.

where Mualem's model is currently most widely used model. When p is used a variable and changed from the original value in those models, p is called a tortuosity factor.

## Research history

- Burdine ([1953](https://doi.org/10.2118/225-G)) proposed a permeability model from pore-size distribution of porous system by applying [Hagen–Poiseuille equation](https://en.wikipedia.org/wiki/Hagen%E2%80%93Poiseuille_equation).
- Brooks and Corey ([1964](https://scholar.google.com/scholar_lookup?hl=en&publication_year=1964&author=R.+H.+Brooks&author=A.+T.+Corey&title=Hydraulic+properties+of+porous+media)) developed a WRF $$S_e = \begin{cases}\left(h / h_b\right)^{-\lambda} & (h>h_b) \\ 1 & (h \le h_b)\end{cases}$$ and HCF based on Burdine's model.
- Mualem ([1976](https://doi.org/10.1029/WR012i003p00513)) proposed his model by considering the effect of combination of cylindrical tubes in radius r and &rho;, where the equivalent tube of radius R is expressed as R<sup>2</sup>=r&rho;. Mualem compared his model with other models, including Burdine's model, with measured data of 45 soils. The value p=0.5 was obtained as the optimized value with these 45 soils. I note (Seki, [2022](https://toyo.repo.nii.ac.jp/?action=repository_uri&item_id=13904&file_id=22&file_no=1)) that for Brooks and Corey model, Mualem's model (p=0.5, q=1, r=2) is equivalent to Burdine's model with changed p value (p=1.5, q=2, r=1).
- van Genuchten ([1980](https://doi.org/10.2136/sssaj1980.03615995004400050002x)) developed a WRF $$S_e = \bigl[1+(\alpha h)^n\bigr]^{-m}$$ and provided closed-form equations for Mualem's and Burdine's HCF. van Genuchten's WRF includes q as a parameter which is common with the HCF, and q determines the m-n relationship as m = 1-q/n. Therefore, when Mualem's model is used, q=1 for WRF, and when Burdine's model is used, q=2 for WRF. As van Genuchten and Nielsen ([1985](https://www.ars.usda.gov/ARSUserFiles/20360500/pdf_pubs/P0871.pdf)) showed that Mualem's approach was found to be applicable to a wider variety of soils than Burdine's model, <strong>van Genuchten-Mualem model</strong> is the most widely used combination of WRF and HCF today, and in many papers it is written that m = 1-1/n as q=1 is assumed.
- Hoffmann-Riem et al ([1999](https://scholar.google.com/scholar_lookup?hl=en&publication_year=1999&pages=31-42&author=H.+Hoffmann%E2%80%90Riem&author=M.Th.+Genuchten&author=H.+Fl%C3%BChler&title=A+general+model+of+the+hydraulic+conductivity+of+unsaturated+soils)) showed the general HCF model with van Genuchten WRF, and recommended optimizing p and r simultaneously.
- Kosugi ([1996](https://doi.org/10.1029/96WR01776)) proposed a WRF $$S_e = Q \biggl[\dfrac{\ln(h/h_m)}{\sigma}\biggr]$$ where $$Q(x) = \mathrm{erfc}(x/\sqrt{2})/2$$ and derived Mualem's and Burdine's HCF, and showed that similar curves to van Genuchten model are obtained. Kosugi ([1999](https://doi.org/10.2136/sssaj1999.03615995006300020003x)) applied general HCF to his WRF and showed that p and q are better to be optimized simultaneously.
- Durner ([1994](https://doi.org/10.1029/93WR02676)) proposed a linear suporposition of van Genuchten WRF, and showed that HCF calculated with Mualem's equation is better than simple van Genuchten model. Although Durner did not get a closed-form expression for HCF, Priesack and Durner ([2006](https://doi.org/10.2136/vzj2005.0066)) solved the equation with general HCF. Durner's model with Mualem's model has been used in several studies for water flow simulation. Seki et al. ([2022](https://doi.org/10.1002/vzj2.20168)) generalized the calculation to other combinations of BC, VG and KO models.
