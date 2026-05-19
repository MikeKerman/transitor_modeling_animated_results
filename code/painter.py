# change lines or blocks marked with "# UPDATE:" to suit your simulations

# import of modules

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as plt2
from scipy.interpolate import LinearNDInterpolator
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap

# plotting of junctions, boundaries and electrodes, to be modified manually
# 
# UPDATE: 
# each line is defined by a list of two lists, first is 'x' coordinate, second is 'y' coordinate
# each rectangle is defined by: left lower corner coordinates as a list, width, height
# note that 'y' coordinate is inverted
# currmult: current multiplies in visualization

plot_junctions = True
struct = 'smp'

if struct == 'smp':
    
    contour = [[0.0, 120.0, 120.0, 0.0, 0.0], [1.0, 1.0, -26.0, -26.0, 0.0]]
    incollector = [[0.0, 120.0, 120.0, 0.0, 0.0], [-20.0, -20.0, -25.0, -25.0, -20.0]]
    inemitter = [[0.0, 5.0, 5.0, 15.0, 15.0, 30.0, 30.0, 110.0, 110.0, 120.0, 0.0], [0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0]]
    collectorbase = [[0.0, 120.0], [-6.0, -6.0]]
    emitterbase = [[20.0, 20.0, 120.0], [0.0, -5.0, -5.0]]
    
    eemitter1 = [[30.0, 0.0], 80.0, 1.0]
    ecollector = [[0.0, -26.0], 120.0, 1.0]
    ebase1 = [[5.0, 0.0], 10.0, 1.0]
    
    oemitter1 = [[0.0, 0.0], 5.0, 1.0]
    oemitter2 = [[15.0, 0.0], 15.0, 1.0]
    oemitter3 = [[110.0, 0.0], 10.0, 1.0]

    lines = [contour, incollector, inemitter, collectorbase, emitterbase]
    elecs = [eemitter1, ecollector, ebase1]
    oxids = [oemitter1, oemitter2, oemitter3]

    currmult = 570.0
    
elif struct == 'asm':
    
    contour = [[0.0, 175.0, 175.0, 0.0, 0.0], [1.0, 1.0, -26.0, -26.0, 0.0]]
    incollector = [[0.0, 175.0, 175.0, 0.0, 0.0], [-20.0, -20.0, -25.0, -25.0, -20.0]]
    inemitter = [[0.0, 35.0, 35.0, 45.0, 45.0, 60.0, 60.0, 140.0, 140.0, 160.0, 160.0, 175.0, 175.0, 0.0], [0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0]]
    collectorbase = [[30.0, 30.0, 175.0], [0.0, -6.0, -6.0]]
    emitterbase = [[50.0, 50.0, 150.0, 150.0], [0.0, -4.0, -4.0, 0.0]]
    
    eemitter1 = [[60.0, 0.0], 80.0, 1.0]
    ecollector = [[0.0, -26.0], 175.0, 1.0]
    ebase1 = [[35.0, 0.0], 10.0, 1.0]
    ebase2 = [[160.0, 0.0], 15.0, 1.0]
    
    oemitter1 = [[0.0, 0.0], 35.0, 1.0]
    oemitter2 = [[45.0, 0.0], 15.0, 1.0]
    oemitter3 = [[140.0, 0.0], 20.0, 1.0]

    lines = [contour, incollector, inemitter, collectorbase, emitterbase]
    elecs = [eemitter1, ecollector, ebase1, ebase2]
    oxids = [oemitter1, oemitter2, oemitter3]

    currmult = 570.0
    
elif struct == 'sym':
    
    contour = [[0.0, 350.0, 350.0, 0.0, 0.0], [1.0, 1.0, -26.0, -26.0, 0.0]]
    incollector = [[0.0, 350.0, 350.0, 0.0, 0.0], [-20.0, -20.0, -25.0, -25.0, -20.0]]
    inemitter = [[0.0, 35.0, 35.0, 45.0, 45.0, 60.0, 60.0, 140.0, 140.0, 160.0, 160.0, 190.0, 190.0, 210.0, 210.0, 290.0, 290.0, 305.0, 305.0, 315.0, 315.0, 350.0, 0.0], [0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0]]
    collectorbase = [[30.0, 30.0, 320.0, 320.0], [0.0, -6.0, -6.0, 0.0]]
    emitterbase = [[50.0, 50.0, 150.0, 150.0, 200.0, 200.0, 300.0, 300.0], [0.0, -4.0, -4.0, 0.0, 0.0, -4.0, -4.0, 0.0]]
    
    eemitter1 = [[60.0, 0.0], 80.0, 1.0]
    eemitter2 = [[210.0, 0.0], 80.0, 1.0]
    ecollector = [[0.0, -26.0], 350.0, 1.0]
    ebase1 = [[35.0, 0.0], 10.0, 1.0]
    ebase2 = [[160.0, 0.0], 30.0, 1.0]
    ebase3 = [[305.0, 0.0], 10.0, 1.0]
    
    oemitter1 = [[0.0, 0.0], 35.0, 1.0]
    oemitter2 = [[45.0, 0.0], 15.0, 1.0]
    oemitter3 = [[140.0, 0.0], 20.0, 1.0]
    oemitter4 = [[190.0, 0.0], 20.0, 1.0]
    oemitter5 = [[290.0, 0.0], 15.0, 1.0]
    oemitter6 = [[315.0, 0.0], 35.0, 1.0]

    lines = [contour, incollector, inemitter, collectorbase, emitterbase]
    elecs = [eemitter1, eemitter2, ecollector, ebase1, ebase2, ebase3]
    oxids = [oemitter1, oemitter2, oemitter3, oemitter4, oemitter5, oemitter6]

    currmult = 285.0

