#!/usr/bin/env python3
# This script tests the get_init() and get_wrf() functions in the models of unsatfit.
# https://sekika.github.io/unsatfit/model.html
# Laboratory drying SWRCs in the UNSODA database with 7 or more data points
# are used for testing. If the R^2 value falls below the predetermined threshold,
# the test stops. To maintain a strict criterion, some data are excluded from testing.

import argparse
import numpy as np
import pandas as pd
import random
import unsatfit
import requests
import sys

# Selection of UNSODA data
UNSODA_DATA = "https://sekika.github.io/file/unsoda/unsoda.json"
MIN_NUM_DATA = 7
EXCLUDE_ID = (1112, 1114, 1161, 1162, 1163, 1165, 1166, 1211, 1300, 1460,
              2374, 2672, 3205, 3341, 4241, 4253, 4272, 4273, 4281, 4283,
              4291, 4442, 4450, 4574, 4610, 4720)
# Models for testing and the minimum R^2 values allowed.
# See definition of DF3, DF4, DF5 models at https://doi.org/10.34428/0002000817
DF3_MODEL = ['BC', 'VG', 'KO']
DF3_MIN_R2 = (0.64, 0.86)  # Criterion for DF3 models
DF4_MODEL = ['DBC', 'DVC', 'DKC', 'VBC', 'KBC', 'FX', 'PK', 'VGFS']
DF4_MIN_R2 = (0.83, 0.90)  # Criterion for DF4 models except the followings
DBC_MIN_R2 = (0.75, 0.86)  # Criterion for dual-BC-CH model
DKC_MIN_R2 = (0.67, 0.88)  # Criterion for dual-KO-CH model
PK_MIN_R2 = (0.67, 0.72)  # Criterion for Peters model
FS_MIN_R2 = (0.12, 0.74)  # Criterion for Fayer and Simmons model
DF5_MODEL = ['DB', 'DV', 'DK', 'VB', 'KB']
DF5_MIN_R2 = (0.92, 0.93)  # Criterion for DF5 models
MODEL_WITH_VG = ['VG', 'DVC', 'VBC', 'DV',
                 'VB', 'VGFS']  # Add q=1 as constants
MODEL_WITH_HE = ['PK', 'VGFS']  # Require HE value
HE = 6.3e6  # Pressure head of zero water content for Peters and Fayer models

# Get UNSODA data
# See https://sekika.github.io/file/unsoda/
response = requests.get(UNSODA_DATA)
response.raise_for_status()
unsoda = response.json()
h_t = unsoda["lab_drying_h-t"]
ids = [int(x) for x in h_t if len(np.array(h_t[x][0]))
       >= MIN_NUM_DATA and int(x) not in EXCLUDE_ID]
parser = argparse.ArgumentParser(description="Test unsatfit models")
parser.add_argument('-i', '--id', type=int,
                    help=f'test a specific sample')
parser.add_argument('-m', '--model', type=str,
                    help=f'test a specific model')
parser.add_argument('-n', '--num', type=int, default=len(ids),
                    help=f'numbers of samples to test (default {len(ids)})')
parser.add_argument('-s', '--start', type=int,
                    help=f'start test from this sample ID')
parser.add_argument('-v', '--verbose', type=int,
                    default=1, help='verbose level (0-2, default 1)')
args = parser.parse_args()
tested = 0
random.shuffle(ids)
ids = ids[:args.num]
ids.sort()
if args.start:
    ids = [x for x in ids if x >= args.start]
if args.id:
    ids = [args.id]
models = DF3_MODEL + DF4_MODEL + DF5_MODEL
if args.model:
    models = [args.model]
for id in ids:
    tested += 1
    texture = unsoda['general'][str(id)]['texture']
    h = np.array(h_t[str(id)][0])
    theta = np.array(h_t[str(id)][1])
    f = unsatfit.Fit()
    f.swrc = (h, theta)
    f.show_fig = True
    minAIC = 99999
    if args.verbose > 1:
        print(f'======== UNSODA {id} {texture} ========')
        print(
            f'https://seki.webmasters.gr.jp/swrc/?unsoda={id}&place=lab&process=drying')
    for model in models:
        if args.verbose == 1:
            print(f'Testing UNSODA {id}\r', end='')
        if model in DF3_MODEL:
            const_ini = [[1, max(theta)], 'qr=0']
            q = [max(theta), 0]
            min_r2_init, min_r2 = DF3_MIN_R2
        if model in DF4_MODEL:
            const_ini = [[1, max(theta)], 'qr=0']
            q = [max(theta)]
            min_r2_init, min_r2 = DF4_MIN_R2
            if model == 'DBC':
                min_r2_init, min_r2 = DBC_MIN_R2
            if model == 'DKC':
                min_r2_init, min_r2 = DKC_MIN_R2
            if model == 'PK':
                min_r2_init, min_r2 = PK_MIN_R2
            if model == 'VGFS':
                min_r2_init, min_r2 = FS_MIN_R2
        if model in DF5_MODEL:
            const_ini = [[1, max(theta)], 'qr=0']
            q = [max(theta)]
            min_r2_init, min_r2 = DF5_MIN_R2
        if model in MODEL_WITH_VG:
            const_ini.append('q=1')
        if model in MODEL_WITH_HE:
            const_ini.append([6, HE])
        f.set_model(model, const=const_ini)
        if model in MODEL_WITH_HE:
            get_init = f.get_init(HE)
        else:
            get_init = f.get_init()
        f.ini = get_init
        f.optimize()
        f.data_legend = f'UNSODA {id}'
        f.line_legend = f'{model} get_init'
        f.legend_opacity = 0.7
        f.clear_curves()
        f.add_curve()
        message_ini = f'get_init(): R2 = {f.r2_ht:.5} for {f.message}'
        r2_ht_ini = f.r2_ht
        f.set_model(model, const=[])
        if model in MODEL_WITH_HE:
            get_wrf = f.get_wrf(HE)
        else:
            get_wrf = f.get_wrf()
        f.ini = get_wrf
        f.optimize()
        message_wrf = f'get_wrf(): R2 = {f.r2_ht:.5} for {f.message}'
        if not f.success or r2_ht_ini < min_r2_init or f.r2_ht < min_r2:
            stop = True
        else:
            stop = False
        if args.verbose > 1 or stop:
            if stop:
                print(f'======== UNSODA {id} {texture} ========')
                print(
                    f'https://seki.webmasters.gr.jp/swrc/?unsoda={id}&place=lab&process=drying')
            print(f'===== {model} model =====')
            formatted = f"[{', '.join(f'{x:.5g}' for x in get_init)}]"
            print(f'get_init() = {formatted}')
            print(message_ini)
            formatted = f"[{', '.join(f'{x:.5g}' for x in get_wrf)}]"
            print(f'get_wrf() = {formatted}')
            print(message_wrf)
        if stop:
            if not f.success:
                print('Test stopped becaues Optimization failed.')
            if r2_ht_ini < min_r2_init:
                print(
                    f'Test stopped because R2 for get_init() of {model} model is smaller than {min_r2_init}.')
            if f.r2_ht < min_r2:
                print(
                    f'Test stopped because R2 for get_wrf() of {model} model is smaller than {min_r2}.')
            f.line_legend = f'{model} get_wrf'
            f.plot()
            sys.exit()
if args.verbose > 0:
    print(f'Testing of get_init() and get_wrf() functions for {', '.join(models)} models using {tested} UNSODA samples was completed successfully without errors.')
