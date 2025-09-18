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

#rc("font", **{"family": "sans-serif", "sans-serif": ["Arial"]})
ticksize=18
labelsize=20
legendsize=15


filename='bulk_Q_H2O'
all_data=[]

all_data.append(np.loadtxt('data/0000.dat'))
all_data.append(np.loadtxt('data/0020.dat')) 
all_data.append(np.loadtxt('data/0040.dat')) 
all_data.append(np.loadtxt('data/0060.dat')) 
all_data.append(np.loadtxt('data/0080.dat')) 


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
#colors=['blue','orange','green','red']                                                                                                                                                                 
#Load data                                                                                                                                                                                              
                                                                                                                                                                                                        
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
    ax.plot(data[:,0],data[:,1], label=r' {:3.2f} eV/A'.format(field[i]),linestyle=linestyle[i],color=colors[i])

ax.set_xlabel(r'Q', fontsize=labelsize)                                                                                                                                                
ax.set_ylabel(r"P(Q)", fontsize=labelsize)                                                                                                                                             
#ax.set_ylabel(r"$\rho_H$ (a.u.) ", fontsize=labelsize)                                                                                                                                                 
#ax.set_xlim([1.5,8.2])                                                                                                                                                                                 
#ax.set_xlim([1.5,6.2])                                                                                                                                                                                 
ax.set_xlim([-0.25,1.1])                                                                                                                                                                                    
ax.set_ylim([0.,5.0])                                                                                                                                                                                    
plt.xticks(fontsize=ticksize)                                                                                                                                                                           
plt.yticks(fontsize=ticksize)                                                                                                                                                                           
#plt.yticks([],fontsize=ticksize)                                                                                                                                                                       
#plt.locator_params(axis='y', nbins=0)                                                                                                                                                                  
plt.locator_params(axis='x', nbins=5)                                                                                                                                                                   
plt.locator_params(axis='y', nbins=5)                                                                                                                                                                   
                                                                                                                                                                                                        
plt.legend(loc='upper center',ncol=3, fancybox=True, shadow=True,fontsize=legendsize, bbox_to_anchor=(0.5,1.30))                                                                                        
plt.savefig('{}.pdf'.format(filename),bbox_inches='tight')                                                                                                                                              
print('{}.pdf'.format(filename))                                                                                                                                                                        
