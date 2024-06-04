#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.parse
import os
import sys
import configparser
from data.message import message
from data.model import model
from data.sample import sample
from data.sample import dataset
config = configparser.ConfigParser()
config.read(os.path.dirname(__file__) + '/data/server.txt')
WORKDIR = config.get('Settings', 'workdir')
IMAGEFILE = config.get('Settings', 'imagefile')
STORAGEPREFIX = 'swrc_'
TEST_R2 = 0.945

# Default limit of parameters
MAX_QS = 1.5
MAX_LAMBDA_I = 10
MAX_N_I = 8
MIN_SIGMA_I = 0.2

os.environ['MPLCONFIGDIR'] = WORKDIR


def test(minR2, strict=False):
    import numpy as np
    import unsatfit
    f = unsatfit.Fit()
    f.test()  # Run test of unsatfit
    sampledata = sample()
    f.cqs = 'fit'
    f.cqr = 'fit'
    f.qsin = ''
    f.qrin = '0'
    f.max_qs = MAX_QS
    f.max_lambda_i = MAX_LAMBDA_I
    f.max_n_i = MAX_N_I
    f.min_sigma_i = MIN_SIGMA_I
    f.debug = False
    f.show_eq = True
    f.show_perr = False
    f.show_cor = False
    for id in sampledata:
        f.selectedmodel = model('all')
        f.b_sigma = (0, np.inf)
        d = sampledata[id]
        soil = d['Soil sample']
        texture = d['Texture']
        f.swrc = d['data']
        print(f'{soil} {texture}')
        for i in swrcfit(f):
            if not i.success:
                print(f'{i.model_name} Failed.')
                if strict:
                    exit(1)
            else:
                if i.r2_ht < minR2:
                    print(f'{i.model_name} R2 = {i.r2_ht}')
                    if strict:
                        print(f'R2 less than {minR2}')
                        exit(1)


