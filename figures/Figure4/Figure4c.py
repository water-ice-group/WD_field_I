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
matplotlib.rcParams['mathtext.default'] = 'regular'

ticksize=18
labelsize=20
legendsize=15



all_data=[]

all_data.append(np.loadtxt('data_orientation/revPBE_0000_330K-xavi-400_orientation.dat'))
all_data.append(np.loadtxt('data_orientation/revPBE_0020_330K-xavi-400_orientation.dat'))
all_data.append(np.loadtxt('data_orientation/revPBE_0040_330K-xavi-400_orientation.dat'))
all_data.append(np.loadtxt('data_orientation/revPBE_0060_330K-xavi-400_orientation.dat'))
field=np.array([0.00, 0.002,0.004,0.006] )
field*=51.422061454950224 #au2eV/au2A

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
ndata_col=5
colors = get_color_gradient(ndata_col,0.8,0.0)                                                                                                                                                              
fig, ax = plt.subplots()#figsize=(6,6))                                                                                                                                                                   

for i in range(ndata):
    data=all_data[i]                                                                                                                                                                                       
    ax.plot(np.arange(data.size)*2,data, label=r' {:3.2f} '.format(field[i])+r'V/$\mathrm{\AA}$',color=colors[i])

ax.set_xlabel(r'time (fs)', fontsize=labelsize)
ax.set_ylabel(r"Norm. orientation", fontsize=labelsize)
filename='figure4c'
ax.set_xlim([0,1000])
ax.set_ylim([-0.1,1.1])                                                                                                                                                                                 

plt.xticks(fontsize=ticksize)                                                                                                                                                                           
plt.yticks(fontsize=ticksize)                                                                                                                                                                           
plt.locator_params(axis='x', nbins=5)                                                                                                                                                                   
plt.locator_params(axis='y', nbins=5)                                                                                                                                                                   
                                                                                                                                                                                                        
plt.legend(loc='upper center',ncol=2, fancybox=True, shadow=True,fontsize=legendsize, bbox_to_anchor=(0.5,1.30))                                                                                        
plt.savefig('{}.pdf'.format(filename),bbox_inches='tight')                                                                                                                                              
print('{}.pdf'.format(filename))                                                                                                                                                                        
