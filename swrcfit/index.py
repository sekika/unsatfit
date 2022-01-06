#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import configparser
from data.message import message
from data.model import model
from data.sample import sample
from data.sample import dataset
config = configparser.ConfigParser()
config.read('data/server.txt')
DEBUG = config.get('Settings', 'debug')
WORKDIR = config.get('Settings', 'workdir')
IMAGEFILE = config.get('Settings', 'imagefile')
STORAGEPREFIX = 'swrc_'

os.environ['MPLCONFIGDIR'] = WORKDIR


def main():
    """SWRC Fit to run as CGI"""
    import cgi
    from io import TextIOWrapper
    from os import getenv
    import unsatfit
    f = unsatfit.Fit()

    if DEBUG:
        import cgitb
        cgitb.enable()

    # Change encoding of stdout to utf-8
    # It is required becaue CGI script runs as another user and may not
    # print utf-8 encoded text
    sys.stdout = TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # Respond HTTP header
    print('Content-Type: text/html')
    print('Cache-Control: public\n')

    # Get input strings
    field = cgi.FieldStorage()
    getlang = field.getfirst('lang', 'none')
    f.inputtext = field.getfirst('input', '')

    # Get language setting
    LANGUAGES = message('', 'list')
    lang = getenv('HTTP_ACCEPT_LANGUAGE')
    if lang is None:
        lang = []
    else:
        lang = lang.split(',')
    lang.append('en')
    for i in lang:
        if i[:2] in LANGUAGES:
            lang = i[:2]
            break
    if getlang in LANGUAGES:
        lang = getlang
    f.lang = lang
    f.getlang = getlang

    # Get model selection
    f.selectedmodel = []
    for m in model('all'):
        if field.getfirst(m, '') == 'on':
            f.selectedmodel.append(m)
    f.onemodel = (field.getfirst('onemodel', '') == 'on')

    # Figure options
    f.show_fig = False
    f.save_fig = True
    f.filename = 'img/swrc.png'
    f.fig_width = 5.5  # inch
    f.fig_height = 4.5
    f.top_margin = 0.05
    f.bottom_margin = 0.12
    f.left_margin = 0.15  # Space for label is needed
    f.right_margin = 0.05
    f.legend_loc = 'upper right'
    f.color_marker = 'blue'
    f.linecolors = ('red', 'blue', 'green', 'magenta', 'cyan', 'black')

    f.sampledata = sample()
    printhead(lang, f)
    print('<body>')
    d = dataset(f.inputtext)

    if field.getfirst('button') == 'Clear setting':
        # Clear field storage
        for i in model('savekeys'):
            key = STORAGEPREFIX + i
            print(
                '<script>localStorage.removeItem("{0}");</script>'.format(key))
        printform(lang, getlang, f)
        printhelp(lang, f)
    else:
        if d['empty']:
            printform(lang, getlang, f)
            printhelp(lang, f)
        elif f.selectedmodel == []:
            printform(lang, getlang, f)
            print('<p><strong>Please select at least one model.</strong></p>')
            printhelp(lang, f)
        elif not d['valid']:
            printform(lang, getlang, f)
            error = escape(d['message']).replace(
                'Error in input data', message(lang, 'inputerror'))
            if d['message'] == 'All h values are same.':
                error = message(lang, 'sameh')
            print(
                '<p><strong>{0}</strong></p><p>{1}</p>'.format(error, message(lang, 'readformat')))
            printhelp(lang, f)
        else:
            f.swrc = h, theta = d['data']  # Data of soil water retention
            f.data = d
            # Get options
            f.cqs = field.getfirst('cqs', '')
            f.cqr = field.getfirst('cqr', '')
            f.qsin = field.getfirst('qsin', str(max(theta)))
            f.qrin = field.getfirst('qrin', '')
            # Save field storage to local storage
            for i in model('savekeys'):
                value = '//'.join(field.getfirst(i, 'off').splitlines())
                if i in ['qsin', 'qrin', 'sigmax']:
                    try:
                        value = float(value)
                    except ValueError:
                        value = 'off'
                    if value == 'off':
                        if i == 'qsin':
                            value = ''
                        if i == 'qrin':
                            value = 0
                        if i == 'sigmax':
                            value = 2.5
                    else:
                        if value <= 0:
                            value = 0
                        if value < 1 and i == 'sigmax':
                            value = 1
                    value = str(value)
                key = STORAGEPREFIX + i
                print(
                    '<script>localStorage.setItem("{0}", "{1}");</script>'.format(key, value))
            calc(f)   # Start main calculation
    # Print footer
    import platform
    footer = message(lang, "footer")
    footer = footer.replace('VER', f.version())
    footer = footer.replace('AUTHOR', message(lang, 'author'))
    pyver = str(sys.version_info.major) + '.' + \
        str(sys.version_info.minor) + '.' + str(sys.version_info.micro)
    footer = footer.replace('PYV', pyver).replace('ARCH', platform.system())
    print('<hr>\n<p>{0}</p>\n<p style="text-align:right;"><img src="https://seki.webmasters.gr.jp/swrc/npc.cgi?L=http://purl.org/net/swrc/" alt="counter"></p></body></html>'.format(footer), flush=True)
    return