def plot_le(ax, plot_junctions, lines, elecs, oxids):
    if not plot_junctions:
        return
    for line in lines:
        ax.plot(line[0], line[1], color='k')
    for elec in elecs:
        ax.add_patch(plt2.Rectangle(*elec, fill=True, edgecolor='slategray', facecolor='slategray'))
    for oxid in oxids:
        ax.add_patch(plt2.Rectangle(*oxid, fill=True, edgecolor='black', facecolor='black'))
    return

# data extraction and initial processing functions

# UPDATE: file naming convention function

def get_filename(sim, frame):   # 'sim' is changing part of the simulation directories
    keyword = "ramp_"           # 'keyword' is constant part of the simulation directories
    ketword = "Vns_smp_b18"      # 'ketword' is constant part after changing part
    dircs = os.listdir()
    found = False
    for dirc in dircs:
        if dirc[:(len(keyword) + len(sim) + len(ketword))] == keyword + sim + ketword:
            found = True
            break
    if not found:
        raise Exception(f"No file or directory that start with '{keyword}', ends with '{ketword}' and corresponds to '{sim}'")
    files = os.listdir(dirc)
    for file in files:
        mainname = file.split('____')[0]
        if mainname == keyword + sim + ketword + str(frame):        # 'frame' is number of simulation file
            return f"{keyword}{sim}{ketword}/{file}"

# UPDATE: function for data from file names

def get_filename_data(filename):
    datadict = {}
    for datapoint in filename.split('____')[1:-1]:
        datadict[datapoint.split('=')[0]] = float(datapoint.split('=')[1].split('_')[0])
    return datadict

def extract(filename):
    with open(filename, 'r') as file:
        points = []
        values = []
        for line in file:
            if line[0] == 'c' and line[1] == ' ':
                points.append(line[1:].split())
            elif line[0] == 'n' and line[1] == ' ':
                values.append(line[1:].split())
    for point in points:
        point[0] = int(point[0])
        for i in range(1, len(point)):
            point[i] = float(point[i])
    for value in values:
        value[0] = int(value[0])
        for i in range(1, len(value)):
            value[i] = float(value[i])
    dell = []
    for i in range(len(points[:-1])):
        if points[i+1][0] - points[i][0] != 1:
            nval = []
            for j in range(len(points[i+1])):
                if points[i+1][j] != points[i][j]:
                    nval.append((points[i+1][j] + points[i][j])/2)
                else:
                    nval.append(points[i][j])
            points[i] = nval
            dell.append(i+1)
    for deli in reversed(dell):
        del points[deli]
    dell = []
    for i in range(len(values[:-1])):
        if values[i+1][0] - values[i][0] == 0:
            nval = []
            for j in range(len(values[i+1])):
                if values[i+1][j] != values[i][j]:
                    nval.append((values[i+1][j] + values[i][j])/2)
                else:
                    nval.append(values[i][j])
            values[i] = nval
            dell.append(i+1)
    for deli in reversed(dell):
        del values[deli]
    if len(points) != len(values):
        raise Exception("Number of points and number of values do not agree after initial processing.")
    return points, values

def round_sig(n, k):
    if n == 0.0:
        return 0.0
    k = k - int(np.floor(np.log10(abs(n)))) - 1
    return round(n, k)

# data processing function, index of required data and data function is to be modified manually
# 
# UPDATE:
# indecies are found in .str file, order in line starting with "s ", keys in lines starting with "Q ", it is recommended to use negative indecies
# "indx" syntax: "int" for single values, "list" with two integers for 2D vectors ("d2vec" function should be updated appropriately) or other transformations

indx = [-9, -28, -29, -3, -6, -31, -8, -18] # total current density (A/cm^2); hole density (1/cm^3); electron density (1/cm^3), displacement current density (A/cm^2); conductive current density (A/cm^2); potential (V); lateral current density (A/cm^2); electric field (V/cm)
d2vec = lambda x, i, j: (x[i]**2 + x[j]**2)**0.5
d2sum = lambda x, i, j: (x[i] + x[j])