def swrcfit(f):
    import copy
    import numpy as np
    result = []
    # Fixed parameters
    con_q, ini_q, par_theta = getoptiontheta(f, False)

    # BC (Brooks and Corey) model
    f.b_qs = b_qs = (0, max(f.swrc[1]) * f.max_qs)
    f.b_lambda1 = f.b_lambda2 = b_lambda_i = (0, f.max_lambda_i)
    f.b_m = f.b_sigma = (0, np.inf)
    max_m_i = 1 - 1/f.max_n_i

    if 'BC' in f.selectedmodel:
        f.set_model('BC', const=[*con_q])
        hb, l = f.get_init()  # Get initial parameter
        f.ini = (*ini_q, hb, l)
        f.optimize()
        if not f.success:
            f.b_qs = (0, max(f.swrc[1])*min(1.05, f.max_qs))
            f.optimize()
            f.b_qs = b_qs
            f2 = copy.deepcopy(f)
            f.ini = f.fitted
            f.optimize
            if not f.success:
                f = copy.deepcopy(f2)
        f.fitted_show = f.fitted
        f.setting = model('BC')
        f.par = (*par_theta, *f.setting['parameter'])
        f2 = copy.deepcopy(f)
        result.append(f2)

    # VG (van Genuchten) model
    f.set_model('VG', const=[*con_q, 'q=1'])
    a, m = f.get_init()  # Get initial parameter
    f.ini = (*ini_q, a, m)
    f.optimize()
    if not f.success:
        return []
    q = f.fitted[:-2]
    a, m = f.fitted[-2:]
    n = 1/(1-m)
    vg_r2 = f.r2_ht
    f.fitted_show = [*f.fitted[:-1], n]  # Convert from m to n
    f.setting = model('VG')
    if f.show_perr or f.show_cor:
        f.par = (*par_theta, *f.setting['parameter_org'])
    else:
        f.par = (*par_theta, *f.setting['parameter'])
    if 'VG' in f.selectedmodel:
        f2 = copy.deepcopy(f)
        result.append(f2)

    # KO (Kosugi) model
    if 'KO' in f.selectedmodel or 'FX' in f.selectedmodel:
        f.set_model('KO', const=[*con_q])
        sigma = 1.2*(n-1)**(-0.8)
        f.ini = (*q, 1/a, sigma)
        f.optimize()
        if not f.success or f.r2_ht < vg_r2 - 0.1:
            print(f.r2_ht, vg_r2)
            hb, l = f.get_init_bc()
            sigma = 1.2*l**(-0.8)
            if sigma > 2.5:
                sigma = 2.5
            f.ini = (*ini_q, hb, sigma)
            f.b_qs = (0, max(f.swrc[1])*min(1.05, f.max_qs))
            f.optimize()
            f.b_qs = b_qs
            f2 = copy.deepcopy(f)
            f.ini = f.fitted
            f.optimize
            if not f.success:
                f = copy.deepcopy(f2)
        q_ko = f.fitted[:-2]
        if f.success:
            hm, sigma = f.fitted[-2:]
            ko_r2 = f.r2_ht
        else:
            ko_r2 = 0
        if 'KO' in f.selectedmodel:
            f.setting = model('KO')
            f.fitted_show = f.fitted
            f.par = (*par_theta, *f.setting['parameter'])
            f2 = copy.deepcopy(f)
            result.append(f2)

    # FX (Fredlund and Xing) model
    if 'FX' in f.selectedmodel:
        f.set_model('FX', const=[*con_q])
        if vg_r2 > ko_r2:
            f.ini = (*q, 1/a, 2.54 * (1-1/n), 0.95 * n)
        else:
            f.ini = (*q_ko, hm, 2.54, 1.52 / sigma)
        f.optimize()
        if not f.success:
            hb, l = f.get_init_bc()
            n = l + 1
            a, m, n = hb, 2.54 * (1-1/n), 0.95 * n
            f.b_qs = (0, max(f.swrc[1]))
            f.b_qr = (0, min(f.swrc[1])/2)
            f.ini = (*ini_q, a, m, n)
            f.optimize()
            f.b_qs = b_qs
            f.b_qr = (0, np.inf)
            f2 = copy.deepcopy(f)
            f.ini = f.fitted
            f.optimize
            if not f.success:
                f = copy.deepcopy(f2)
        f.setting = model('FX')
        f.fitted_show = f.fitted
        f.par = (*par_theta, *f.setting['parameter'])
        f2 = copy.deepcopy(f)
        result.append(f2)

    # Bimodal model
    if any(name in f.selectedmodel for name in model('bimodal')):
        con_q, ini_q, par_theta = getoptiontheta(f, True)
    f.b_m = (0, max_m_i)

    # dual-BC-CH model
    if 'DBCH' in f.selectedmodel or 'VGBCCH' in f.selectedmodel or 'DB' in f.selectedmodel or 'KOBCCH' in f.selectedmodel:
        f.set_model('dual-BC-CH', const=[*con_q])
        hb, hc, l1, l2 = f.get_init()
        if l1 > f.max_lambda_i:
            l1 = f.max_lambda_i - 0.00001
        if l2 > f.max_lambda_i:
            l2 = f.max_lambda_i - 0.00001
        f.ini = (*ini_q, hb, hc, l1, l2)  # Get initial parameter
        f.optimize()
        if not f.success or f.r2_ht < vg_r2 - 0.05:
            hb2, l1 = f.get_init_bc()
            l2 = l/5
            if l1 > f.max_lambda_i:
                l1 = f.max_lambda_i - 0.00001
            if l2 > f.max_lambda_i:
                l2 = f.max_lambda_i - 0.00001
            f.ini = (*ini_q, hb, hb*2, l1, l2)
            f.optimize()
            if not f.success:
                f.b_qs = (max(f.swrc[1]) * 0.9, max(f.swrc[1]))
                f.b_qr = (0, min(f.swrc[1])/100)
                f.b_lambda1 = f.b_lambda2 = (0, l*1.5)
                f.ini = (*ini_q, hb, hb, l, l)
                f.optimize()
                f.b_qs = b_qs
                f.b_qr = (0, np.inf)
                f.b_lambda1 = f.b_lambda2 = b_lambda_i
            f2 = copy.deepcopy(f)
            f.ini = f.fitted
            f.optimize
            if not f.success:
                f = copy.deepcopy(f2)
        if f.success:
            hb, hc, l1, l2 = f.fitted[-4:]
            w1 = 1/(1+(hc/hb)**(l2-l1))
            q = f.fitted[:-4]
            f.fitted_show = (*q, w1, hb, l1, l2)
        f.setting = model('DBCH')
        if f.show_perr or f.show_cor:
            f.par = (*par_theta, *f.setting['parameter_org'])
            f.setting['equation'] = f.setting['equation_conv']
        else:
            f.par = (*par_theta, *f.setting['parameter'])
        dbch = copy.deepcopy(f)
        if 'DBCH' in f.selectedmodel:
            result.append(dbch)

    # VG1BC2-CH model
    if 'VGBCCH' in f.selectedmodel:
        f.set_model('VG1BC2-CH', const=[*con_q, 'q=1'])
        if dbch.success:
            n1 = l1 + 1
            m1 = 1-1/n1
            if m1 < 0.1:
                m1 = 0.1
            if m1 > 0.8:
                m1 = 0.8
            f.ini = (*q, w1, 1/hb, m1, l2)
            f.optimize()
            if not f.success:
                f.b_qs = (max(f.swrc[1]) * 0.95,
                          max(f.swrc[1]) * min(1.05, f.max_qs))
                f.b_qr = (0, min(f.swrc[1]) / 10)
                f.ini = (*ini_q, w1, 1/hb, m, l2)
                f.optimize()
                if not f.success:
                    f.ini = (*ini_q, 0.9, 1/hb, m, l2)
                    f.b_lambda2 = (l2 * 0.8, l2 * 1.2)
                    f.optimize()
                f.b_qs = b_qs
                f.b_qr = (0, np.inf)
                f.b_lambda2 = b_lambda_i
                f2 = copy.deepcopy(f)
                f.ini = f.fitted
                f.optimize
                if not f.success:
                    f = copy.deepcopy(f2)
        else:
            f.ini = (*ini_q, 0.9, a, m, m/2)
            f.optimize()
        if f.success:
            w1, a1, m1, l2 = f.fitted[-4:]
            n1 = 1/(1-m1)
            q = f.fitted[:-4]
            f.fitted_show = (*q, w1, 1/a1, n1, l2)
        f.setting = model('VGBCCH')
        if f.show_perr or f.show_cor:
            f.par = (*par_theta, *f.setting['parameter_org'])
        else:
            f.par = (*par_theta, *f.setting['parameter'])
        vgbcch = copy.deepcopy(f)
        result.append(vgbcch)

    # dual-VG-CH model
    if 'DVCH' in f.selectedmodel:
        f.set_model('dual-VG-CH', const=[*con_q, 'q=1'])
        w1, a, m1, m2 = f.get_init()  # Get initial parameter
        if m1 > max_m_i:
            m1 = max_m_i - 0.0001
        if m2 > max_m_i:
            m2 = max_m_i - 0.0001
        f.ini = (*ini_q, w1, a, m1, m2)
        f.optimize()
        if not f.success:
            f.b_qs = (max(f.swrc[1]) * 0.95,
                      max(f.swrc[1]) * min(1.05, f.max_qs))
            f.b_m = (0, 0.9)
            a, m = f.get_init_vg()
            if m > 0.9:
                m = 0.9
            f.ini = (*ini_q, 0.5, a, m, m)
            f.optimize()
            f.b_qs = b_qs
            f.b_m = (0, max_m_i)
            f2 = copy.deepcopy(f)
            f.ini = f.fitted
            f.optimize
            if not f.success:
                f = copy.deepcopy(f2)
        if f.success:
            w1, a1, m1, m2 = f.fitted[-4:]
            q = f.fitted[:-4]
            n1 = 1/(1-m1)
            n2 = 1/(1-m2)
            f.fitted_show = (*q, w1, a1, n1, n2)
        f.setting = model('DVCH')
        if f.show_perr or f.show_cor:
            f.par = (*par_theta, *f.setting['parameter_org'])
        else:
            f.par = (*par_theta, *f.setting['parameter'])
        dvch = copy.deepcopy(f)
        if 'DVCH' in f.selectedmodel:
            result.append(dvch)

    # KO1BC2-CH model
    if 'KOBCCH' in f.selectedmodel:
        f.set_model('KO1BC2-CH', const=[*con_q])
        f.b_sigma = (f.min_sigma_i, np.inf)
        if dbch.success:
            s1 = 1.2*l1**(-0.8)
            if s1 > 2:
                s1 = 2
            if s1 < f.min_sigma_i:
                s1 = f.min_sigma_i + 0.00001
            if l2 > f.max_lambda_i:
                l2 = f.max_lambda_i - 0.00001
            f.ini = (*q, w1, hb, s1, l2)
            f.optimize()
            if not f.success:
                f.b_qs = (max(f.swrc[1]) * 0.95,
                          max(f.swrc[1]) * min(1.05, f.max_qs))
                f.b_qr = (0, min(f.swrc[1]) / 10)
                f.ini = (*ini_q, w1, hb, s1, l2)
                if s1 < f.min_sigma_i:
                    s1 = f.min_sigma_i + 0.00001
                if l2 > f.max_lambda_i:
                    l2 = f.max_lambda_i - 0.00001
                f.optimize()
                if not f.success:
                    f.ini = (*ini_q, 0.9, hb, s1, l2)
                    f.b_lambda2 = (l2 * 0.8, min(l2 * 1.2, f.max_lambda_i))
                    f.optimize()
                f.b_qs = b_qs
                f.b_qr = (0, np.inf)
                f.b_lambda2 = b_lambda_i
                f2 = copy.deepcopy(f)
                f.ini = f.fitted
                f.optimize
                if not f.success:
                    f = copy.deepcopy(f2)
        else:
            w1, hm, sigma1, l2 = f.get_init_kobcch()
            if l2 > f.max_lambda_i:
                l2 = f.max_lambda_i - 0.00001
            f.ini = (*ini_q, w1, hm, sigma1, l2)
            f.optimize()
        if f.success:
            w1, hm, s1, l2 = f.fitted[-4:]
            q = f.fitted[:-4]
            f.fitted_show = (*q, w1, hm, s1, l2)
        f.setting = model('KOBCCH')
        f.par = (*par_theta, *f.setting['parameter'])
        vgbcch = copy.deepcopy(f)
        result.append(vgbcch)

    # dual-BC model
    if 'DB' in f.selectedmodel:
        f.set_model('dual-BC', const=[*con_q])
        if dbch.success:
            hb, hc, l1, l2 = dbch.fitted[-4:]
            w1 = 1/(1+(hc/hb)**(l2-l1))
            q = dbch.fitted[:-4]
            f.ini = (*ini_q, w1, hb*0.9, l1, (hb*max(f.swrc[0]))**0.5, l2)
            f.b_qs = (max(f.swrc[1]) * 0.95,
                      max(f.swrc[1]) * min(1.05, f.max_qs))
            f.optimize()
            if not f.success:
                f.b_qr = (0, min(f.swrc[1]) / 10)
                f.ini = (*ini_q, w1, hb*0.9, l1, hb*1.1, l2)
                f.optimize()
                if not f.success:
                    hb, l = f.get_init_bc()
                    if l > f.max_lambda_i:
                        l = f.max_lambda_i - 0.00001
                    f.b_lambda1 = f.b_lambda2 = (
                        0, min(l * 1.1, f.max_lambda_i))
                    f.ini = (*ini_q, 0.7, hb, l, hb, l)
                    f.optimize()
                f.b_qr = (0, np.inf)
                f.b_lambda1 = f.b_lambda2 = b_lambda_i
                f2 = copy.deepcopy(f)
                f.ini = f.fitted
                f.optimize
                if not f.success or f.r2_ht < f2.r2_ht:
                    f = copy.deepcopy(f2)
            f.b_qs = b_qs
            f2 = copy.deepcopy(f)
            f.ini = f.fitted
            f.optimize
            if not f.success or f.r2_ht < f2.r2_ht:
                f = copy.deepcopy(f2)
        else:
            hb, l = f.get_init_bc()
            if l > f.max_lambda_i:
                l = f.max_lambda_i - 0.00001
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
        f.par = (*par_theta, *f.setting['parameter'])
        f2 = copy.deepcopy(f)
        result.append(f2)

    # dual-VG model
    if 'DV' in f.selectedmodel or 'DK' in f.selectedmodel:
        f.set_model('dual-VG', const=[*con_q, 'q=1'])
        w1, a1, m1, a2, m2 = init_vg2 = f.get_init_vg2()
        if m1 > max_m_i:
            m1 = max_m_i - 0.0001
        if m2 > max_m_i:
            m2 = max_m_i - 0.0001
        f.ini = (*ini_q, w1, a1, m1, a2, m2)
        f.optimize()
        vg2_r2 = 0
        if f.success:
            vg2_r2 = f.r2_ht
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
        if f.show_perr or f.show_cor:
            f.par = (*par_theta, *f.setting['parameter_org'])
        else:
            f.par = (*par_theta, *f.setting['parameter'])
        f2 = copy.deepcopy(f)
        if 'DV' in f.selectedmodel:
            result.append(f2)

    # dual-KO model
    if 'DK' in f.selectedmodel:
        if f.success:
            if n1 < 1.4:
                n1 = 1.4
            s1 = 1.2*(n1-1)**(-0.8)
            if s1 < f.min_sigma_i:
                s1 = f.min_sigma_i + 0.00001
            if n2 < 1.4:
                n2 = 1.4
            s2 = 1.2*(n2-1)**(-0.8)
            if s2 < f.min_sigma_i:
                s2 = f.min_sigma_i + 0.00001
            if s2 > 2:
                s2 = 2
            hm1 = 1/a1
            hm2 = 1/a2
            f.set_model('dual-KO', const=[*con_q])
            f.b_w1 = (max(w1 * 0.5, w1-0.15), min(w1+0.15, 1-(1-w1)*0.5))
            f.b_hm1 = (hm1 / 8, hm1 * 8)
            f.b_hm2 = (min(max(f.swrc[0])*0.5, hm2 / 8), hm2 * 8)
            f.b_sigma = (f.min_sigma_i, 2.5)
            f.ini = (*q, w1, hm1, s1, hm2, s2)
            f.optimize()
            f.b_w1 = (0, 1)
            f.b_hm1 = f.b_hm2 = (0, np.inf)
            if not f.success or f.r2_ht < vg2_r2 - 0.05:
                f.b_qs = (max(f.swrc[1]) * 0.95,
                          max(f.swrc[1]) * min(1.05, f.max_qs))
                f.b_qr = (0, min(f.swrc[1]) / 10)
                f.ini = (*ini_q, w1, 1/a1, s1, 1/a2, s2)
                f.optimize()
                if not f.success:
                    a, m = f.get_init_vg()
                    n = 1/(1-m)
                    if n < 1.4:
                        n = 1.4
                    s = 1.2*(n-1)**(-0.8)
                    f.ini = (*ini_q, 0.5, 1/a, s, 1/a, s)
                    f.optimize()
                f.b_qs = b_qs
                f.b_qr = (0, np.inf)
                f2 = copy.deepcopy(f)
                f.ini = f.fitted
                f.optimize()
                if not f.success:
                    f = copy.deepcopy(f2)
            f.b_sigma = (f.min_sigma_i, np.inf)
            f2 = copy.deepcopy(f)
            f.ini = f.fitted
            f.optimize()
            if not f.success or f.r2_ht < f2.r2_ht:
                f = copy.deepcopy(f2)
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
        f.par = (*par_theta, *f.setting['parameter'])
        f2 = copy.deepcopy(f)
        result.append(f2)
    return result


