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
rc("font", **{"family": "sans-serif", "sans-serif": ["Arial"]})
ticksize=18
labelsize=20
legendsize=15

field_evA2au=51.422061454950224
filename='figure1b'

def linearFunc(x,intercept,slope):
    y = intercept + slope * x
    return y


x=np.array(    [0.          ,0.10284412   ,0.20568825   ,0.25711031   ,0.30853237  , 0.35995443  ,  0.41137649])
y=np.array(    [0.43336548  ,0.43336548   ,0.43336548   ,0.43336548   ,1.56011573  ,17.50796539 ,171.17936463])
y_err=np.array([0.          ,0.           ,0.           ,0.           ,0.1838614   , 4.29009938  , 15.32178348])

fig, ax = plt.subplots()
bar_width=0.03
ax.bar(x, y, bar_width, yerr=y_err, label='Center', color='red', capsize=2, zorder=3, edgecolor='k')


plt.grid(True, linestyle="--", linewidth=0.7, color="gray")

# Labels and legend
plt.xlabel(r'Field (V/$\mathrm{\AA}$)',fontsize=labelsize)
plt.ylabel(r' H$^+$/OH$^-$  conc. (mM)',fontsize=labelsize)
plt.grid(True)

plt.xticks(fontsize=ticksize)
plt.yticks(fontsize=ticksize)
plt.xlim([-0.01,0.45])
plt.ylim([-2,205])

#plt.legend(loc='best',ncol=1, fancybox=True, shadow=True,fontsize=legendsize, bbox_to_anchor=(0.5,1.40))
plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=6)
plt.savefig('{}.pdf'.format(filename),bbox_inches='tight')

print('{}.pdf'.format(filename))

