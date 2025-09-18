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

all_data.append(np.loadtxt('data_free_energy/0000.dat',skiprows=1))
all_data.append(np.loadtxt('data_free_energy/0020.dat',skiprows=1))
all_data.append(np.loadtxt('data_free_energy/0040.dat',skiprows=1))
all_data.append(np.loadtxt('data_free_energy/0060.dat',skiprows=1))
field=np.array([0.      ,   0.10284412, 0.20568825 ,0.30853237])


def get_color_gradient(n,init=0.0,fin=1.0):                                                                                                                                                             
    """ Generate n distinct colors from a colormap. """                                                                                                                                                 
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
tiny=10**-6
factor=1
for i in range(ndata):
    data=all_data[i]                                                                                                                                                                                       
    free_energy = -np.log(data[:,1]+tiny)
    free_energy -= np.min(free_energy)
    free_energy_smoothed = pd.Series(free_energy).rolling(window=5, center=True, min_periods=1).mean().to_numpy()
    free_energy_smoothed -= np.min(free_energy_smoothed)

    ax.plot(data[:,0],free_energy_smoothed, label=r' {:3.2f} '.format(field[i])+r'V/$\mathrm{\AA}$',color=colors[i])



    plt.fill_between(data[:,0],free_energy_smoothed*0.95,  free_energy_smoothed*1.05, alpha=0.3, color=colors[i])

ax.set_xlabel(r'$\delta$ ($\mathrm{\AA}$)', fontsize=labelsize)                                                                                                                                                
ax.set_ylabel(r"$\Delta $F$ / k_\mathrm{B}T$  ", fontsize=labelsize)                                                                                                                                             
plt.grid(True, linestyle="--", linewidth=0.7, color="gray")

filename='figure4b'

ax.set_xlim([-0.7,+0.7])
ax.set_ylim([-0.1,2.5])



plt.xticks(fontsize=ticksize)                                                                                                                                                                           
plt.yticks(fontsize=ticksize)                                                                                                                                                                           
plt.locator_params(axis='x', nbins=5)                                                                                                                                                                   
plt.locator_params(axis='y', nbins=5)                                                                                                                                                                   
                                                                                                                                                                                                        
plt.legend(loc='upper center',ncol=2, fancybox=True, shadow=True,fontsize=legendsize, bbox_to_anchor=(0.5,1.30))                                                                                        
plt.savefig('{}.pdf'.format(filename),bbox_inches='tight')                                                                                                                                              