def main():
    """Determine if it is invoked as cgi or command line
    """
    if os.getenv('SCRIPT_NAME') is None:
        maincl()
    else:
        maincgi()


def maincl():
    import argparse
    parser = argparse.ArgumentParser(description='SWRC Fit in command line')
    parser.add_argument('-c', '--cgi', action='store_true',
                        help='run as cgi')
    parser.add_argument('-t', '--test', action='store_true',
                        help='run test')
    args = parser.parse_args()
    if args.cgi:
        maincgi()
        return
    if args.test:
        test(TEST_R2, strict=True)
        return
    parser.print_help()


# Since the cgi module is deprecated as of Python 3.11 (PEP 594),
# get_field_storage() was defined as an alternative to the cgi module.
# The line field = cgi.FieldStorage() is replaced with
# field = get_field_storage(), and the field.getfirst method
# functions in the same way.
class FieldStorage:
    def __init__(self, form_data):
        self.form_data = form_data

    def getfirst(self, key, default=''):
        """ Get first value of the key """
        return self.form_data.get(key, [default])[0]


def get_field_storage():
    method = os.environ.get('REQUEST_METHOD', 'GET').upper()

    if method == 'POST':
        content_type = os.environ.get('CONTENT_TYPE', '')
        content_length = int(os.environ.get('CONTENT_LENGTH', 0))
        if content_length > 0 and content_type == 'application/x-www-form-urlencoded':
            post_data = sys.stdin.read(content_length)
            form_data = urllib.parse.parse_qs(post_data, keep_blank_values=1)
        else:
            form_data = {}
    else:
        query_string = os.environ.get('QUERY_STRING', '')
        form_data = urllib.parse.parse_qs(query_string, keep_blank_values=1)

    return FieldStorage(form_data)