def calc(f):
    """Main calculation"""
    import copy
    lang = f.lang
    getlang = f.getlang
    d = f.data
    result = []
    # Note
    note = [
        'The model with minumum AIC is shown in red color. AIC (<a href="https://en.wikipedia.org/wiki/Akaike_information_criterion">Akaike Information Criterion</a>) = n ln(RSS/n)+2k, where n is sample size, RSS is residual sum of squares and k is the number of estimated parameters.']
    note.append(
        'Effective saturation \\(S_e = \\frac{\\theta-\\theta_r}{\\theta_s-\\theta_r}\\). Therefore &theta; = &theta;<sub>r</sub> + (&theta;<sub>s</sub>-&theta;<sub>r</sub>)S<sub>e</sub>.')

    # Show process
    if getlang in message('', 'list'):
        url = './?lang='+lang
    else:
        url = './'
    print(
        '<h1><a href="{0}">SWRC Fit</a> - {1}</h1>'.format(url, message(lang, 'result')))
    print('<ul>')
    for i in sorted(d):
        if i not in ['empty', 'valid', 'text', 'data']:
            if i == 'doi':
                print(
                    '<li>{0} = <a href="https://doi.org/{1}">{1}</a>'.format(escape(i), escape(d[i])))
            else:
                print('<li>{0} = {1}'.format(escape(i), escape(d[i])))
    for i in getoptiontheta(f, True)[0]:
        bi = ''
        if f.cqr == 'both' and i[0] == 2:
            bi = ' for bimodal models'
        par = ('&theta;<sub>s</sub>', '&theta;<sub>r</sub>')[i[0]-1]
        print('<li>Constant: {0} = {1}{2}'.format(par, i[1], bi))
    print('</ul>')
    print(
        '<div class="tmp" id="tmp">{0}</div>'.format(message(lang, 'wait')), flush=True)

    # Fixed parameters
    con_q, ini_q, par_theta = getoptiontheta(f, False)

    # BC (Brooks and Corey) model
    if 'BC' in f.selectedmodel:
        hb, l = f.get_init_bc()  # Get initial parameter
        f.set_model('bc', const=[*con_q])
        f.ini = (*ini_q, hb, l)
        f.optimize()
        f.fitted_show = f.fitted
        f.setting = model('BC')
        f.par = (*par_theta, 'h<sub>b</sub>', '&lambda;')
        f2 = copy.deepcopy(f)
        result.append(f2)

    # VG (van Genuchten) model
    a, m = f.get_init_vg()  # Get initial parameter
    f.set_model('vg', const=[*con_q, [7, 1]])
    f.ini = (*ini_q, a, m)
    f.optimize()
    q = f.fitted[:-2]
    a, m = f.fitted[-2:]
    n = 1/(1-m)
    vg_r2 = f.r2_ht
    f.fitted_show = [*f.fitted[:-1], n]  # Convert from m to n
    f.setting = model('VG')
    f.par = (*par_theta, '&alpha;', 'n')
    if not f.success:
        print(
            '<script>_delete_element("tmp"); function _delete_element( id_name ){var dom_obj = document.getElementById(id_name); var dom_obj_parent = dom_obj.parentNode; dom_obj_parent.removeChild(dom_obj);}</script>')
        print('<p><strong>Optimization failed.</strong></p>')
        f.data_only = True
        f.plot()
        print('<p><a href="{0}"></a></p>')
        showdata(f)
        return

    if 'VG' in f.selectedmodel:
        f2 = copy.deepcopy(f)
        result.append(f2)

    # KO (Kosugi) model
    if 'KO' in f.selectedmodel or 'FX' in f.selectedmodel:
        f.set_model('ln', const=[*con_q])
        f.ini = (*q, 1/a, 1.2*(n-1)**(-0.8))
        f.optimize()
        q_ko = f.fitted[:-2]
        hm, sigma = f.fitted[-2:]
        ko_r2 = f.r2_ht
        if 'KO' in f.selectedmodel:
            f.setting = model('KO')
            f.fitted_show = f.fitted
            f.par = (*par_theta, 'h<sub>m</sub>', '&sigma;')
            f2 = copy.deepcopy(f)
            result.append(f2)

    # FX (Fredlund and Xing) model
    if 'FX' in f.selectedmodel:
        f.set_model('fx', const=[*con_q])
        if vg_r2 > ko_r2:
            f.ini = (*q, 1/a, 2.54 * (1-1/n), 0.95 * n)
        else:
            f.ini = (*q_ko, hm, 2.54, 1.52 / sigma)
        f.optimize()
        f.setting = model('FX')
        f.fitted_show = f.fitted
        f.par = (*par_theta, 'a', 'm', 'n')
        f2 = copy.deepcopy(f)
        result.append(f2)

    # Bimodal model
    if any(name in f.selectedmodel for name in model('bimodal')):
        con_q, ini_q, par_theta = getoptiontheta(f, True)

    # dual-BC-CH model
    if 'DBCH' in f.selectedmodel or 'VGBCCH' in f.selectedmodel or 'DB' in f.selectedmodel:
        f.set_model('bc2', const=[*con_q])
        hb, hc, l1, l2 = f.get_init_bc2()
        f.ini = (*ini_q, hb, hc, l1, l2)  # Get initial parameter
        f.optimize()
        if not f.success:
            hb2, l = f.get_init_bc()
            f.ini = (*ini_q, hb, hb, l, l/5)
            f.optimize()
        if f.success:
            hb, hc, l1, l2 = f.fitted[-4:]
            w1 = 1/(1+(hc/hb)**(l2-l1))
            q = f.fitted[:-4]
            f.fitted_show = (*q, w1, hb, l1, l2)
        f.setting = model('DBCH')
        f.par = (*par_theta, 'w<sub>1</sub>', 'h<sub>b</sub>',
                 '&lambda;<sub>1</sub>', '&lambda;<sub>2</sub>')
        dbch = copy.deepcopy(f)
        if 'DBCH' in f.selectedmodel:
            result.append(dbch)

    # VG1BC2-CH model
    if 'VGBCCH' in f.selectedmodel:
        f.set_model('vgbcch', const=[*con_q, [9, 1]])
        if dbch.success:
            n1 = l1 + 1
            if n1 < 1.1:
                n1 = 1.1
            if n1 > 10:
                n1 = 10
            m1 = 1-1/n1
            f.ini = (*q, w1, 1/hb, m1, l2)
        else:
            f.ini = (*ini_q, 0.9, a, m, m/2)
        f.optimize()
        if f.success:
            w1, a1, m1, l2 = f.fitted[-4:]
            n1 = 1/(1-m1)
            q = f.fitted[:-4]
            f.fitted_show = (*q, w1, 1/a1, n1, l2)
        f.setting = model('VGBCCH')
        f.par = (*par_theta, 'w<sub>1</sub>', 'H', 'n', '&lambda;')
        vgbcch = copy.deepcopy(f)
        result.append(vgbcch)

    # dual-VG-CH model
    if 'DVCH' in f.selectedmodel or 'DV' in f.selectedmodel or 'DK' in f.selectedmodel:
        f.set_model('vg2ch', const=[*con_q, [9, 1]])
        w1, a, m1, m2 = f.get_init_vg2ch()  # Get initial parameter
        f.ini = (*ini_q, w1, a, m1, m2)
        f.optimize()
        if f.success:
            w1, a1, m1, m2 = f.fitted[-4:]
            q = f.fitted[:-4]
            n1 = 1/(1-m1)
            n2 = 1/(1-m2)
            f.fitted_show = (*q, w1, a1, n1, n2)
        f.setting = model('DVCH')
        f.par = (*par_theta, 'w<sub>1</sub>', '&alpha;',
                 'n<sub>1</sub>', 'n<sub>2</sub>')
        dvch = copy.deepcopy(f)
        if 'DVCH' in f.selectedmodel:
            result.append(dvch)

    # dual-BC model
    if 'DB' in f.selectedmodel:
        f.set_model('bc2f', const=[*con_q])
        if dbch.success:
            hb, hc, l1, l2 = dbch.fitted[-4:]
            w1 = 1/(1+(hc/hb)**(l2-l1))
            q = dbch.fitted[:-4]
            f.ini = (*q, w1, hb*0.9, l1, (hb*max(f.swrc[0]))**0.5, l2)
            f.optimize()
            if not f.success:
                f.ini = (*q, w1, hb*0.9, l1, hb*100, l2)
                f.optimize()
        else:
            hb, l = f.get_init_bc()
            f.ini = (*ini_q, 0.7, hb, l, hb, l)
            f.optimize()
        if f.success:
            w1, hb1, l1, hb2, l2 = f.fitted[-5:]
            q = f.fitted[:-5]
            if hb1 > hb2:
                hb1, hb2 = hb2, hb1
                l1, l2 = l2, l1
                w1 = 1-w1
                f.fitted = (*q, w1, hb1, l1, hb2, l2)
            f.fitted_show = f.fitted
        f.setting = model('DB')
        f.par = (*par_theta, 'w<sub>1</sub>', 'hb<sub>1</sub>',
                 '&lambda;<sub>1</sub>', 'hb<sub>2</sub>', '&lambda;<sub>2</sub>')
        f2 = copy.deepcopy(f)
        result.append(f2)

    # dual-VG model
    if 'DV' in f.selectedmodel or 'DK' in f.selectedmodel:
        f.set_model('vg2', const=[*con_q, [10, 1]])
        if dvch.success:
            w1, a1, m1, m2 = dvch.fitted[-4:]
            q = dvch.fitted[:-4]
            f.ini = (*q, w1, a, m1, a, m2)
            f.optimize()
            if f.success:
                w1, a1, m1, a2, m2 = f.fitted[-5:]
                q = f.fitted[:-5]
                if a1 < a2:
                    a1, a2 = a2, a1
                    m1, m2 = m2, m1
                    w1 = 1-w1
                    f.fitted = (*q, w1, a1, m1, a2, m2)
                n1 = 1/(1-m1)
                n2 = 1/(1-m2)
                f.fitted_show = (*q, w1, a1, n1, a2, n2)
            f.setting = model('DV')
            f.par = (*par_theta, 'w<sub>1</sub>', '&alpha;<sub>1</sub>',
                     'n<sub>1</sub>', '&alpha;<sub>2</sub>', 'n<sub>2</sub>')
            f2 = copy.deepcopy(f)
            if 'DV' in f.selectedmodel:
                result.append(f2)

    # dual-KO model
    if 'DK' in f.selectedmodel:
        sigmax = float(field.getfirst('sigmax', 2.5))
        if sigmax < 1:
            sigmax = 1
        f.set_model('ln2', const=[*con_q])
        if f.success:
            s1 = 1.2*(n1-1)**(-0.8)
            if s1 > sigmax * 0.8:
                s1 = sigmax * 0.8
            s2 = 1.2*(n2-1)**(-0.8)
            if s2 > sigmax * 0.8:
                s2 = sigmax * 0.8
            f.ini = (*q, w1, 1/a1, s1, 1/a2, s2)
            f.b_sigma = (0, sigmax)
            f.optimize()
            if f.success:
                w1, hm1, s1, hm2, s2 = f.fitted[-5:]
                q = f.fitted[:-5]
                if hm1 > hm2:
                    hm1, hm2 = hm2, hm1
                    s1, s2 = s2, s1
                    w1 = 1-w1
                    f.fitted = (*q, w1, hm1, s1, hm2, s2)
                f.fitted_show = f.fitted
        f.setting = model('DK')
        f.par = (*par_theta, 'w<sub>1</sub>', 'hm<sub>1</sub>',
                 '&sigma;<sub>1</sub>', 'hm<sub>2</sub>', '&sigma;<sub>2</sub>')
        f2 = copy.deepcopy(f)
        result.append(f2)

    # Show result
    error = False
    try:
        with open(IMAGEFILE, 'w') as file:
            pass
    except:
        error = True
    if error:
        print(
            '<strong>Server setup error: Cannot write {0}. Please check permission.</strong>'.format(IMAGEFILE))
    error = False
    tmpfile = WORKDIR + '/dksafjsdafkpaoeiwr'
    try:
        with open(tmpfile, 'w') as file:
            pass
    except:
        error = True
    if error:
        print(
            '<strong>Server setup error: Cannot write in {0}. Please check permission.</strong>'.format(WORKDIR))
    else:
        os.remove(tmpfile)
    print(
        '<script>_delete_element("tmp"); function _delete_element( id_name ){var dom_obj = document.getElementById(id_name); var dom_obj_parent = dom_obj.parentNode; dom_obj_parent.removeChild(dom_obj);}</script>')
    aic = []
    for i in result:
        aic.append(i.aic_ht)
    aic_min = aic.index(min(aic))
    print(
        '<table border="1">\n<tr><th>Model<th>Equation<th>Parameters<th>R<sup>2</sup><th>AIC</tr>')
    count = 0
    for i in result:
        if i.success:
            par = ''
            for j in range(len(i.par)):
                par += '{0} = {1:.5}<br>'.format(
                    i.par[j], i.fitted_show[j])
            r2 = '{0:.4f}'.format(i.r2_ht)
        else:
            par = 'Failed'
            r2 = aic = ''
        if count == aic_min:
            name = '<strong>' + i.setting['html'] + '</strong>'
            aic = '<strong>{0:.2f}</strong>'.format(i.aic_ht)
        else:
            name = i.setting['html']
            if i.success:
                aic = '{0:.2f}'.format(i.aic_ht)
        print('<tr><td>{0}<td>\\( {1} \\)<td>{2}<td>{3}<td>{4}</tr>'.format(
            name, i.setting['equation'], par, r2, aic))
        if len(i.setting['note']) > 0:
            note.append(i.setting['note'])
        f.set_model(i.model_name, i.const)
        f.fitted = i.fitted
        f.line_legend = i.setting['label']
        if i.success:
            if f.onemodel:
                if count == aic_min:
                    f.color_line = 'red'
                    f.line_style = 'solid'
                    f.plot()
            else:
                f.color_line = f.linecolors[count % len(f.linecolors)]
                f.line_style = 'dashed'
                if len(result) > count:
                    f.plot()
                else:
                    f.add_curve()
        count += 1
    print('</table>\n<ul>\n')
    for n in note:
        print('<li>{0}</li>'.format(n))
    print('</ul>\n<h2>Figure</h2>')
    if f.onemodel:
        print('<p>Showing the model with the minumim AIC value.</p>')
    showdata(f)


