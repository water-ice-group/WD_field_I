import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import matplotlib
import matplotlib.ticker as ticker
from toolkit.tools.units import convert as c
import sys

from toolkit.tools.units import Elements, Constants
from scipy.optimize import curve_fit

fit=True
filename='DeltaF_E018'
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
field=0.18


def linearFunc(x,intercept,slope):
    y = intercept + slope * x
    return y

temp       = np.array( [ 300 ,330    , 360   ,390])
deltaF     = np.array( [ 77.3, 75.80  , 73.39 ,76.75 ]) # KJ/mol
deltaF_err = np.ones(deltaF.shape)*2.0  # KJ/mol
xdata=temp
ydata=deltaF
ydata_err=deltaF_err

a_fit,cov=curve_fit(linearFunc,xdata,ydata,sigma=ydata_err,absolute_sigma=True)
inter = a_fit[0]
slope = a_fit[1]
inter_err = np.sqrt(cov[0][0])
slope_err = np.sqrt(cov[1][1])


# Compute a best fit line from the fit intercept and slope.
yfit = inter + slope*xdata

# Create a graph showing the data.
plt.errorbar(xdata,ydata,yerr=ydata_err,fmt='o',capsize=5,color='red')

# Create a graph of the fit to the data. We just use the ordinary plot
plt.plot(xdata,yfit,color='black')


# Add title and labels
plt.xlabel('Temperature (K) ',fontsize=labelsize)
plt.ylabel(r'$\Delta$F (kJ/mol)',fontsize=labelsize)
plt.title(r'E={:4.2f}'.format(field) +r'V/$\mathrm{\AA}$',fontsize=labelsize)

plt.grid(True)
plt.xlim([290,400])
plt.ylim([65,85])
plt.xticks(fontsize=ticksize)
plt.yticks(fontsize=ticksize)
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=4)

plt.savefig('{}.pdf'.format(filename),bbox_inches='tight')
print('{}.pdf'.format(filename))

