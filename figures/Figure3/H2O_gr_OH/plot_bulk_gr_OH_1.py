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

all_data=[]

all_data.append(np.loadtxt('data/000.dat'))
all_data.append(np.loadtxt('data/002.dat'))
all_data.append(np.loadtxt('data/004.dat'))
all_data.append(np.loadtxt('data/006.dat'))
all_data.append(np.loadtxt('data/008.dat'))

field=np.array([0.00, 0.002,0.004,0.006,0.008] )
field_au2evA=51.422061454950224
field*=field_au2evA

def get_color_gradient(n,init=0.0,fin=1.0):                                                                                                                                                             
    """ Generate n distinct colors from a colormap. """                                                                                                                                                 
    cmap = plt.get_cmap('cool')                                                                                                                                                                        
    cmap = plt.get_cmap('Greens')                                                                                                                                                                      
    cmap = plt.get_cmap('gist_heat')                                                                                                                                                                    
    cmap = plt.get_cmap('plasma')
    return [cmap(i) for i in np.linspace(init, fin, n)]                                                                                                                                                 
                                                                                                                                                                                                        
rc("font", **{"family": "sans-serif", "sans-serif": ["Arial"]})                                                                                                                                         
ticksize=18                                                                                                                                                                                             
labelsize=20                                                                                                                                                                                            
legendsize=15                                                                                                                                                                                           
ndata=len(field)                                                                                                                                                                                  
colors = get_color_gradient(ndata,0.8,0.0)                                                                                                                                                              
colors[-1]='black'
fig, ax = plt.subplots()#figsize=(6,6))                                                                                                                                                                   
plt.grid(True, linestyle="--", linewidth=0.7, color="gray")

linestyle=[]
for i in range(ndata):
 linestyle.extend('-')
linestyle[-1]='--'

for i in range(ndata):
    data=all_data[i]                                                                                                                                                                                       
    print(data.shape)
    ax.plot(data[:,0],data[:,1], label=r' {:3.2f} '.format(field[i])+r'V/$\mathrm{\AA}$',linestyle=linestyle[i],color=colors[i])   
ax.set_xlabel(r'r ($\mathrm{\AA}$)', fontsize=labelsize)                                                                                                                                                
ax.set_ylabel(r"gr$_\mathrm{OH}$ ", fontsize=labelsize)                                                                                                                                             
filename='bulk_grOH_1'
ax.set_xlim([1.3,6.2])
ax.set_xlim([1.3,4])
ax.set_ylim([0,2])                                                                                                                                                                                 
plt.xticks(fontsize=ticksize)                                                                                                                                                                           
plt.yticks(fontsize=ticksize)                                                                                                                                                                           
plt.locator_params(axis='x', nbins=5)                                                                                                                                                                   
plt.locator_params(axis='y', nbins=5)                                                                                                                                                                   
plt.legend(loc='upper center',ncol=3, fancybox=True, shadow=True,fontsize=legendsize, bbox_to_anchor=(0.5,1.30))                                                                                        
plt.savefig('{}.pdf'.format(filename),bbox_inches='tight')                                                                                                                                              
print('{}.pdf'.format(filename))                                                                                                                                                                        
