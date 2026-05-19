# change lines or blocks marked with "# UPDATE:" to suit your simulations

# import of modules

import numpy as np
import matplotlib.pyplot as plt

# data extraction function

def extract(filename):
    with open(filename, 'r') as file:
        values = []
        for line in file:
            if line[0] == 'd' and line[1] == ' ':
                values.append(line[1:].split())
    for value in values:
        value[0] = float(value[0])
        for i in range(1, len(value)):
            value[i] = float(value[i])
    return values

# data processing function, index of required data and data function is to be modified manually
# 
# UPDATE:
# indecies are found in .log file, order in line starting with "p ", keys in lines starting with "Q ", it is recommended to use negative indecies
# "indx" syntax: "int" for single values, "list" with two integers for 2D vectors ("d2vec" function should be updated appropriately)

timeshift = 100030e-9       # UPDATE: time shift between simulation start and important part
indx = [-75, -57, -64, -71, -63, -70, -62, -69, -61, -68, -60, -67, -59, -66, -58, -65] # transient time (s); V(18); V4 (V); V5 (V); V6 (V); V7 (V); V8 (V); V9 (V);  V10 (V); V11 (V);  V12 (V); V13 (V);  V14 (V); V15 (V);  V16 (V); V17 (V)
d2vec = lambda x, i, j: (x[i]**2 + x[j]**2)**0.5

def full_data(values, indx):
    data = []
    for i in range(len(values)):
        lst = []
        for ix in indx:
            if type(ix) is int:
                lst.append(values[i][ix])
            elif type(ix) is list:
                if len(ix) == 2:
                    lst.append(d2vec(values[i], ix[0], ix[1]))
        data.append(lst)
    data = np.array(data)
    return data

def volt_drop(timedata, voltdata):
    rampvals = []
    for i in range(1, len(timedata) - 1):
        if voltdata[i] > 50.0:
            rampvals.append((voltdata[i - 1] - voltdata[i + 1]) / (timedata[i + 1] - timedata[i - 1]))
    return max(rampvals) * 1.0e-9

# extraction

data = []
data.append(full_data(extract("mixed_7A_prp/mixed_7A_tr.log"), indx))         # UPDATE: file path        # UPDATE: uncomment or add if multiple

# plotting

plt.plot(1e9 * (data[0][:, 0] - timeshift), -data[0][:, 1]/50, color='orange', alpha=0.6)
plt.xlim([0, 10])
plt.ylim([0, 20])
plt.grid()
plt.xlabel("Time [ns]")
plt.ylabel("Electric current [A]")
plt.savefig("mixed_7A_curr.pdf", format="pdf", bbox_inches="tight")
plt.show()

plt.plot(1e9 * (data[0][:, 0] - timeshift), (data[0][:, 3] - data[0][:, 2]), color='red', alpha=0.6, label='T1')
plt.plot(1e9 * (data[0][:, 0] - timeshift), (data[0][:, 5] - data[0][:, 4]), color='yellow', alpha=0.6, label='T2')
plt.plot(1e9 * (data[0][:, 0] - timeshift), (data[0][:, 7] - data[0][:, 6]), color='green', alpha=0.6, label='T3')
plt.plot(1e9 * (data[0][:, 0] - timeshift), (data[0][:, 9] - data[0][:, 8]), color='cyan', alpha=0.6, label='T4')
plt.plot(1e9 * (data[0][:, 0] - timeshift), (data[0][:, 11] - data[0][:, 10]), color='blue', alpha=0.6, label='T5')
plt.plot(1e9 * (data[0][:, 0] - timeshift), (data[0][:, 13] - data[0][:, 12]), color='purple', alpha=0.6, label='T6')
plt.plot(1e9 * (data[0][:, 0] - timeshift), (data[0][:, 15] - data[0][:, 14]), color='magenta', alpha=0.6, label='T7')
plt.xlim([0, 10])
plt.ylim([0, 400])
plt.grid()
plt.xlabel("Time [ns]")
plt.ylabel("Voltage [V]")
plt.legend(prop={'size': 12})
plt.savefig("mixed_7A_volt.pdf", format="pdf", bbox_inches="tight")
plt.show()