def maincgi():
    """SWRC Fit to run as CGI"""
    from io import TextIOWrapper
    import unsatfit
    f = unsatfit.Fit()

    # Change encoding of stdout to utf-8
    # It is required becaue CGI script runs as another user and may not
    # print utf-8 encoded text
    sys.stdout = TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # Respond HTTP header
    print('Content-Type: text/html')
    print('Cache-Control: public\n')

    # Get input strings
    # field = cgi.FieldStorage() was replaced to the following line
    field = get_field_storage()
    getlang = field.getfirst('lang', 'none')
    f.inputtext = field.getfirst('input', '')

    # Get language setting
    LANGUAGES = message('', 'list')
    lang = os.getenv('HTTP_ACCEPT_LANGUAGE')
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

    # Get UNSODA data
    code = field.getfirst('unsoda', '')
    f.given_data = ''
    if code != '':
        import json
        place = field.getfirst('place', '')
        process = field.getfirst('process', '')
        table = place + '_' + process + '_h-t'
        unsoda_json = json.load(open('data/unsoda.json', 'r'))
        if table in unsoda_json and code in unsoda_json[table]:
            s = unsoda_json[table][code]
            f.given_data = 'UNSODA = ' + str(code)
            f.given_data += '\nTexture = ' + \
                unsoda_json['general'][code]['texture'] + '\n\n'
            for i in [list(x) for x in zip(*s)]:
                f.given_data += str(i[0]) + ' ' + str(i[1]) + '\n'
    # Get model selection
    f.selectedmodel = []
    for m in model('all'):
        if field.getfirst(m, '') == 'on':
            f.selectedmodel.append(m)
    f.onemodel = (field.getfirst('onemodel', '') == 'on')

    # Output options
    f.show_eq = (field.getfirst('show_eq', '') == 'on')
    f.show_perr = (field.getfirst('show_perr', '') == 'on')
    f.show_cor = (field.getfirst('show_cor', '') == 'on')

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

    f.sampledata = sample()
    printhead(lang, f)
    print('<body>')
    d = dataset(f.inputtext)

    if field.getfirst('button') == 'Clear setting':
        # Clear field storage
        for i in model('savekeys'):
            key = STORAGEPREFIX + i
            print(f'<script>localStorage.removeItem("{key}");</script>')
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
                f'<p><strong>{error}</strong></p><p>{message(lang, "readformat")}</p>')
            printhelp(lang, f)
        else:
            f.swrc = h, theta = d['data']  # Data of soil water retention
            f.data = d
            # Get options
            f.cqs = field.getfirst('cqs', '')
            f.cqr = field.getfirst('cqr', '')
            f.qsin = field.getfirst('qsin', str(max(theta)))
            f.qrin = field.getfirst('qrin', '')
            f.max_qs = getfloat(field, 'max_qs', MAX_QS, 1.00001)
            f.max_lambda_i = getfloat(field, 'max_lambda_i', MAX_LAMBDA_I, 0.5)
            f.max_n_i = getfloat(field, 'max_n_i', MAX_N_I, 1.5)
            f.min_sigma_i = getfloat(field, 'min_sigma_i', MIN_SIGMA_I, 0)
            if f.min_sigma_i > 1:
                f.min_sigma_i = 1
            # Save field storage to local storage
            for i in model('savekeys'):
                value = '//'.join(field.getfirst(i, 'off').splitlines())
                if i in ('qsin', 'qrin') + model('limit'):
                    try:
                        value = float(value)
                    except ValueError:
                        value = -99
                    if value == int(value):
                        value = int(value)
                    if value == -99:
                        if i == 'qsin':
                            value = ''
                        if i == 'qrin':
                            value = 0
                        if i == 'max_qs':
                            value = MAX_QS
                        if i == 'max_lambda_i':
                            value = MAX_LAMBDA_I
                        if i == 'max_n_i':
                            value = MAX_N_I
                        if i == 'min_sigma_i':
                            value = MIN_SIGMA_I
                    else:
                        if value <= 0:
                            value = 0
                    if i == 'max_qs' and value < 1:
                        value = 1
                    if i == 'max_lambda_i' and value < 0.5:
                        value = 0.5
                    if i == 'max_n_i' and value < 1.5:
                        value = 1.5
                    if i == 'min_sigma_i' and value < 0:
                        value = 0
                    if i == 'min_sigma_i' and value > 1:
                        value = 1
                    value = str(value)
                key = STORAGEPREFIX + i
                print(
                    f'<script>localStorage.setItem("{key}", "{value}");</script>')
            calc(f)   # Start main calculation
    # Print footer
    import platform
    footer = message(lang, "footer")
    footer = footer.replace('VER', f.version())
    footer = footer.replace('AUTHOR', message(lang, 'author'))
    pyver = str(sys.version_info.major) + '.' + \
        str(sys.version_info.minor) + '.' + str(sys.version_info.micro)
    footer = footer.replace('PYV', pyver).replace('ARCH', platform.system())
    print(f'<hr>\n<p>{footer}</p>\n<p style="text-align:right;"><img src="https://seki.webmasters.gr.jp/swrc/npc.cgi?L=http://purl.org/net/swrc/" alt="counter"></p></body></html>', flush=True)
    return


