import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import matplotlib
import matplotlib.ticker as ticker
from toolkit.tools.units import convert as c
import sys

#### plot settings
matplotlib.rcParams.update(matplotlib.rcParamsDefault)
smallsize = 10
largesize = 10
plt.rcParams.update({'font.size': largesize})
plt.rc('xtick', labelsize = smallsize, direction='in')
plt.rc('ytick', labelsize= smallsize, direction='in')
plt.rc('axes', labelsize = largesize)
plt.rc('axes', titlesize = largesize, linewidth=0.7)
plt.rc('legend', fontsize=largesize)
plt.rc('lines', markersize=8, linewidth=2)
plt.rc('legend', frameon=True,framealpha=1,)
plt.rcParams['figure.figsize'] = [4,4]
plt.rc('text', usetex=False)
matplotlib.rcParams['mathtext.default'] = 'regular'
rc("font", **{"family": "sans-serif", "sans-serif": ["Arial"]})
ticksize=18
labelsize=20
legendsize=15
###### 

filename='figure1c'
datafile='data1c.dat'
data=np.loadtxt(datafile)
field=     data[:,0]
field_evA2au=c.au2eV/c.au2A                                                                                                                                                                             
field*=field_evA2au   
angle    =    data[:,1]
angle_err=data[:,2]


#
x=field
factor=1.0#64*1000/12.42/12.42/12.42
y=angle*factor
yerr=2.0*angle_err*factor


# Plot with error bars
plt.errorbar(x, y, yerr=yerr, fmt='o', capsize=10, label='Pure H2O',color='black')
plt.plot(x, y,color='black',linestyle='--')


plt.xlabel('Field (V/A)',fontsize=labelsize)

plt.ylabel(r" Norm. Orientation ",fontsize=labelsize)
plt.grid(True)

plt.xticks(fontsize=ticksize)
plt.yticks(fontsize=ticksize)
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=6)
plt.savefig('{}.pdf'.format(filename),bbox_inches='tight')
print('{}.pdf'.format(filename))