def full_data(points, values, indx):
    data = []
    for i in range(len(points)):
        lst = [points[i][1], points[i][2]]
        for ix in indx:
            if type(ix) is int:
                lst.append(values[i][ix])
            elif type(ix) is list:
                if len(ix) == 2:
                    lst.append(d2vec(values[i], ix[0], ix[1]))
                elif len(ix) == 3 and ix[0] == 'sum':
                    lst.append(d2sum(values[i], ix[1], ix[2]))
        data.append(lst)
    data = np.array(data)
    return data

# single sample plotting
# 
# change cmap_pivots to change colormap properties

# cmap_pivots = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]   # UPDATE: either onesided uniform
cmap_pivots = [0.0, 0.01, 0.05, 0.1, 0.5, 1.0]   # UPDATE: or onesided logarithmic
# cmap_pivots = [0.0, 0.25, 0.5, 0.75, 1.0]   # UPDATE: or doublesided uniform
# cmap_pivots = [0.0, 0.45, 0.5, 0.55, 1.0]   # UPDATE: or doublesided logarithmic
# UPDATE: either onesided, or doublesided colrmap, comment out one
# non-rgb
cmap_dict = {'red':   [[cmap_pivots[0], 0.2, 0.2], [cmap_pivots[1], 0.5, 0.5], [cmap_pivots[2], 1.0, 1.0], [cmap_pivots[3], 1.0, 1.0], [cmap_pivots[4], 1.0, 1.0], [cmap_pivots[5], 1.0, 1.0]],
             'green': [[cmap_pivots[0], 0.2, 0.2], [cmap_pivots[1], 0.5, 0.5], [cmap_pivots[2], 1.0, 1.0], [cmap_pivots[3], 0.5, 0.5], [cmap_pivots[4], 0.25, 0.25], [cmap_pivots[5], 1.0, 1.0]],
             'blue':  [[cmap_pivots[0], 0.2, 0.2], [cmap_pivots[1], 0.0, 0.0], [cmap_pivots[2], 0.0, 0.0], [cmap_pivots[3], 0.2, 0.2], [cmap_pivots[4], 1.0, 1.0], [cmap_pivots[5], 1.0, 1.0]]}
# onesided:
# cmap_dict = {'red':   [[cmap_pivots[0], 1.0, 1.0], [cmap_pivots[1], 1.0, 1.0], [cmap_pivots[2], 0.0, 0.0], [cmap_pivots[4], 0.0, 0.0], [cmap_pivots[5], 1.0, 1.0]],
#              'green': [[cmap_pivots[0], 0.0, 0.0], [cmap_pivots[1], 1.0, 1.0], [cmap_pivots[3], 1.0, 1.0], [cmap_pivots[4], 0.0, 0.0], [cmap_pivots[5], 0.0, 0.0]],
#              'blue':  [[cmap_pivots[0], 0.0, 0.0], [cmap_pivots[2], 0.0, 0.0], [cmap_pivots[3], 1.0, 1.0], [cmap_pivots[5], 1.0, 1.0]]}
# doublesided:
# cmap_dict = {'red':   [[cmap_pivots[0], 0.0, 0.0], [cmap_pivots[1], 1.0, 1.0], [cmap_pivots[3], 1.0, 1.0], [cmap_pivots[4], 0.0, 0.0]],
#              'green': [[cmap_pivots[0], 0.0, 0.0], [cmap_pivots[2], 0.0, 0.0], [cmap_pivots[3], 1.0, 1.0], [cmap_pivots[4], 1.0, 1.0]],
#              'blue':  [[cmap_pivots[0], 1.0, 1.0], [cmap_pivots[1], 1.0, 1.0], [cmap_pivots[2], 0.0, 0.0], [cmap_pivots[4], 0.0, 0.0]]}
fine_rygcbm_cmap = LinearSegmentedColormap('fine_rygcbm_cmap', cmap_dict, N=65536)

def scmap(fig, ax, sim, n):
    filename = "ramp_" + sim + "_r/ramp_" + sim + str(n) + ".str"   # UPDATE: file naming convention (desired file)
    data = full_data(*extract(filename), indx)
    x = data[:, 0]
    y = -data[:, 1]
    z = data[:, 2]
    xg = np.linspace(min(x), max(x), 1000)
    yg = np.linspace(min(y), max(y), 1000)
    xg, yg = np.meshgrid(xg, yg)
    interp = LinearNDInterpolator(list(zip(x, y)), z)
    zg = interp(xg, yg)
    pcm = ax.pcolormesh(xg, yg, zg, shading='auto', cmap=fine_rygcbm_cmap, vmin=0.0, vmax=8000.0)   # UPDATE: "vmin" and "vmax" are upper and lower limits for the colormap
    fig.colorbar(pcm, ax=ax)
    plot_le(ax, plot_junctions, lines, elecs, oxids)
    return pcm
   