def getfloat(field, id, default, min):
    value = field.getfirst(id, 'a')
    try:
        value = float(value)
    except ValueError:
        value = default
    if value < min:
        value = min
    if value == int(value):
        value = int(value)
    return value


def calc(f):
    """Main calculation"""
    lang = f.lang
    getlang = f.getlang
    d = f.data
    # Show process
    if getlang in message('', 'list'):
        url = './?lang='+lang
    else:
        url = './'
    print(
        f'<h1><a href="{url}">SWRC Fit</a> - {message(lang, "result")}</h1>')
    print('<ul>')
    for i in sorted(d):
        if i not in ['empty', 'valid', 'text', 'data']:
            if i == 'doi':
                print(
                    f'<li>{escape(i)} = <a href="https://doi.org/{1}">{escape(d[i])}</a>')
            elif i == 'UNSODA':
                print(
                    f'<li>{escape(i)} = <a href="https://sekika.github.io/unsoda/?{escape(d[i])}">{escape(d[i])}</a>')
            else:
                print(f'<li>{escape(i)} = {escape(d[i])}')
    for i in getoptiontheta(f, True)[0]:
        bi = ''
        if f.cqr == 'both' and i[0] == 2:
            bi = ' for bimodal models'
        par = ('&theta;<sub>s</sub>', '&theta;<sub>r</sub>')[i[0]-1]
        print(f'<li>Constant: {par} = {i[1]}{bi}')
    limit = []
    if f.cqs == 'fit':
        limit.append(
            f'&theta;<sub>s</sub> &lt; {f.max_qs * max(d["data"][1]):.3f}')
    if 'DBCH' in f.selectedmodel or 'DB' in f.selectedmodel:
        limit.append(f'&lambda;<sub>1</sub> &lt; {f.max_lambda_i}')
    if 'VGBCCH' in f.selectedmodel or 'DVCH' in f.selectedmodel or 'DV' in f.selectedmodel:
        limit.append(f'n<sub>1</sub> &lt; {f.max_n_i}')
    if 'KOBCCH' in f.selectedmodel or 'DK' in f.selectedmodel:
        limit.append(f'&sigma;<sub>1</sub> &gt; {f.min_sigma_i}')
    if 'DBCH' in f.selectedmodel or 'DB' in f.selectedmodel or 'VGBCCH' in f.selectedmodel or 'KOBCCH' in f.selectedmodel:
        limit.append(f'&lambda;<sub>2</sub> &lt; {f.max_lambda_i}')
    if 'DVCH' in f.selectedmodel or 'DV' in f.selectedmodel:
        limit.append(f'n<sub>2</sub> &lt; {f.max_n_i}')
    if 'DK' in f.selectedmodel:
        limit.append(f'&sigma;<sub>2</sub> &gt; {f.min_sigma_i}')
    if len(limit) > 0:
        print('<li>Limit: ' + ', '.join(limit))
    print('</ul>')
    print(
        f'<div class="tmp" id="tmp">{message(lang, "wait")}</div>', flush=True)
    result = swrcfit(f)  # Calculation
    if len(result) == 0:
        print(
            '<script>_delete_element("tmp"); function _delete_element( id_name ){var dom_obj = document.getElementById(id_name); var dom_obj_parent = dom_obj.parentNode; dom_obj_parent.removeChild(dom_obj);}</script>')
        print('<p><strong>Optimization failed.</strong></p>')
        f.data_only = True
        f.plot()
        print('<p><a href="{0}"></a></p>')
        showdata(f)
        return
    # Show result
    # Note
    note = [
        'The model with minumum AIC is shown in red color. AIC (<a href="https://en.wikipedia.org/wiki/Akaike_information_criterion">Akaike Information Criterion</a>) = n ln(RSS/n)+2k, where n is sample size, RSS is residual sum of squares and k is the number of estimated parameters.']
    note.append(
        'Effective saturation \\(S_e = \\frac{\\theta-\\theta_r}{\\theta_s-\\theta_r}\\). Therefore &theta; = &theta;<sub>r</sub> + (&theta;<sub>s</sub>-&theta;<sub>r</sub>)S<sub>e</sub>.')
    if f.show_perr:
        note.append(
            '&pm; shows 1&sigma; uncertainty of parameters.')

    error = False
    try:
        with open(IMAGEFILE, 'w') as file:
            pass
    except:
        error = True
    if error:
        print(
            f'<strong>Server setup error: Cannot write {IMAGEFILE}. Please check permission.</strong>')
    error = False
    tmpfile = WORKDIR + '/dksafjsdafkpaoeiwr'
    try:
        with open(tmpfile, 'w') as file:
            pass
    except:
        error = True
    if error:
        print(
            f'<strong>Server setup error: Cannot write in {WORKDIR}. Please check permission.</strong>')
    else:
        os.remove(tmpfile)
    print(
        '<script>_delete_element("tmp"); function _delete_element( id_name ){var dom_obj = document.getElementById(id_name); var dom_obj_parent = dom_obj.parentNode; dom_obj_parent.removeChild(dom_obj);}</script>')
    aic = []
    for i in result:
        if i.success:
            aic.append(i.aic_ht)
        else:
            aic.append(99999)
    aic_min = aic.index(min(aic))
    if f.show_eq:
        eq = '<th>Equation'
    else:
        eq = ''
    if f.show_cor:
        cor = '<th>Correlation matrix'
    else:
        cor = ''
    print(
        f'<table border="1">\n<tr><th>Model{eq}<th>Parameters{cor}<th>R<sup>2</sup><th>AIC</tr>')
    count = 0
    for i in result:
        if i.success:
            par = ''
            for j in range(len(i.par)):
                if f.show_perr:
                    p = f'{i.fitted[j]:.5}'
                    if i.perr is not None:
                        p += f' &pm; {i.perr[j]:.3}'
                elif f.show_cor:
                    p = f'{i.fitted[j]:.5}'
                else:
                    p = f'{i.fitted_show[j]:.5}'
                par += f'{i.par[j]} = {p}<br>'
            r2 = f'{i.r2_ht:.4f}'
        else:
            par = 'Failed'
            r2 = aic = ''
        if count == aic_min:
            name = '<strong>' + i.setting['html'] + '</strong>'
            aic = f'<strong>{i.aic_ht:.2f}</strong>'
        else:
            name = i.setting['html']
            if i.success:
                aic = f'{i.aic_ht:.2f}'
        if f.show_eq:
            eq = f'<td>\\( {i.setting["equation"]} \\)'
        else:
            eq = ''
        if f.show_cor:
            if i.cor is None:
                cor = 'Not available'
            else:
                cor = "<br>".join(" ".join(f"{num:+.3f}".replace("+", "&nbsp;") for num in row) for row in i.cor)
            cor = f'<td>{cor}'
        else:
            cor = ''
        print(
            f'<tr><td>{name}{eq}<td>{par}{cor}<td>{r2}<td>{aic}</tr>')
        if len(i.setting['note']) > 0:
            note.append(i.setting['note'])
        f.set_model(i.model_name, i.const)
        f.fitted = i.fitted
        f.line_legend = i.setting['label']
        if i.success:
            if f.onemodel:
                if count == aic_min:
                    f.plot()
            else:
                if len(result) > count:
                    f.plot()
                else:
                    f.add_curve()
        count += 1
    print('</table>\n<ul>\n')
    for n in note:
        print(f'<li>{n}</li>')
    print('</ul>\n<h2>Figure</h2>')
    if f.onemodel:
        print('<p>Showing the model with the minumim AIC value.</p>')
    showdata(f)