def showdata(f):
    print(
        '<div align="center"><img src="{0}" alt="Figure"></div>'.format(IMAGEFILE))
    print('<h2>Original data</h2><table border="1"><tr><th>h<th>&theta;')
    for i in list(zip(*f.swrc)):
        print('<tr><td>{0}<td>{1}</tr>'.format(*i))
    print('</table>')


def getoptiontheta(f, bimodal):
    """Get options for theta_s and theta_r"""
    con_q = []
    ini_q = []
    par_theta = []
    if f.cqs == 'max':
        con_q.append([1, max(f.swrc[1])])
    elif f.cqs == 'fix':
        qs = float(f.qsin)
        con_q.append([1, qs])
    else:
        ini_q.append(max(f.swrc[1]))
        par_theta.append('&theta;<sub>s</sub>')
    cqr = f.cqr
    if cqr == 'fix':
        qr = float(f.qrin)
        if qr <= 0 or qr > max(f.swrc[1]):
            qr = 0
        con_q.append([2, qr])
    if cqr == 'fit' or cqr == 'both' and not bimodal:
        ini_q.append(0)
        par_theta.append('&theta;<sub>r</sub>')
    if cqr == 'both' and bimodal:
        con_q.append([2, 0])
    return con_q, ini_q, par_theta


