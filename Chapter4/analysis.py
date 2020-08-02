import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns;
from scipy.interpolate import make_interp_spline, BSpline
from random import random

plt.rcParams.update({'errorbar.capsize': 2})

df = pd.read_csv(
    '/Users/marc/Thesis/Chapter4/permeabilities.csv')

h2 = df[ df['Test'] == 'Pure H2']
carbon = df[ df['Test'] == 'Non Sulphur']
sulf = df[ df['Test'] == 'Sulphur']

df
def bar_chart():
    df = pd.read_csv(
        '/Users/marc/Thesis/Chapter4/permeabilities.csv')

    h2 = df[ df['Test'] == 'Pure H2']
    carbon = df[ df['Test'] == 'Non Sulphur']
    sulf = df[ df['Test'] == 'Sulphur']

    h2[h2['Metal']=='PdAu']
    plt.style.use('science')
    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(15,8))
        #PdAu
        ax.bar(1,3.338900, yerr= 0.2, width=1, label = 'Pure H$_2$', color='white', edgecolor='black' )
        ax.bar(1+1,1.649674, yerr= 0.268, width=1, label = 'Carbonaceous', color='grey', hatch='/', edgecolor='black' )
        ax.bar(1+2,2.154176, yerr= 0.168, width=1, label = 'Sulphurous', color='grey', hatch='/', edgecolor='black' )
        #PdAg
        ax.bar(1,9.486891, yerr= 0.212, width=1, label = 'Pure H$_2$', color='white', edgecolor='black' )
        ax.bar(1+1,1.173821, yerr= 0.38, width=1, label = 'Carbonaceous', color='grey', hatch='/', edgecolor='black' )
        ax.bar(1+2,0.779300, yerr= 0.12, width=1, label = 'Sulphurous', color='grey', hatch='/', edgecolor='black' )



        ax.set(xlabel="Metal")
        ax.set(ylabel="Permeability")
        fig.suptitle('Permeability of palladium alloy membranes at 30oC', fontsize=24)
        ax.autoscale(tight=False)
        plt.legend()
        fig.show()
        fig.savefig('permeabilities.jpg', dpi=300)


