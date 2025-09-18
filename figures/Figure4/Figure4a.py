import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import matplotlib
import matplotlib.ticker as ticker
import sys

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

field_au2evA=51.422061454950224 #au2eV/au2A

datafile='data_hb/proton-hb.dat'
data=np.loadtxt(datafile)
datafile_pure_h2o='data_hb/h2o-hb.dat'
data_pure_h2o=np.loadtxt(datafile_pure_h2o)
error=True

######   water in 0.86 M H3O^+   ##############

field       =    data[:,0]*field_au2evA
h2o_d       =    (data[:,1])
h2o_d_err   =    data[:,2]

filename='Figure4a'
label =[r'H$_2$O (H$_3$O$^+$ 0.86 M)']
plot_data    = [  h2o_d ]
#plot_data[0]-=plot_data[0][0]
plot_data_err=[  h2o_d_err ]
ylabel=r"HB per H$_2$O"
y_min=3.35
y_max=4.0
   
   
######   Pure water   ##############
factor=1
x=field
ndata=len(label)
for i in range(ndata):
 # Plot with error bars
 plt.errorbar(x, 2*plot_data[i],yerr=plot_data_err[i], fmt='x', capsize=5, label=label[i],color='blue')
 plt.plot(x, 2*plot_data[i],color='blue',linestyle='--') 

h2o_pure      =    (data_pure_h2o[:,1]-data_pure_h2o[0,1])
h2o_pure      =    data_pure_h2o[:,1]
h2o_pure_err  =    data_pure_h2o[:,2]
field_pure     =    data_pure_h2o[:,0]*field_au2evA

plt.errorbar(field_pure, 2*h2o_pure,yerr=h2o_pure_err, fmt='o', capsize=5, label=r'Pure H$_2$O',color='black')
plt.plot(field_pure, 2*h2o_pure,color='black',linestyle='--')

##########################################


# Customize the plot
plt.xlabel('Field (V/A)',fontsize=labelsize)
plt.ylabel(ylabel,fontsize=labelsize)
plt.legend()
plt.grid(True)

plt.ylim([y_min,y_max]) 
plt.xticks(fontsize=ticksize)
plt.yticks(fontsize=ticksize)
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=6)
plt.savefig('{}.pdf'.format(filename),bbox_inches='tight')
print('{}.pdf'.format(filename))