def printhead(lang, f):
    mathjax = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
    print(r'''<!DOCTYPE html>
<html lang="{0}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SWRC Fit</title>
  <link rel="stylesheet" type="text/css" href="{1}">
  <script id="MathJax-script" async src="{2}"></script>
  <script>
    function showMore(btn) {{
        var targetId = btn.getAttribute("href").slice(1);
        document.getElementById(targetId).style.display = "block";
        btn.parentNode.style.display = "none";
        return false;
    }}
  function a(){{'''.format(lang, message(lang, 'css'), mathjax))
    print('if(document.getElementById("sample").value == "clear"){')
    print('  document.getElementById("input").value = "";')
    print('  localStorage.removeItem("{0}");'.format(STORAGEPREFIX + 'input'))
    print('} else ', end="")
    for ID in f.sampledata:
        d = f.sampledata[ID]
        unsoda = escape(d['UNSODA'])
        text = "\\n".join(escape(d['text']).splitlines())
        print(
            'if(document.getElementById("sample").value == "{0}"){{'.format(unsoda))
        print('  document.getElementById("input").value = "{0}";'.format(text))
        print('} else ', end="")
    print('{   document.getElementById("input").value = ""; }')
    print('  }</script></head>', flush=True)


def printform(lang, getlang, f):
    url = './'
    print('<p>{0}</p>\n<h1>SWRC Fit</h1>\n<p>{1}</p>\n<form action="{2}" method="post">'.format(
        message(lang, 'langbar', url), message(lang, 'description'), url), flush=True)
    print(r'''<div align="center">
<table>
<tr>
<td width="240">
  <p>{0}</p>
'''.format(message(lang, 'modelselect')))
    for ID in model('all'):
        if model(ID)['selected']:
            checked = ' checked'
        else:
            checked = ''
        print('<INPUT TYPE="checkbox" id={0} name="{0}" value="on"{1}>{2}<br>'.format(
            ID, checked, model(ID)['html']))
    print(r'''<p>{0}<br>
  <input type="checkbox" name="onemodel" id="onemodel" value="on">{1}<br>
  </p>
</td>
<td>
<p>{2}<br>
<select name="sample" id="sample" onChange="a()">'''.format(message(lang, 'figoption'), message(lang, 'onemodel'), message(lang, 'swrc')))
    print('    <option value="">{0}'.format(message(lang, 'selectsample')))
    for ID in f.sampledata:
        d = f.sampledata[ID]
        unsoda = escape(d['UNSODA'])
        texture = escape(d['Texture'])
        print('    <option value="{0}">{1}'.format(unsoda, texture))
    print('  <option value="clear">*** Clear input ***')
    print('''  </select>
<div><textarea name="input" id="input" rows="15" cols="27" wrap="off"></textarea></div>
</td></tr>
<tr>
<td colspan="2">
<p><a href="#detail" onclick="return showMore(this);">{0}</a></p>
<div id="detail" class="detailed-options">

<p>Calculation options</p>

<ul>
<li><input type="radio" name="cqr" value="fit">Fit &theta;<sub>r</sub>
<input type="radio" name="cqr" value="fix">&theta;<sub>r</sub> = <input type="text" name="qrin" id="qrin" size="5" maxlength="10" value="0">
<input type="radio" name="cqr" value="both" checked="checked">Fit &theta;<sub>r</sub> for unimodal and &theta;<sub>r</sub> = 0 for bimodal</sub>
<li><input type="radio" name="cqs" value="fit" checked="checked">Fit &theta;<sub>s</sub>
<input type="radio" name="cqs" value="max">&theta;<sub>s</sub> = &theta;<sub>max</sub>
<input type="radio" name="cqs" value="fix">&theta;<sub>s</sub> = <input type="text" name="qsin" id="qsin" size="5" maxlength="10" value="">
<li>Maximum &sigma; for dual-KO = <input type="text" name="sigmax" id="sigmax" size="5" maxlength="10" value="2.5">
</ul>
<p>When you calculate, setting is saved in your web browser.</p>
<p><input type="submit" name="button" value="Clear setting"></p>
</div>
<p><input type="hidden" name="lang" value="{1}">\n  <div align="center"><input type="submit" name="button" value="{2}"></div>\n</form></p>
</td>
</tr>
</tr>
</table></div>'''.format(message(lang, 'showmore'), getlang, message(lang, 'calculate')), flush=True)
    # Read setting from local storage
    for i in model('all'):
        loadchecked(i)
    loadchecked('onemodel')
    loadradio('cqr', 'both')
    loadradio('cqs', 'fit')
    for i in ('qrin', 'sigmax'):
        loadnum(i)
    loadtext('input')


