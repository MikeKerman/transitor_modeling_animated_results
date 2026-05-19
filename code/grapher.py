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
        value[0] = int(value[0])
        for i in range(1, len(value)):
            value[i] = float(value[i])
    return values

# data processing function, index of required data and data function is to be modified manually
# 
# UPDATE:
# indecies are found in .log file, order in line starting with "p ", keys in lines starting with "Q ", it is recommended to use negative indecies
# "indx" syntax: "int" for single values, "list" with two integers for 2D vectors ("d2vec" function should be updated appropriately)

timeshift = 100e-9       # UPDATE: time shift between simulation start and important part
indx = [-1, -4, -3, -2] # transient time (s); collector voltage (V); collector internal voltage (V); collector current (A)
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

def char_time(timedata, ramp):
    chartimedata = []
    for i in range(len(timedata)):
        chartimedata.append((timedata[i] - timeshift) * ramp * 1.0e9)
    return np.array(chartimedata)

def volt_drop(timedata, voltdata):
    rampvals = []
    for i in range(1, len(timedata) - 1):
        if voltdata[i] > 50.0:
            rampvals.append((voltdata[i - 1] - voltdata[i + 1]) / (timedata[i + 1] - timedata[i - 1]))
    return max(rampvals) * 1.0e-9

# extraction

data = []
ramps = [6, 100, 200, 400, 800, 1600, 4800, 19200, 96000]       # UPDATE: directory numeration

for ramp in ramps:
    data.append(full_data(extract(f"ramp_{ramp}Vns_prp/ramp_{ramp}Vns_prp.log"), indx))         # UPDATE: file path        # UPDATE: uncomment or add if multiple

# plotting

stls = ['-', '-', '-', '-', '-', '-', '-', '-', '-']          # UPDATE: add or change line styles
clrs = ['red', 'orange', 'yellow', 'lime', 'green', 'cyan', 'blue', 'purple', 'magenta']                    # UPDATE: add or change colors
lbls = ['6Vns', '100Vns', '200Vns', '400Vns', '800Vns', '1600Vns', '4800Vns', '19200Vns', '96000Vns']       # UPDATE: add or change labels

vltlst = []
rmprat = []
for i in range(len(data)):
    plt.plot(char_time(data[i][:, 0], (2 * ramps)[i]), 570*data[i][:, 3], stls[i], color=clrs[i], alpha=0.6, label=lbls[i])
    vltlst.append(volt_drop(data[i][:, 0], data[i][:, 2]))
    rmprat.append(vltlst[-1] / (2 * ramps)[i])
plt.xlim([0, 6000])
plt.grid()
plt.xlabel("Normalized time scale [V]")
plt.ylabel("Electric current [A]")
plt.legend(prop={'size': 12})
plt.savefig("internal_currents_prp_0.pdf", format="pdf", bbox_inches="tight")
plt.show()

# plt.plot(['6', '100', '200', '400', '800', '1600', '4800', '19600', '96000'], vltlst[:9], color='red', alpha=0.6, label='')
# plt.plot(['6', '100', '200', '400', '800', '1600', '4800', '19600', '96000'], [6, 100, 200, 400, 800, 1600, 4800, 19200, 96000], color='black', alpha=0.6, label='')
# plt.yscale('log')
# plt.grid()
# plt.xlabel("Input voltage ramp [Vns]")
# plt.ylabel("Maximum output voltage ramp [Vns]")
# plt.legend(prop={'size': 12})
# plt.savefig("voltages_ramps.pdf", format="pdf", bbox_inches="tight")
# plt.show()

# plt.plot(['6', '100', '200', '400', '800', '1600', '4800', '19600', '96000'], rmprat, color='blue')
# plt.plot(['6', '96000'], [1, 1], '--', color='black', alpha=0.6)
# plt.ylim([0, 6])
# plt.grid()
# plt.savefig("voltage_ramp_ratio.pdf", format="pdf", bbox_inches="tight")
# plt.show()

# tlst = [30.0, 6.0, 4.0, 2.0, 1.5, 1.2, 1.2, 1.2, 1.2]
# for i in range(9):
#     plt.plot(1e9 * (data[i][:, 0] - timeshift), 570 * data[i][:, 3], color='darkorange', alpha=0.6, label=lbls[i])
#     plt.xlim([0, tlst[i]])
#     plt.grid()
#     plt.xlabel("Time [ns]")
#     plt.ylabel("Electric current [A]")
#     plt.legend(prop={'size': 24})
#     plt.savefig(f"time_curr_prp_{ramps[i]}.pdf", format="pdf", bbox_inches="tight")
#     plt.show()
