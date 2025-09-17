import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import matplotlib
import matplotlib.ticker as ticker
import sys

from toolkit.tools.units import Elements, Constants
from scipy.optimize import curve_fit



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

filename='DeltaF_E036'
field=0.36

def linearFunc(x,intercept,slope):
    y = intercept + slope * x
    return y

temp       = np.array( [300    , 330    ,  360   , 390    ] )
deltaF=np.array([28.71338703 ,26.63250585, 24.64410291 ,19.85536282])
deltaF_err=np.array([1.22362741, 0.97768438, 0.80843341, 1.34801938])

xdata=temp
ydata=deltaF
ydata_err=deltaF_err


a_fit,cov=curve_fit(linearFunc,xdata,ydata,sigma=ydata_err,absolute_sigma=True)
 
inter = a_fit[0]
slope = a_fit[1]
inter_err = np.sqrt(cov[0][0])
slope_err = np.sqrt(cov[1][1])


# Create a graph showing the data.
plt.errorbar(xdata,ydata,yerr=ydata_err,fmt='o',capsize=5,label='Data',color='red')
yfit = inter + slope*xdata
plt.plot(xdata,yfit,color='black')
 

# Add title and labels
plt.xlabel('Temperature (K) ',fontsize=labelsize)
plt.ylabel(r'$\Delta$F (kJ/mol)',fontsize=labelsize)
plt.title(r'E={:4.2f} '.format(field)+r'V/$\mathrm{\AA}$',fontsize=labelsize)


plt.grid(True) 
plt.xlim([290,400])
plt.ylim([15,35])
plt.xticks(fontsize=ticksize)
plt.yticks(fontsize=ticksize)
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=4)

plt.savefig('{}.pdf'.format(filename),bbox_inches='tight')
print('{}.pdf'.format(filename))