def loadchecked(id):
    print('''<script>
  if (localStorage.getItem("{0}{1}") == 'on') {{
    document.getElementById('{1}').checked = true;
  }};
  if (localStorage.getItem("{0}{1}") == 'off') {{
    document.getElementById('{1}').checked = false;
  }};
</script>'''.format(STORAGEPREFIX, id))


def loadradio(id, default):
    print('''<script>
    let val{1} = localStorage.getItem("{0}{1}");
    if (!val{1}) {{
        val{1} = "{2}"
    }}
    let ele{1} = document.getElementsByName("{1}");
    for (let i = 0; i < ele{1}.length; i++){{
        if (ele{1}.item(i).value == val{1}) {{
            ele{1}[i].checked = true;
        }} else {{
            ele{1}[i].checked = false;
        }}
    }}
    </script>'''.format(STORAGEPREFIX, id, default))


def loadnum(id):
    print('''<script>
  const num{1} = localStorage.getItem("{0}{1}");
  if (num{1}) {{
    document.getElementById('{1}').value = num{1};
  }}
</script>'''.format(STORAGEPREFIX, id))


def loadtext(id):
    print('''<script>
  const text = localStorage.getItem("{0}{1}");
  if (text) {{
    document.getElementById('{1}').textContent = text.replace(/\\/\\//g,'\\n');
  }}
</script>'''.format(STORAGEPREFIX, id))


def printhelp(lang, f):
    import random
    print(message(lang, 'news'))
    print(message(lang, 'format'))
    print('<h2>{0}</h2>'.format(message(lang, 'sample')))
    id = list(f.sampledata)[random.randint(0, 7)]
    texture = f.sampledata[id]['Texture']
    soil = f.sampledata[id]['Soil sample']
    print('<ul><li>{0}<li>Texture: {1}<li><a href="fig.html">List of figures</a></ul>\n<p><div align="center"><img src="img/{2}.png" alt="Sample output"></div></p>'.format(soil, texture, id))
    print(message(lang, 'help'))
    print(message(lang, 'ack'))
    print(message(lang, 'question'))


def escape(text):
    """escape html control characters

    Everything which might include input text should be escaped before output
    as html for security"""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace(
        '>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')


if __name__ == '__main__':
    main()
