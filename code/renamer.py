# change lines or blocks marked with "# UPDATE:" to suit your simulations

# import of required modules

import os
import numpy as np

# function definition

def round_sig(n, k):
    k = k - int(np.floor(np.log10(abs(n)))) - 1
    return round(n, k)

def extract_basic(filename):
    values = []
    with open(filename, 'r') as file:
        for line in file:
            if line[0] == 'd' and line[1] == ' ':
                values.append(line[1:].split())
    for value in values:
        value[0] = int(value[0])
        for i in range(1, len(value)):
            value[i] = float(value[i])
    return values[0]

def rename_data(filename):
    values = extract_basic(filename)
    t = round_sig(values[-1], 6)       # UPDATE: time index from the back, check rounding
    U = round_sig(values[-7], 3)       # UPDATE: voltage index from the back
    Ui = round_sig(values[-4], 3)      # UPDATE: internal voltage index from the back
    I = round_sig(values[-6], 3)       # UPDATE: current index from the back
    os.rename(filename, filename[:-4] + f'____t={t}_s____U={U}_V____Ui={Ui}_V____I={I}_A____.str')



ramps = [6, 100, 200, 400, 800, 1600, 4800, 19200, 96000]       # UPDATE: directory numeration

for ramp in ramps:
    n = 0
    while True:
        try:
            rename_data(f'ramp_{ramp}Vns_prp/ramp_{ramp}Vns_prp{n}.str')        # UPDATE: file path
        except FileNotFoundError:
            break
        n += 1