def showdata(f):
    print(
        f'<div align="center"><img src="{IMAGEFILE}" alt="Figure"></div>')
    print('<h2>Original data</h2><table border="1"><tr><th>h<th>&theta;')
    for i in list(zip(*f.swrc)):
        print(f'<tr><td>{i[0]}<td>{i[1]}</tr>')
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
    print(f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SWRC Fit</title>
  <link rel="stylesheet" type="text/css" href="{message(lang, "css")}">
  <script id="MathJax-script" async src="{mathjax}"></script>
  <script>
    function showMore(btn) {{
        var targetId = btn.getAttribute("href").slice(1);
        document.getElementById(targetId).style.display = "block";
        btn.parentNode.style.display = "none";
        return false;
    }}
  function a(){{''')
    print('if(document.getElementById("sample").value == "clear"){')
    print('  document.getElementById("input").value = "";')
    print(f"  localStorage.removeItem('{STORAGEPREFIX + 'input'}');")
    print('} else ', end="")
    for ID in f.sampledata:
        d = f.sampledata[ID]
        unsoda = escape(d['UNSODA'])
        text = "\\n".join(escape(d['text']).splitlines())
        print(
            f'if(document.getElementById("sample").value == "{unsoda}"){{')
        print(f'  document.getElementById("input").value = "{text}";')
        print('} else ', end="")
    print('{   document.getElementById("input").value = ""; }')
    print('  }</script></head>', flush=True)


def printform(lang, getlang, f):
    url = './'
    print(f'<p>{message(lang, "langbar", url)}</p>\n<h1>SWRC Fit</h1>\n<p>{message(lang, "description")}</p>\n<form action="{url}" method="post">', flush=True)
    print(f'''<div align="center">
<table>
<tr>
<td width="240">
  <p>{message(lang, "modelselect")}</p>
''')
    for ID in model('all'):
        if model(ID)['selected']:
            checked = ' checked'
        else:
            checked = ''
        print('<INPUT TYPE="checkbox" id={0} name="{0}" value="on"{1}>{2}<br>'.format(
            ID, checked, model(ID)['html']))
    print(f'''<p>{message(lang, "figoption")}<br>
  <input type="checkbox" name="onemodel" id="onemodel" value="on">{message(lang, "onemodel")}<br>
  </p>
</td>
<td>
<p>{message(lang, "swrc")}<br>
<select name="sample" id="sample" onChange="a()">''')
    print(f'    <option value="">{message(lang, "selectsample")}')
    for ID in f.sampledata:
        d = f.sampledata[ID]
        unsoda = escape(d['UNSODA'])
        texture = escape(d['Texture'])
        print(f'    <option value="{unsoda}">{texture}')
    print('  <option value="clear">*** Clear input ***')
    print(f'''  </select>
<div><textarea name="input" id="input" rows="15" cols="27" wrap="off">{f.given_data}</textarea></div>
</td></tr>
<tr>
<td colspan="2">
<p><a href="#detail" onclick="return showMore(this);">{message(lang, 'showmore')}</a></p>
<div id="detail" class="detailed-options">

<p>Calculation options</p>

<ul>
<li><input type="radio" name="cqr" value="fit">Fit &theta;<sub>r</sub>
<input type="radio" name="cqr" value="fix">&theta;<sub>r</sub> = <input type="text" name="qrin" id="qrin" size="5" maxlength="10" value="0">
<input type="radio" name="cqr" value="both" checked="checked">Fit &theta;<sub>r</sub> for unimodal and &theta;<sub>r</sub> = 0 for bimodal</sub>
<li><input type="radio" name="cqs" value="fit" checked="checked">Fit &theta;<sub>s</sub>
<input type="radio" name="cqs" value="max">&theta;<sub>s</sub> = &theta;<sub>max</sub>
<input type="radio" name="cqs" value="fix">&theta;<sub>s</sub> = <input type="text" name="qsin" id="qsin" size="5" maxlength="10" value="">
<li>Upper limit of &theta;<sub>s</sub> / &theta;<sub>max</sub> = <input type="text" name="max_qs" id="max_qs" size="5" maxlength="10" value="{MAX_QS}">
<li>Upper limit of &lambda;<sub>1</sub>, &lambda;<sub>2</sub> = <input type="text" name="max_lambda_i" id="max_lambda_i" size="5" maxlength="10" value="{MAX_LAMBDA_I}">
<li>Upper limit of n<sub>1</sub>, n<sub>2</sub> = <input type="text" name="max_n_i" id="max_n_i" size="5" maxlength="10" value="{MAX_N_I}">
<li>Lower limit of &sigma;<sub>1</sub>, &sigma;<sub>2</sub> = <input type="text" name="min_sigma_i" id="min_sigma_i" size="5" maxlength="10" value="{MIN_SIGMA_I}">
</ul>
<p><strong>[New]</strong> Output options</p>
<input type="checkbox" name="show_eq" id="show_eq" value="on" checked>Equation<br>
<input type="checkbox" name="show_perr" id="show_perr" value="on">1&sigma; uncertainty of parameters<br>
<input type="checkbox" name="show_cor" id="show_cor" value="on">Correlation matrix<br>

<p>When you calculate, setting is saved in your web browser.</p>
<p><input type="submit" name="button" value="Clear setting"></p>
</div>
<p><input type="hidden" name="lang" value="{getlang}">\n  <div align="center"><input type="submit" name="button" value="{message(lang, 'calculate')}"></div>\n</form></p>
</td>
</tr>
</tr>
</table></div>''', flush=True)
    # Read setting from local storage
    for i in model('all'):
        loadchecked(i)
    loadchecked('onemodel')
    loadchecked('show_eq')
    loadchecked('show_perr')
    loadchecked('show_cor')
    loadradio('cqr', 'both')
    loadradio('cqs', 'fit')
    for i in ('qrin',) + model('limit'):
        loadnum(i)
    if f.given_data == '':
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
    print(f'<h2>{message(lang, "sample")}</h2>')
    id = list(f.sampledata)[random.randint(0, 7)]
    texture = f.sampledata[id]['Texture']
    soil = f.sampledata[id]['Soil sample']
    print(f'<ul><li>{soil}<li>Texture: {texture}<li><a href="fig.html">List of figures</a></ul>\n<p><div align="center"><img src="img/{id}.png" alt="Sample output"></div></p>')
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