#fig, ax = plt.subplots()
#scmap(fig, ax, "medium", 30)

# animated plotting

sim = "96000"   # UPDATE: simulation selection (name, number of frames, including frame zero)
framen = 33
if sim == "6":
    simcodename = "static"
elif sim == "100":
    simcodename = "slow"
elif sim == "200":
    simcodename = "medium"
elif sim == "400":
    simcodename = "fast"
elif sim == "800":
    simcodename = "faster"
elif sim == "1600":
    simcodename = "fastest"
elif sim == "4800":
    simcodename = "rapid"
elif sim == "19200":
    simcodename = "blitz"
elif sim == "96000":
    simcodename = "bullet"
else:
    simcodename = "noname"
# ttl = lambda t, U, I, Ui: f" $t$ = {round_sig(t * 1.0e9 - 100.0, 3)}ns, $V$ = {round_sig(U, 3)}V, $I$ = {round_sig(currmult * I, 3)}A "   # UPDATE: plot title
ttl = lambda t, U, I, Ui: f"$I$ = {round_sig(currmult * I, 3)}A"
dindex = 2      # UPDATE: index of plotted data from "indx" list starting at "2", first two are cartesian coordinates
dmax = -1000000000
dmin = 1000000000

fig, ax = plt.subplots()
plt.title("ramp_" + sim)
filename = get_filename(sim, 0)     # UPDATE: by default, file numbering starts from zero
data = full_data(*extract(filename), indx)
x = data[:, 0]
y = -data[:, 1]
z = data[:, dindex] - min(data[:, dindex])   # UPDATE: uncomment to normalize (useful for potential)
xg = np.linspace(min(x), max(x), 1000)
yg = np.linspace(min(y), max(y), 1000)
xg, yg = np.meshgrid(xg, yg)
interp = LinearNDInterpolator(list(zip(x, y)), z)
zg = interp(xg, yg)
pcm = ax.pcolormesh(xg, yg, zg, shading='auto', cmap=fine_rygcbm_cmap, vmin=0.0, vmax=12000000) # UPDATE: "vmin" and "vmax" are upper and lower limits for the colormap
cbar = fig.colorbar(pcm, ax=ax)
cbar.set_label('A$\cdot$cm$^{-2}$', rotation=90)
plot_le(ax, plot_junctions, lines, elecs, oxids)
plt.xlabel("μm")
plt.ylabel("μm")

def init():
    filename = get_filename(sim, 0)     # UPDATE: by default, file numbering starts from zero
    data = full_data(*extract(filename), indx)
    x = data[:, 0]
    y = -data[:, 1]
    z = data[:, dindex] # - min(data[:, dindex])   # UPDATE: uncomment to normalize (useful for potential)
    xg = np.linspace(min(x), max(x), 1000)
    yg = np.linspace(min(y), max(y), 1000)
    xg, yg = np.meshgrid(xg, yg)
    interp = LinearNDInterpolator(list(zip(x, y)), z)
    zg = interp(xg, yg)
    pcm.set_array(zg)
    datadict = get_filename_data(filename)
    plt.title(ttl(datadict['t'], datadict['U'], datadict['I'], datadict['Ui']))     # UPDATE: dictionary keys
    return pcm

def update(frame):
    global dmax, dmin
    filename = get_filename(sim, frame)
    data = full_data(*extract(filename), indx)
    x = data[:, 0]
    y = -data[:, 1]
    z = data[:, dindex] # - min(data[:, dindex])   # UPDATE: uncomment to normalize (useful for potential)
    zmax = max(z)
    zmin = min(z)
    dmax = max([zmax, dmax])
    dmin = min([zmin, dmin])
    xg = np.linspace(min(x), max(x), 1000)
    yg = np.linspace(min(y), max(y), 1000)
    xg, yg = np.meshgrid(xg, yg)
    interp = LinearNDInterpolator(list(zip(x, y)), z)
    zg = interp(xg, yg)
    pcm.set_array(zg)
    datadict = get_filename_data(filename)
    plt.title(ttl(datadict['t'], datadict['U'], datadict['I'], datadict['Ui']))     # UPDATE: dictionary keys
    return pcm

ani = FuncAnimation(fig, update, frames=np.arange(0, framen), init_func=init, repeat=False, interval=1000)   # UPDATE: by default, file (frame) numbering starts from zero; interval between frames in milliseconds
ani.save(filename=("ramp_" + sim + "_" + simcodename + "_b18_current.gif"), writer="pillow")   # UPDATE: output file name

print(f"minimun value: {dmin}")
print(f"maximum value: {dmax}")
