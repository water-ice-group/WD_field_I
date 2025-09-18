import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from pathlib import Path
import sys
import pandas as pd

import matplotlib
import matplotlib.ticker as ticker




# plot settings
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
#plt.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]
matplotlib.rcParams['mathtext.default'] = 'regular'

#rc("font", **{"family": "sans-serif", "sans-serif": ["Arial"]})
ticksize=18
labelsize=20
legendsize=15


filename='populations'
datafile='data/selected.dat'
all_data=np.loadtxt(datafile)

field=     all_data[:,0]
field_au2evA=51.422061454950224
field*=field_au2evA
data={}
data_err={}
data['DDAA'] = all_data[:,1]
data['DDA']  = all_data[:,3]
data['DAA']  = all_data[:,5]
data['DA']   = all_data[:,7]
data_err['DDAA']= all_data[:,2]
data_err['DDA'] = all_data[:,4]
data_err['DAA'] = all_data[:,6]
data_err['DA']  = all_data[:,8]

rc("font", **{"family": "sans-serif", "sans-serif": ["Arial"]})
ticksize=18
labelsize=20
legendsize=15

#
factor=100
# Plot with error bars
for i,key in enumerate(data.keys()):
  plt.errorbar(field,factor * data[key], yerr=data_err[key], fmt='o', capsize=5, label=key)
  plt.plot(field, factor * data[key],color='black',linestyle='--')
#-----------------------------------------------------------------------------------


# Customize the plot
plt.xlabel('Field (V/A)',fontsize=labelsize)
plt.ylabel(r"Populations (%)",fontsize=labelsize)
plt.grid(True)

plt.xlim([-0.01,0.45])
plt.ylim([-0.01,101])
plt.xticks(fontsize=ticksize)
plt.yticks(fontsize=ticksize)
plt.legend(loc='upper center',ncol=2, fancybox=True, shadow=True,fontsize=legendsize, bbox_to_anchor=(0.5,1.30))
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=5)
plt.savefig('{}.pdf'.format(filename),bbox_inches='tight')
