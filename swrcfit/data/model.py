def model(ID):
    """Define model"""
    q = 'Q(x) &=& \mathrm{erfc}(x/\sqrt{2})/2'
    # q = 'Q(x) &=& \mathrm{erfc}(x/\sqrt{2})/2 = \int_{x}^{\infty}\\frac{\exp(-x^2/2)}{\sqrt{2\pi}}dx'
    if ID == 'all':
        return model('unimodal') + model('bimodal')
    if ID == 'unimodal':
        return ('BC', 'VG', 'KO', 'FX')
    if ID == 'bimodal':
        return ('DBCH', 'VGBCCH', 'DVCH', 'KOBCCH', 'DB', 'DV', 'DK')
    if ID == 'limit':
        return ('max_qs', 'max_lambda_i', 'max_n_i', 'min_sigma_i')
    if ID == 'savekeys':
        return model('all') + model('limit') + ('onemodel', 'cqs', 'cqr', 'qsin', 'qrin', 'input', 'show_eq', 'show_perr', 'show_cor')
    if ID == 'BC':
        return {
            'html': 'Brooks and Corey',
            'label': 'BC',
            'equation': 'S_e = \\begin{cases}\left(h / h_b\\right)^{-\lambda} & (h>h_b) \\\\ 1 & (h \le h_b)\end{cases}',
            'parameter': ('h<sub>b</sub>', '&lambda;'),
            'note': '',
            'selected': True
        }
    if ID == 'VG':
        return {
            'html': 'van Genuchten',
            'label': 'VG',
            'equation': 'S_e = \\biggl[\dfrac{1}{1+(\\alpha h)^n}\\biggr]^m ~~ (m=1-1/n)',
            'parameter': ('&alpha;', 'n'),
            'parameter_org': ('&alpha;', 'm'),
            'note': '',
            'selected': True
        }
    if ID == 'KO':
        return {
            'html': 'Kosugi',
            'label': 'KO',
            'equation': '\\begin{eqnarray}S_e &=& Q \\biggl[\dfrac{\ln(h/h_m)}{\sigma}\\biggr]\\\\' + q + '\end{eqnarray}',
            'parameter': ('h<sub>m</sub>', '&sigma;'),
            'note': '',
            'selected': False
        }
    if ID == 'FX':
        return {
            'html': 'Fredlund and Xing',
            'label': 'FX',
            'equation': 'S_e = \\biggl[ \dfrac{1}{\ln \left[e+(h / a)^n \\right]} \\biggr]^m',
            'parameter': ('a', 'm', 'n'),
            'note': 'For FX model, e is Napier\'s constant.',
            'selected': False
        }
    if ID == 'DBCH':
        return {
            'html': 'dual-BC-CH',
            'label': 'dual-BC-CH',
            'equation': 'S_e = \\begin{cases}w_1 \left(h / h_b\\right)^{-\lambda_1} + (1-w_1)\left(h / h_b\\right)^{-\lambda_2}  & (h>h_b)\\\\ 1 & (h \le h_b)\end{cases}',
            'equation_conv': '\\begin{eqnarray}S_e &=& \\begin{cases}w_1 \left(h / h_b\\right)^{-\lambda_1} + (1-w_1)\left(h / h_b\\right)^{-\lambda_2}  & (h>h_b)\\\\ 1 & (h \le h_b)\end{cases}\\\\w_1 &=& \dfrac{1}{1 + \left(h_c / h_b\\right)^{(l_2 - l_1)}}\end{eqnarray}',
            'parameter': ('w<sub>1</sub>', 'h<sub>b</sub>', '&lambda;<sub>1</sub>', '&lambda;<sub>2</sub>'),
            'parameter_org': ('h<sub>c</sub>', 'h<sub>b</sub>', '&lambda;<sub>1</sub>', '&lambda;<sub>2</sub>'),
            'note': '',
            'selected': False
        }
    if ID == 'VGBCCH':
        return {
            'html': 'VG<sub>1</sub>BC<sub>2</sub>-CH',
            'label': '$\mathrm{VG}_1\mathrm{BC}_2$-CH',
            'equation': '\\begin{eqnarray}S_e &=& \\begin{cases}w_1 S_1 + (1-w_1)\left(h/H\\right)^{-\lambda_2}  & (h>H)\\\\ w_1 S_1 + 1-w_1 & (h \le H)\end{cases}\\\\S_1 &=& \\bigl[1+(h/H)^{n_1}\\bigr]^{-{m_1}} ~~ (m_1=1-1/{n_1})\end{eqnarray}',
            'parameter': ('w<sub>1</sub>', 'H', 'n<sub>1</sub>', '&lambda;<sub>2</sub>'),
            'parameter_org': ('w<sub>1</sub>', 'H', 'm<sub>1</sub>', '&lambda;<sub>2</sub>'),
            'note': '',
            'selected': False
        }
    if ID == 'DVCH':
        return {
            'html': 'dual-VG-CH',
            'label': 'dual-VG-CH',
            'equation': '\\begin{eqnarray}S_e &=& w_1\\bigl[1+(\\alpha h)^{n_1}\\bigr]^{-m_1} + (1-w_1)\\bigl[1+(\\alpha h)^{n_2}\\bigr]^{-m_2}\\\\m_i&=&1-1/{n_i}\end{eqnarray}',
            'parameter': ('w<sub>1</sub>', '&alpha;', 'n<sub>1</sub>', 'n<sub>2</sub>'),
            'parameter_org': ('w<sub>1</sub>', '&alpha;', 'm<sub>1</sub>', 'm<sub>2</sub>'),
            'note': '',
            'selected': True
        }
    if ID == 'KOBCCH':
        return {
            'html': 'KO<sub>1</sub>BC<sub>2</sub>-CH',
            'label': '$\mathrm{KO}_1\mathrm{BC}_2$-CH',
            'equation': '\\begin{eqnarray}S_e &=& \\begin{cases}w_1 S_1 + (1-w_1)\left(h/H\\right)^{-\lambda_2}  & (h>H)\\\\ w_1 S_1 + 1-w_1 & (h \le H)\end{cases}\\\\S_1 &=& Q \\biggl[\dfrac{\ln(h/h_m)}{\sigma_1}\\biggr], Q(x) = \mathrm{erfc}(x/\sqrt{2})/2\end{eqnarray}',
            'parameter': ('w<sub>1</sub>', 'H', '&sigma;<sub>1</sub>', '&lambda;<sub>2</sub>'),
            'note': '',
            'selected': True
        }
    if ID == 'DB':
        return {
            'html': 'dual-BC',
            'label': 'dual-BC',
            'equation': 'S_e = \\begin{cases}w_1 \left(h / h_{b_1}\\right)^{-\lambda_1} + (1-w_1)\left(h / h_{b_2}\\right)^{-\lambda_2}  & (h>h_{b_2}) \\\\ ' +
            'w_1 \left(h / h_{b_1}\\right)^{-\lambda_1} + 1-w_1  & (h_{b_1} < h \le h_{b_2}) \\\\1 & (h \le h_{b_1})\end{cases}',
            'parameter': ('w<sub>1</sub>', 'hb<sub>1</sub>', '&lambda;<sub>1</sub>', 'hb<sub>2</sub>', '&lambda;<sub>2</sub>'),
            'note': '',
            'selected': False
        }
    if ID == 'DV':
        return {
            'html': 'dual-VG',
            'label': 'dual-VG',
            'equation': '\\begin{eqnarray}S_e &=& w_1\\bigl[1+(\\alpha_1 h)^{n_1}\\bigr]^{-m_1} + (1-w_1)\\bigl[1+(\\alpha_2 h)^{n_2}\\bigr]^{-m_2}\\\\m_i&=&1-1/{n_i}\end{eqnarray}',
            'parameter': ('w<sub>1</sub>', '&alpha;<sub>1</sub>', 'n<sub>1</sub>', '&alpha;<sub>2</sub>', 'n<sub>2</sub>'),
            'parameter_org': ('w<sub>1</sub>', '&alpha;<sub>1</sub>', 'm<sub>1</sub>', '&alpha;<sub>2</sub>', 'm<sub>2</sub>'),
            'note': '',
            'selected': True
        }
    if ID == 'DK':
        return {
            'html': 'dual-KO',
            'label': 'dual-KO',
            'equation': '\\begin{eqnarray}S_e &=& w_1 Q \\biggl[\dfrac{\ln(h/h_{m_1})}{\sigma_1}\\biggr] + (1-w_1) Q \\biggl[\dfrac{\ln(h/h_{m_2})}{\sigma_2}\\biggr]\\\\' + q + '\end{eqnarray}',
            'parameter': ('w<sub>1</sub>', 'hm<sub>1</sub>', '&sigma;<sub>1</sub>', 'hm<sub>2</sub>', '&sigma;<sub>2</sub>'),
            'note': '',
            'selected': False
        }
