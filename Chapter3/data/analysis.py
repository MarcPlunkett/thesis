import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns;
from scipy.interpolate import make_interp_spline, BSpline
from random import random

plt.rcParams.update({'errorbar.capsize': 2})

def site_graph():
    df = pd.read_csv(
            '/Users/marc/Thesis/Chapter3/data/Hydrogen_adsorption.csv')

    df


    df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))

    isPd = df['Metal'] == 'Pd'


    plt.style.use('science')


    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(6,5))
        ax.plot(PD['Site'], PD['adsry'], label='Pd', color='black', marker='D' )
        

        ax.set(xlabel="Adsorption site")
        ax.set(ylabel="Adsorption energy (Ry)")
        fig.suptitle('Hydrogen adsorption sites on Pd', fontsize=14)
        ax.autoscale(tight=False)
        fig.show()

        fig.savefig('PDSITES.jpg', dpi=300)



def heatmap():

    df = pd.read_csv(
                '/Users/marc/Thesis/Chapter3/data/Hydrogen_adsorption.csv')
    df['Adsorption energy (Ry)'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))
    df.drop(['Metal','Site', 'Total energy (Ry)', 'Total energy (kJ)','Adsorption energy(kJ)', 'K/mol'], axis=1, inplace=True)

    corr = df.corr()
    corr = corr.drop(['Pd', 'Ag', 'Au', 'Cu', 'Zr'])
    ax = sns.heatmap(
        corr, 
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        square=True
    )
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right'
    );

heatmap()



## H2
def H2_graphs():

    df = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/Hydrogen_adsorption.csv')

    df

    df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))

    isPd = df['Metal'] == 'Pd'
    isPdAu10 = df['Metal'] == 'PdAu10'
    isPdAg23 = df['Metal'] == 'PdAg23'
    isPd80Cu20 = df['Metal'] == 'Pd80Cu20'
    isPd60Cu40 = df['Metal'] == 'Pd60Cu40'
    isPdAu20 = df['Metal'] == 'PdAu20'
    isPdZr10 = df['Metal'] == 'PdZr10'
    isPdZr20 = df['Metal'] == 'PdZr20'
    isPd70Au20Ag10 = df['Metal'] == 'Pd70Au20Ag10'


    PD = df[isPd]
    PDAu10 = df[isPdAu10]
    PdAg23 = df[isPdAg23]
    Pd80Cu20 = df[isPd80Cu20]
    Pd60Cu40 = df[isPd60Cu40]
    PdAu20 = df[isPdAu20]
    PdZr10 = df[isPdZr10]
    PdZr20 = df[isPdZr20]
    Pd70Au20Ag10 = df[isPd70Au20Ag10]
    Pd70Au20Cu10 = df[ df['Metal'] == 'Pd70Au20Cu10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Ag10 = df[ df['Metal'] == 'Pd70Cu20Ag10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Zr10 = df[ df['Metal'] == 'Pd70Cu20Zr10']
    Pd70Zr20Ag10 = df[ df['Metal'] == 'Pd70Zr20Ag10']


    PD

    PDAu10

    # spl = make_interp_spline(x, data, k=3)  # type: BSpline
    # power_smooth = spl(x_new)


    plt.style.use('science')


    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(15,8))
        ax.bar('Pd', PD['adsry'].mean(),yerr=PDAu10['adsry'].sem(), width=1, label='Pd', color='white', edgecolor='black',)
        ax.bar('PdAu$_{10}$', PDAu10['adsry'].mean(),yerr=PDAu10['adsry'].sem(),width=1,zorder=1, label='PdAu$_{10}$', color='0.8', edgecolor='black')
        ax.bar('PdAu$_{20}$', PdAu20['adsry'].mean(),yerr=PdAu20['adsry'].sem(),width=1,zorder=1, label='PdAu$_{20}$',color='0.6', edgecolor='black')
        ax.bar('PdAg$_{23}$', PdAg23['adsry'].mean(),yerr=PdAg23['adsry'].sem(),width=1,zorder=1, label='PdAg$_{23}$',color='0.3', edgecolor='black')
        ax.bar('Pd$_{80}$Cu$_{20}$', Pd80Cu20['adsry'].mean(),yerr=Pd80Cu20['adsry'].sem(),width=1,zorder=1, label='Pd$_{80}$Cu$_{20}$',color='0.8', edgecolor='black', hatch='//')
        ax.bar('Pd$_{60}$Cu$_{40}$', Pd60Cu40['adsry'].mean(),yerr=Pd60Cu40['adsry'].sem(),width=1,zorder=1, label='Pd$_{60}$Cu$_{40}$', color='0.6', edgecolor='black', hatch='+')
        ax.bar('PdZr$_{10}$', PdZr10['adsry'].mean(),yerr=PdZr10['adsry'].sem(),width=1,zorder=1, label='PdZr$_{10}$',color='0.3', edgecolor='black', hatch='*')
        ax.bar('PdZr$_{20}$', PdZr20['adsry'].mean(),yerr=PdZr20['adsry'].sem(),width=1,zorder=1, label='PdZr$_{20}$',color='1', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Au$_{20}$Ag$_{10}$', Pd70Au20Ag10['adsry'].mean(),yerr=Pd70Au20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='+')
        ax.bar('Pd$_{70}$Au$_{20}$Cu$_{10}$', Pd70Au20Cu10['adsry'].mean(),yerr=Pd70Au20Cu10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Cu$_{10}$',color='0.6', edgecolor='black', hatch='*')
        ax.bar('Pd$_{70}$Au$_{20}$Zr$_{10}$', Pd70Au20Zr10['adsry'].mean(),yerr=Pd70Au20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Zr$_{10}$',color='0.3', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Cu$_{20}$Ag$_{10}$', Pd70Cu20Ag10['adsry'].mean(),yerr=Pd70Cu20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Cu$_{20}$Zr$_{10}$', Pd70Cu20Zr10['adsry'].mean(),yerr=Pd70Cu20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Zr$_{10}$',color='0.6', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Zr$_{20}$Ag$_{10}$', Pd70Zr20Ag10['adsry'].mean(),yerr=Pd70Zr20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Zr$_{20}$Ag$_{10}$',color='0.3', edgecolor='black', hatch='+')
        
        ax.set(xlabel="Simulated metal")
        ax.set(ylabel="Adsorption energy (Ry)")
        ax.axes.xaxis.set_visible(False)
        fig.suptitle('Hydrogen adsorption', fontsize=24)
        ax.autoscale(tight=False)
        plt.legend()
        fig.show()
        fig.savefig('h2ads.jpg', dpi=300)



H2_graphs()
#######################################################################################################
## CO #################################################################################################
#######################################################################################################
def CO_graphs():

    df = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/CO_adsorption.csv')

    df

    dfH2 = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/Hydrogen_adsorption.csv')

    dfH2

    df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))
    dfH2['adsry'] = dfH2['Adsorption energy(kJ)'] /(2.179872*10**(-21))


    isPd = df['Metal'] == 'Pd'
    isPdAu10 = df['Metal'] == 'PdAu10'
    isPdAg23 = df['Metal'] == 'PdAg23'
    isPd80Cu20 = df['Metal'] == 'Pd80Cu20'
    isPd60Cu40 = df['Metal'] == 'Pd60Cu40'
    isPdAu20 = df['Metal'] == 'PdAu20'
    isPdZr10 = df['Metal'] == 'PdZr10'
    isPdZr20 = df['Metal'] == 'PdZr20'
    isPd70Au20Ag10 = df['Metal'] == 'Pd70Au20Ag10'


    PD = df[isPd]
    PDAu10 = df[isPdAu10]
    PdAg23 = df[isPdAg23]
    Pd80Cu20 = df[isPd80Cu20]
    Pd60Cu40 = df[isPd60Cu40]
    PdAu20 = df[isPdAu20]
    PdZr10 = df[isPdZr10]
    PdZr20 = df[isPdZr20]
    Pd70Au20Ag10 = df[isPd70Au20Ag10]
    Pd70Au20Cu10 = df[ df['Metal'] == 'Pd70Au20Cu10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Ag10 = df[ df['Metal'] == 'Pd70Cu20Ag10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Zr10 = df[ df['Metal'] == 'Pd70Cu20Zr10']
    Pd70Zr20Ag10 = df[ df['Metal'] == 'Pd70Zr20Ag10']

    h2PD = dfH2[ dfH2['Metal'] == 'Pd']
    h2PDAu10 = dfH2[ dfH2['Metal'] == 'PdAu10']
    h2PdAg23 = dfH2[ dfH2['Metal'] == 'PdAg23']
    h2Pd80Cu20 = dfH2[ dfH2['Metal'] == 'Pd80Cu20']
    h2Pd60Cu40 = dfH2[ dfH2['Metal'] == 'Pd60Cu40']
    h2PdAu20 = dfH2[ dfH2['Metal'] == 'PdAu20']
    h2PdZr10 = dfH2[ dfH2['Metal'] == 'PdZr10']
    h2PdZr20 = dfH2[ dfH2['Metal'] == 'PdZr20']
    h2Pd70Au20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Ag10']
    h2Pd70Au20Cu10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Cu10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Ag10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Zr10']
    h2Pd70Zr20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Zr20Ag10']


    PD

    PDAu10
    PDAu10['adsry'].std()

    # spl = make_interp_spline(x, data, k=3)  # type: BSpline
    # power_smooth = spl(x_new)



    plt.style.use('science')


    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(6,5))
        ax.plot(PD['Site'], PD['adsry'], label='CO', color='black', marker='D', linestyle='dashed' )
        ax.plot(h2PD['Site'], h2PD['adsry'], label='H', color='black', marker='D' )

        

        ax.set(xlabel="Adsorption site")
        ax.set(ylabel="Adsorption energy (eV)")
        fig.suptitle('CO adsorption sites on Pd compared to H', fontsize=14)
        ax.autoscale(tight=False)
        plt.legend()

        fig.show()

        fig.savefig('COSites.jpg', dpi=300)

    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(15,8))
        ax.bar('Pd', PD['adsry'].mean(),yerr=PDAu10['adsry'].sem(), width=1, label='Pd', color='white', edgecolor='black',)
        ax.bar('PdAu$_{10}$', PDAu10['adsry'].mean(),yerr=PDAu10['adsry'].sem(),width=1,zorder=1, label='PdAu$_{10}$', color='0.8', edgecolor='black')
        ax.bar('PdAu$_{20}$', PdAu20['adsry'].mean(),yerr=PdAu20['adsry'].sem(),width=1,zorder=1, label='PdAu$_{20}$',color='0.6', edgecolor='black')
        ax.bar('PdAg$_{23}$', PdAg23['adsry'].mean(),yerr=PdAg23['adsry'].sem(),width=1,zorder=1, label='PdAg$_{23}$',color='0.3', edgecolor='black')
        ax.bar('Pd$_{80}$Cu$_{20}$', Pd80Cu20['adsry'].mean(),yerr=Pd80Cu20['adsry'].sem(),width=1,zorder=1, label='Pd$_{80}$Cu$_{20}$',color='0.8', edgecolor='black', hatch='//')
        ax.bar('Pd$_{60}$Cu$_{40}$', Pd60Cu40['adsry'].mean(),yerr=Pd60Cu40['adsry'].sem(),width=1,zorder=1, label='Pd$_{60}$Cu$_{40}$', color='0.6', edgecolor='black', hatch='+')
        ax.bar('PdZr$_{10}$', PdZr10['adsry'].mean(),yerr=PdZr10['adsry'].sem(),width=1,zorder=1, label='PdZr$_{10}$',color='0.3', edgecolor='black', hatch='*')
        ax.bar('PdZr$_{20}$', PdZr20['adsry'].mean(),yerr=PdZr20['adsry'].sem(),width=1,zorder=1, label='PdZr$_{20}$',color='1', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Au$_{20}$Ag$_{10}$', Pd70Au20Ag10['adsry'].mean(),yerr=Pd70Au20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='+')
        ax.bar('Pd$_{70}$Au$_{20}$Cu$_{10}$', Pd70Au20Cu10['adsry'].mean(),yerr=Pd70Au20Cu10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Cu$_{10}$',color='0.6', edgecolor='black', hatch='*')
        ax.bar('Pd$_{70}$Au$_{20}$Zr$_{10}$', -Pd70Au20Zr10['adsry'].mean(),yerr=Pd70Au20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Zr$_{10}$',color='0.3', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Cu$_{20}$Ag$_{10}$', -Pd70Cu20Ag10['adsry'].mean(),yerr=Pd70Cu20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Cu$_{20}$Zr$_{10}$', Pd70Cu20Zr10['adsry'].mean(),yerr=Pd70Cu20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Zr$_{10}$',color='0.6', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Zr$_{20}$Ag$_{10}$', -Pd70Zr20Ag10['adsry'].mean(),yerr=Pd70Zr20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Zr$_{20}$Ag$_{10}$',color='0.3', edgecolor='black', hatch='+')
        
        ax.scatter('Pd', h2PD['adsry'].mean(),color='red', zorder=2, label='Average H $E_{ads}$')
        ax.scatter('PdAu$_{10}$', h2PDAu10['adsry'].mean(),color='red', zorder=2)
        ax.scatter('PdAu$_{20}$', h2PdAu20['adsry'].mean(), color='red', zorder=2)
        ax.scatter('PdAg$_{23}$', h2PdAg23['adsry'].mean(),color='red', zorder=2)
        ax.scatter('Pd$_{80}$Cu$_{20}$', h2Pd80Cu20['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{60}$Cu$_{40}$', h2Pd60Cu40['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('PdZr$_{10}$', h2PdZr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('PdZr$_{20}$', h2PdZr20['adsry'].mean(),color='red', zorder=2)
        ax.scatter('Pd$_{70}$Au$_{20}$Ag$_{10}$', h2Pd70Au20Ag10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Au$_{20}$Cu$_{10}$', h2Pd70Au20Cu10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Au$_{20}$Zr$_{10}$', h2Pd70Au20Zr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Cu$_{20}$Ag$_{10}$', h2Pd70Cu20Ag10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Cu$_{20}$Zr$_{10}$', h2Pd70Cu20Zr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Zr$_{20}$Ag$_{10}$', h2Pd70Zr20Ag10['adsry'].mean(),color='red', zorder=2, )

        ax.set(xlabel="Simulated metal")
        ax.set(ylabel="Adsorption energy (eV)")
        ax.axes.xaxis.set_visible(False)
        fig.suptitle('CO adsorption', fontsize=24)
        ax.autoscale(tight=False)
        plt.ylim(-1.5, 0.25)
        plt.legend()
        fig.show()
        fig.savefig('COads.jpg', dpi=300)

CO_graphs()

def H2S_graphs():

    df = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/h2S_adsorption.csv')

    dfH2 = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/Hydrogen_adsorption.csv')

    dfH2

    df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))
    dfH2['adsry'] = dfH2['Adsorption energy(kJ)'] /(2.179872*10**(-21))

    isPd = df['Metal'] == 'Pd'
    isPdAu10 = df['Metal'] == 'PdAu10'
    isPdAg23 = df['Metal'] == 'PdAg23'
    isPd80Cu20 = df['Metal'] == 'Pd80Cu20'
    isPd60Cu40 = df['Metal'] == 'Pd60Cu40'
    isPdAu20 = df['Metal'] == 'PdAu20'
    isPdZr10 = df['Metal'] == 'PdZr10'
    isPdZr20 = df['Metal'] == 'PdZr20'
    isPd70Au20Ag10 = df['Metal'] == 'Pd70Au20Ag10'


    PD = df[isPd]
    PDAu10 = df[isPdAu10]
    PdAg23 = df[isPdAg23]
    Pd80Cu20 = df[isPd80Cu20]
    Pd60Cu40 = df[isPd60Cu40]
    PdAu20 = df[isPdAu20]
    PdZr10 = df[isPdZr10]
    PdZr20 = df[isPdZr20]
    Pd70Au20Ag10 = df[isPd70Au20Ag10]
    Pd70Au20Cu10 = df[ df['Metal'] == 'Pd70Au20Cu10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Ag10 = df[ df['Metal'] == 'Pd70Cu20Ag10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Zr10 = df[ df['Metal'] == 'Pd70Cu20Zr10']
    Pd70Zr20Ag10 = df[ df['Metal'] == 'Pd70Zr20Ag10']
    h2PD = dfH2[ dfH2['Metal'] == 'Pd']
    h2PDAu10 = dfH2[ dfH2['Metal'] == 'PdAu10']
    h2PdAg23 = dfH2[ dfH2['Metal'] == 'PdAg23']
    h2Pd80Cu20 = dfH2[ dfH2['Metal'] == 'Pd80Cu20']
    h2Pd60Cu40 = dfH2[ dfH2['Metal'] == 'Pd60Cu40']
    h2PdAu20 = dfH2[ dfH2['Metal'] == 'PdAu20']
    h2PdZr10 = dfH2[ dfH2['Metal'] == 'PdZr10']
    h2PdZr20 = dfH2[ dfH2['Metal'] == 'PdZr20']
    h2Pd70Au20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Ag10']
    h2Pd70Au20Cu10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Cu10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Ag10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Zr10']
    h2Pd70Zr20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Zr20Ag10']

    PD

    PDAu10

    # spl = make_interp_spline(x, data, k=3)  # type: BSpline
    # power_smooth = spl(x_new)



    plt.style.use('science')


    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(15,8))
        ax.bar('Pd', PD['adsry'].mean(),yerr=PDAu10['adsry'].sem(), width=1, label='Pd', color='white', edgecolor='black',)
        ax.bar('PdAu$_{10}$', PDAu10['adsry'].mean(),yerr=PDAu10['adsry'].sem(),width=1,zorder=1, label='PdAu$_{10}$', color='0.8', edgecolor='black')
        ax.bar('PdAu$_{20}$', PdAu20['adsry'].mean(),yerr=PdAu20['adsry'].sem(),width=1,zorder=1, label='PdAu$_{20}$',color='0.6', edgecolor='black')
        ax.bar('PdAg$_{23}$', PdAg23['adsry'].mean(),yerr=PdAg23['adsry'].sem(),width=1,zorder=1, label='PdAg$_{23}$',color='0.3', edgecolor='black')
        ax.bar('Pd$_{80}$Cu$_{20}$', Pd80Cu20['adsry'].mean(),yerr=Pd80Cu20['adsry'].sem(),width=1,zorder=1, label='Pd$_{80}$Cu$_{20}$',color='0.8', edgecolor='black', hatch='//')
        ax.bar('Pd$_{60}$Cu$_{40}$', Pd60Cu40['adsry'].mean(),yerr=Pd60Cu40['adsry'].sem(),width=1,zorder=1, label='Pd$_{60}$Cu$_{40}$', color='0.6', edgecolor='black', hatch='+')
        ax.bar('PdZr$_{10}$', PdZr10['adsry'].mean(),yerr=PdZr10['adsry'].sem(),width=1,zorder=1, label='PdZr$_{10}$',color='0.3', edgecolor='black', hatch='*')
        ax.bar('PdZr$_{20}$', PdZr20['adsry'].mean(),yerr=PdZr20['adsry'].sem(),width=1,zorder=1, label='PdZr$_{20}$',color='1', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Au$_{20}$Ag$_{10}$', Pd70Au20Ag10['adsry'].mean(),yerr=Pd70Au20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='+')
        ax.bar('Pd$_{70}$Au$_{20}$Cu$_{10}$', Pd70Au20Cu10['adsry'].mean(),yerr=Pd70Au20Cu10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Cu$_{10}$',color='0.6', edgecolor='black', hatch='*')
        ax.bar('Pd$_{70}$Au$_{20}$Zr$_{10}$', -Pd70Au20Zr10['adsry'].mean(),yerr=Pd70Au20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Zr$_{10}$',color='0.3', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Cu$_{20}$Ag$_{10}$', -Pd70Cu20Ag10['adsry'].mean(),yerr=Pd70Cu20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Cu$_{20}$Zr$_{10}$', Pd70Cu20Zr10['adsry'].mean(),yerr=Pd70Cu20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Zr$_{10}$',color='0.6', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Zr$_{20}$Ag$_{10}$', -Pd70Zr20Ag10['adsry'].mean(),yerr=Pd70Zr20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Zr$_{20}$Ag$_{10}$',color='0.3', edgecolor='black', hatch='+')
        
        ax.scatter('Pd', h2PD['adsry'].mean(),color='red', zorder=2, label='Average H $E_{ads}$')
        ax.scatter('PdAu$_{10}$', h2PDAu10['adsry'].mean(),color='red', zorder=2)
        ax.scatter('PdAu$_{20}$', h2PdAu20['adsry'].mean(), color='red', zorder=2)
        ax.scatter('PdAg$_{23}$', h2PdAg23['adsry'].mean(),color='red', zorder=2)
        ax.scatter('Pd$_{80}$Cu$_{20}$', h2Pd80Cu20['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{60}$Cu$_{40}$', h2Pd60Cu40['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('PdZr$_{10}$', h2PdZr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('PdZr$_{20}$', h2PdZr20['adsry'].mean(),color='red', zorder=2)
        ax.scatter('Pd$_{70}$Au$_{20}$Ag$_{10}$', h2Pd70Au20Ag10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Au$_{20}$Cu$_{10}$', h2Pd70Au20Cu10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Au$_{20}$Zr$_{10}$', h2Pd70Au20Zr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Cu$_{20}$Ag$_{10}$', h2Pd70Cu20Ag10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Cu$_{20}$Zr$_{10}$', h2Pd70Cu20Zr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Zr$_{20}$Ag$_{10}$', h2Pd70Zr20Ag10['adsry'].mean(),color='red', zorder=2, )

        ax.set(xlabel="Simulated metal")
        ax.set(ylabel="Adsorption energy (Ry)")
        ax.axes.xaxis.set_visible(False)
        fig.suptitle('H$_2$S adsorption', fontsize=24)
        ax.autoscale(tight=False)
        plt.legend()
        fig.show()
        fig.savefig('H2Sads.jpg', dpi=300)

H2S_graphs()

def CO2_graphs():

    df = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/CO2_adsorption.csv')

    df

    df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))

    isPd = df['Metal'] == 'Pd'
    isPdAu10 = df['Metal'] == 'PdAu10'
    isPdAg23 = df['Metal'] == 'PdAg23'
    isPd80Cu20 = df['Metal'] == 'Pd80Cu20'
    isPd60Cu40 = df['Metal'] == 'Pd60Cu40'
    isPdAu20 = df['Metal'] == 'PdAu20'
    isPdZr10 = df['Metal'] == 'PdZr10'
    isPdZr20 = df['Metal'] == 'PdZr20'
    isPd70Au20Ag10 = df['Metal'] == 'Pd70Au20Ag10'


    PD = df[isPd]
    PDAu10 = df[isPdAu10]
    PdAg23 = df[isPdAg23]
    Pd80Cu20 = df[isPd80Cu20]
    Pd60Cu40 = df[isPd60Cu40]
    PdAu20 = df[isPdAu20]
    PdZr10 = df[isPdZr10]
    PdZr20 = df[isPdZr20]
    Pd70Au20Ag10 = df[isPd70Au20Ag10]
    Pd70Au20Cu10 = df[ df['Metal'] == 'Pd70Au20Cu10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Ag10 = df[ df['Metal'] == 'Pd70Cu20Ag10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Zr10 = df[ df['Metal'] == 'Pd70Cu20Zr10']
    Pd70Zr20Ag10 = df[ df['Metal'] == 'Pd70Zr20Ag10']


    PD

    PDAu10

    # spl = make_interp_spline(x, data, k=3)  # type: BSpline
    # power_smooth = spl(x_new)



    plt.style.use('science')


    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(11,8))
        ax.bar('Pd', PD['adsry'].mean(),yerr=PDAu10['adsry'].sem(), width=1, label='Pd', color='white', edgecolor='black',)
        ax.bar('PdAu$_{10}$', PDAu10['adsry'].mean(),yerr=PDAu10['adsry'].sem(),width=1,zorder=1, label='PdAu$_{10}$', color='0.8', edgecolor='black')
        ax.bar('PdAu$_{20}$', PdAu20['adsry'].mean(),yerr=PdAu20['adsry'].sem(),width=1,zorder=1, label='PdAu$_{20}$',color='0.6', edgecolor='black')
        ax.bar('PdAg$_{23}$', PdAg23['adsry'].mean(),yerr=PdAg23['adsry'].sem(),width=1,zorder=1, label='PdAg$_{23}$',color='0.3', edgecolor='black')
        ax.bar('Pd$_{80}$Cu$_{20}$', Pd80Cu20['adsry'].mean(),yerr=Pd80Cu20['adsry'].sem(),width=1,zorder=1, label='Pd$_{80}$Cu$_{20}$',color='0.8', edgecolor='black', hatch='//')
        ax.bar('Pd$_{60}$Cu$_{40}$', Pd60Cu40['adsry'].mean(),yerr=Pd60Cu40['adsry'].sem(),width=1,zorder=1, label='Pd$_{60}$Cu$_{40}$', color='0.6', edgecolor='black', hatch='+')
        ax.bar('PdZr$_{10}$', PdZr10['adsry'].mean(),yerr=PdZr10['adsry'].sem(),width=1,zorder=1, label='PdZr$_{10}$',color='0.3', edgecolor='black', hatch='*')
        ax.bar('PdZr$_{20}$', PdZr20['adsry'].mean(),yerr=PdZr20['adsry'].sem(),width=1,zorder=1, label='PdZr$_{20}$',color='1', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Au$_{20}$Ag$_{10}$', Pd70Au20Ag10['adsry'].mean(),yerr=Pd70Au20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='+')
        ax.bar('Pd$_{70}$Au$_{20}$Cu$_{10}$', Pd70Au20Cu10['adsry'].mean(),yerr=Pd70Au20Cu10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Cu$_{10}$',color='0.6', edgecolor='black', hatch='*')
        ax.bar('Pd$_{70}$Au$_{20}$Zr$_{10}$', Pd70Au20Zr10['adsry'].mean(),yerr=Pd70Au20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Zr$_{10}$',color='0.3', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Cu$_{20}$Ag$_{10}$', Pd70Cu20Ag10['adsry'].mean(),yerr=Pd70Cu20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Cu$_{20}$Zr$_{10}$', Pd70Cu20Zr10['adsry'].mean(),yerr=Pd70Cu20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Zr$_{10}$',color='0.6', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Zr$_{20}$Ag$_{10}$', Pd70Zr20Ag10['adsry'].mean(),yerr=Pd70Zr20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Zr$_{20}$Ag$_{10}$',color='0.3', edgecolor='black', hatch='+')
        

        ax.set(xlabel="Simulated metal")
        ax.set(ylabel="Adsorption energy (Ry)")
        ax.axes.xaxis.set_visible(False)
        fig.suptitle('CO$_2$ adsorption', fontsize=24)
        ax.autoscale(tight=False)
        plt.legend()
        fig.show()
        fig.savefig('CO2ads.jpg', dpi=300)

CO2_graphs()

def Ar_graphs():

    df = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/Ar_adsorption.csv')

    df

    df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))

    isPd = df['Metal'] == 'Pd'
    isPdAu10 = df['Metal'] == 'PdAu10'
    isPdAg23 = df['Metal'] == 'PdAg23'
    isPd80Cu20 = df['Metal'] == 'Pd80Cu20'
    isPd60Cu40 = df['Metal'] == 'Pd60Cu40'
    isPdAu20 = df['Metal'] == 'PdAu20'
    isPdZr10 = df['Metal'] == 'PdZr10'
    isPdZr20 = df['Metal'] == 'PdZr20'
    isPd70Au20Ag10 = df['Metal'] == 'Pd70Au20Ag10'


    PD = df[isPd]
    PDAu10 = df[isPdAu10]
    PdAg23 = df[isPdAg23]
    Pd80Cu20 = df[isPd80Cu20]
    Pd60Cu40 = df[isPd60Cu40]
    PdAu20 = df[isPdAu20]
    PdZr10 = df[isPdZr10]
    PdZr20 = df[isPdZr20]
    Pd70Au20Ag10 = df[isPd70Au20Ag10]
    Pd70Au20Cu10 = df[ df['Metal'] == 'Pd70Au20Cu10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Ag10 = df[ df['Metal'] == 'Pd70Cu20Ag10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Zr10 = df[ df['Metal'] == 'Pd70Cu20Zr10']
    Pd70Zr20Ag10 = df[ df['Metal'] == 'Pd70Zr20Ag10']


    PD

    PDAu10

    # spl = make_interp_spline(x, data, k=3)  # type: BSpline
    # power_smooth = spl(x_new)



    plt.style.use('science')


    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(11,8))
        ax.bar('Pd', PD['adsry'].mean(),yerr=PDAu10['adsry'].sem(), width=1, label='Pd', color='white', edgecolor='black',)
        ax.bar('PdAu$_{10}$', PDAu10['adsry'].mean(),yerr=PDAu10['adsry'].sem(),width=1,zorder=1, label='PdAu$_{10}$', color='0.8', edgecolor='black')
        ax.bar('PdAu$_{20}$', PdAu20['adsry'].mean(),yerr=PdAu20['adsry'].sem(),width=1,zorder=1, label='PdAu$_{20}$',color='0.6', edgecolor='black')
        ax.bar('PdAg$_{23}$', PdAg23['adsry'].mean(),yerr=PdAg23['adsry'].sem(),width=1,zorder=1, label='PdAg$_{23}$',color='0.3', edgecolor='black')
        ax.bar('Pd$_{80}$Cu$_{20}$', Pd80Cu20['adsry'].mean(),yerr=Pd80Cu20['adsry'].sem(),width=1,zorder=1, label='Pd$_{80}$Cu$_{20}$',color='0.8', edgecolor='black', hatch='//')
        ax.bar('Pd$_{60}$Cu$_{40}$', Pd60Cu40['adsry'].mean(),yerr=Pd60Cu40['adsry'].sem(),width=1,zorder=1, label='Pd$_{60}$Cu$_{40}$', color='0.6', edgecolor='black', hatch='+')
        ax.bar('PdZr$_{10}$', PdZr10['adsry'].mean(),yerr=PdZr10['adsry'].sem(),width=1,zorder=1, label='PdZr$_{10}$',color='0.3', edgecolor='black', hatch='*')
        ax.bar('PdZr$_{20}$', PdZr20['adsry'].mean(),yerr=PdZr20['adsry'].sem(),width=1,zorder=1, label='PdZr$_{20}$',color='1', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Au$_{20}$Ag$_{10}$', Pd70Au20Ag10['adsry'].mean(),yerr=Pd70Au20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='+')
        ax.bar('Pd$_{70}$Au$_{20}$Cu$_{10}$', Pd70Au20Cu10['adsry'].mean(),yerr=Pd70Au20Cu10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Cu$_{10}$',color='0.6', edgecolor='black', hatch='*')
        ax.bar('Pd$_{70}$Au$_{20}$Zr$_{10}$', Pd70Au20Zr10['adsry'].mean(),yerr=Pd70Au20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Zr$_{10}$',color='0.3', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Cu$_{20}$Ag$_{10}$', Pd70Cu20Ag10['adsry'].mean(),yerr=Pd70Cu20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Cu$_{20}$Zr$_{10}$', Pd70Cu20Zr10['adsry'].mean(),yerr=Pd70Cu20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Zr$_{10}$',color='0.6', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Zr$_{20}$Ag$_{10}$', Pd70Zr20Ag10['adsry'].mean(),yerr=Pd70Zr20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Zr$_{20}$Ag$_{10}$',color='0.3', edgecolor='black', hatch='+')
        

        ax.set(xlabel="Simulated metal")
        ax.set(ylabel="Adsorption energy (Ry)")
        ax.axes.xaxis.set_visible(False)
        fig.suptitle('Ar adsorption', fontsize=24)
        ax.autoscale(tight=False)
        plt.legend()
        fig.show()
        fig.savefig('ARads.jpg', dpi=300)

Ar_graphs()

def He_graphs():

    df = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/He_adsorption.csv')

    df

    df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))

    isPd = df['Metal'] == 'Pd'
    isPdAu10 = df['Metal'] == 'PdAu10'
    isPdAg23 = df['Metal'] == 'PdAg23'
    isPd80Cu20 = df['Metal'] == 'Pd80Cu20'
    isPd60Cu40 = df['Metal'] == 'Pd60Cu40'
    isPdAu20 = df['Metal'] == 'PdAu20'
    isPdZr10 = df['Metal'] == 'PdZr10'
    isPdZr20 = df['Metal'] == 'PdZr20'
    isPd70Au20Ag10 = df['Metal'] == 'Pd70Au20Ag10'


    PD = df[isPd]
    PDAu10 = df[isPdAu10]
    PdAg23 = df[isPdAg23]
    Pd80Cu20 = df[isPd80Cu20]
    Pd60Cu40 = df[isPd60Cu40]
    PdAu20 = df[isPdAu20]
    PdZr10 = df[isPdZr10]
    PdZr20 = df[isPdZr20]
    Pd70Au20Ag10 = df[isPd70Au20Ag10]
    Pd70Au20Cu10 = df[ df['Metal'] == 'Pd70Au20Cu10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Ag10 = df[ df['Metal'] == 'Pd70Cu20Ag10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Zr10 = df[ df['Metal'] == 'Pd70Cu20Zr10']
    Pd70Zr20Ag10 = df[ df['Metal'] == 'Pd70Zr20Ag10']


    PD

    PDAu10

    # spl = make_interp_spline(x, data, k=3)  # type: BSpline
    # power_smooth = spl(x_new)



    plt.style.use('science')


    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(11,8))
        ax.bar('Pd', PD['adsry'].mean(),yerr=PDAu10['adsry'].sem(), width=1, label='Pd', color='white', edgecolor='black',)
        ax.bar('PdAu$_{10}$', PDAu10['adsry'].mean(),yerr=PDAu10['adsry'].sem(),width=1,zorder=1, label='PdAu$_{10}$', color='0.8', edgecolor='black')
        ax.bar('PdAu$_{20}$', PdAu20['adsry'].mean(),yerr=PdAu20['adsry'].sem(),width=1,zorder=1, label='PdAu$_{20}$',color='0.6', edgecolor='black')
        ax.bar('PdAg$_{23}$', PdAg23['adsry'].mean(),yerr=PdAg23['adsry'].sem(),width=1,zorder=1, label='PdAg$_{23}$',color='0.3', edgecolor='black')
        ax.bar('Pd$_{80}$Cu$_{20}$', Pd80Cu20['adsry'].mean(),yerr=Pd80Cu20['adsry'].sem(),width=1,zorder=1, label='Pd$_{80}$Cu$_{20}$',color='0.8', edgecolor='black', hatch='//')
        ax.bar('Pd$_{60}$Cu$_{40}$', Pd60Cu40['adsry'].mean(),yerr=Pd60Cu40['adsry'].sem(),width=1,zorder=1, label='Pd$_{60}$Cu$_{40}$', color='0.6', edgecolor='black', hatch='+')
        ax.bar('PdZr$_{10}$', PdZr10['adsry'].mean(),yerr=PdZr10['adsry'].sem(),width=1,zorder=1, label='PdZr$_{10}$',color='0.3', edgecolor='black', hatch='*')
        ax.bar('PdZr$_{20}$', PdZr20['adsry'].mean(),yerr=PdZr20['adsry'].sem(),width=1,zorder=1, label='PdZr$_{20}$',color='1', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Au$_{20}$Ag$_{10}$', Pd70Au20Ag10['adsry'].mean(),yerr=Pd70Au20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='+')
        ax.bar('Pd$_{70}$Au$_{20}$Cu$_{10}$', Pd70Au20Cu10['adsry'].mean(),yerr=Pd70Au20Cu10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Cu$_{10}$',color='0.6', edgecolor='black', hatch='*')
        ax.bar('Pd$_{70}$Au$_{20}$Zr$_{10}$', Pd70Au20Zr10['adsry'].mean(),yerr=Pd70Au20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Zr$_{10}$',color='0.3', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Cu$_{20}$Ag$_{10}$', Pd70Cu20Ag10['adsry'].mean(),yerr=Pd70Cu20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Cu$_{20}$Zr$_{10}$', Pd70Cu20Zr10['adsry'].mean(),yerr=Pd70Cu20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Zr$_{10}$',color='0.6', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Zr$_{20}$Ag$_{10}$', Pd70Zr20Ag10['adsry'].mean(),yerr=Pd70Zr20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Zr$_{20}$Ag$_{10}$',color='0.3', edgecolor='black', hatch='+')
        

        ax.set(xlabel="Simulated metal")
        ax.set(ylabel="Adsorption energy (Ry)")
        ax.axes.xaxis.set_visible(False)
        fig.suptitle('He adsorption', fontsize=24)
        ax.autoscale(tight=False)
        plt.legend()
        fig.show()
        fig.savefig('HEads.jpg', dpi=300)

He_graphs()

def N2_graphs():

    df = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/N2_adsorption.csv')

    df

    df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))

    isPd = df['Metal'] == 'Pd'
    isPdAu10 = df['Metal'] == 'PdAu10'
    isPdAg23 = df['Metal'] == 'PdAg23'
    isPd80Cu20 = df['Metal'] == 'Pd80Cu20'
    isPd60Cu40 = df['Metal'] == 'Pd60Cu40'
    isPdAu20 = df['Metal'] == 'PdAu20'
    isPdZr10 = df['Metal'] == 'PdZr10'
    isPdZr20 = df['Metal'] == 'PdZr20'
    isPd70Au20Ag10 = df['Metal'] == 'Pd70Au20Ag10'


    PD = df[isPd]
    PDAu10 = df[isPdAu10]
    PdAg23 = df[isPdAg23]
    Pd80Cu20 = df[isPd80Cu20]
    Pd60Cu40 = df[isPd60Cu40]
    PdAu20 = df[isPdAu20]
    PdZr10 = df[isPdZr10]
    PdZr20 = df[isPdZr20]
    Pd70Au20Ag10 = df[isPd70Au20Ag10]
    Pd70Au20Cu10 = df[ df['Metal'] == 'Pd70Au20Cu10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Ag10 = df[ df['Metal'] == 'Pd70Cu20Ag10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Zr10 = df[ df['Metal'] == 'Pd70Cu20Zr10']
    Pd70Zr20Ag10 = df[ df['Metal'] == 'Pd70Zr20Ag10']


    PD

    PDAu10

    # spl = make_interp_spline(x, data, k=3)  # type: BSpline
    # power_smooth = spl(x_new)



    plt.style.use('science')


    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(11,8))
        ax.bar('Pd', PD['adsry'].mean(),yerr=PDAu10['adsry'].sem(), width=1, label='Pd', color='white', edgecolor='black',)
        ax.bar('PdAu$_{10}$', PDAu10['adsry'].mean(),yerr=PDAu10['adsry'].sem(),width=1,zorder=1, label='PdAu$_{10}$', color='0.8', edgecolor='black')
        ax.bar('PdAu$_{20}$', PdAu20['adsry'].mean(),yerr=PdAu20['adsry'].sem(),width=1,zorder=1, label='PdAu$_{20}$',color='0.6', edgecolor='black')
        ax.bar('PdAg$_{23}$', PdAg23['adsry'].mean(),yerr=PdAg23['adsry'].sem(),width=1,zorder=1, label='PdAg$_{23}$',color='0.3', edgecolor='black')
        ax.bar('Pd$_{80}$Cu$_{20}$', Pd80Cu20['adsry'].mean(),yerr=Pd80Cu20['adsry'].sem(),width=1,zorder=1, label='Pd$_{80}$Cu$_{20}$',color='0.8', edgecolor='black', hatch='//')
        ax.bar('Pd$_{60}$Cu$_{40}$', Pd60Cu40['adsry'].mean(),yerr=Pd60Cu40['adsry'].sem(),width=1,zorder=1, label='Pd$_{60}$Cu$_{40}$', color='0.6', edgecolor='black', hatch='+')
        ax.bar('PdZr$_{10}$', PdZr10['adsry'].mean(),yerr=PdZr10['adsry'].sem(),width=1,zorder=1, label='PdZr$_{10}$',color='0.3', edgecolor='black', hatch='*')
        ax.bar('PdZr$_{20}$', PdZr20['adsry'].mean(),yerr=PdZr20['adsry'].sem(),width=1,zorder=1, label='PdZr$_{20}$',color='1', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Au$_{20}$Ag$_{10}$', Pd70Au20Ag10['adsry'].mean(),yerr=Pd70Au20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='+')
        ax.bar('Pd$_{70}$Au$_{20}$Cu$_{10}$', Pd70Au20Cu10['adsry'].mean(),yerr=Pd70Au20Cu10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Cu$_{10}$',color='0.6', edgecolor='black', hatch='*')
        ax.bar('Pd$_{70}$Au$_{20}$Zr$_{10}$', Pd70Au20Zr10['adsry'].mean(),yerr=Pd70Au20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Zr$_{10}$',color='0.3', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Cu$_{20}$Ag$_{10}$', Pd70Cu20Ag10['adsry'].mean(),yerr=Pd70Cu20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Cu$_{20}$Zr$_{10}$', Pd70Cu20Zr10['adsry'].mean(),yerr=Pd70Cu20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Zr$_{10}$',color='0.6', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Zr$_{20}$Ag$_{10}$', Pd70Zr20Ag10['adsry'].mean(),yerr=Pd70Zr20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Zr$_{20}$Ag$_{10}$',color='0.3', edgecolor='black', hatch='+')
        

        ax.set(xlabel="Simulated metal")
        ax.set(ylabel="Adsorption energy (Ry)")
        ax.axes.xaxis.set_visible(False)
        fig.suptitle('N$_2$ adsorption', fontsize=24)
        ax.autoscale(tight=False)
        plt.legend()
        fig.show()
        fig.savefig('N2ads.jpg', dpi=300)

N2_graphs()

def NH3_graphs():

    df = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/NH3_adsorption.csv')

    df

    dfH2 = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/Hydrogen_adsorption.csv')

    dfH2

    df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))
    dfH2['adsry'] = dfH2['Adsorption energy(kJ)'] /(2.179872*10**(-21))


    isPd = df['Metal'] == 'Pd'
    isPdAu10 = df['Metal'] == 'PdAu10'
    isPdAg23 = df['Metal'] == 'PdAg23'
    isPd80Cu20 = df['Metal'] == 'Pd80Cu20'
    isPd60Cu40 = df['Metal'] == 'Pd60Cu40'
    isPdAu20 = df['Metal'] == 'PdAu20'
    isPdZr10 = df['Metal'] == 'PdZr10'
    isPdZr20 = df['Metal'] == 'PdZr20'
    isPd70Au20Ag10 = df['Metal'] == 'Pd70Au20Ag10'


    PD = df[isPd]
    PDAu10 = df[isPdAu10]
    PdAg23 = df[isPdAg23]
    Pd80Cu20 = df[isPd80Cu20]
    Pd60Cu40 = df[isPd60Cu40]
    PdAu20 = df[isPdAu20]
    PdZr10 = df[isPdZr10]
    PdZr20 = df[isPdZr20]
    Pd70Au20Ag10 = df[isPd70Au20Ag10]
    Pd70Au20Cu10 = df[ df['Metal'] == 'Pd70Au20Cu10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Ag10 = df[ df['Metal'] == 'Pd70Cu20Ag10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Zr10 = df[ df['Metal'] == 'Pd70Cu20Zr10']
    Pd70Zr20Ag10 = df[ df['Metal'] == 'Pd70Zr20Ag10']

    h2PD = dfH2[ dfH2['Metal'] == 'Pd']
    h2PDAu10 = dfH2[ dfH2['Metal'] == 'PdAu10']
    h2PdAg23 = dfH2[ dfH2['Metal'] == 'PdAg23']
    h2Pd80Cu20 = dfH2[ dfH2['Metal'] == 'Pd80Cu20']
    h2Pd60Cu40 = dfH2[ dfH2['Metal'] == 'Pd60Cu40']
    h2PdAu20 = dfH2[ dfH2['Metal'] == 'PdAu20']
    h2PdZr10 = dfH2[ dfH2['Metal'] == 'PdZr10']
    h2PdZr20 = dfH2[ dfH2['Metal'] == 'PdZr20']
    h2Pd70Au20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Ag10']
    h2Pd70Au20Cu10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Cu10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Ag10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Zr10']
    h2Pd70Zr20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Zr20Ag10']

    PD

    PDAu10
    PDAu10['adsry'].std()

    # spl = make_interp_spline(x, data, k=3)  # type: BSpline
    # power_smooth = spl(x_new)



    plt.style.use('science')


    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(15,8))
        ax.bar('Pd', PD['adsry'].mean(),yerr=PDAu10['adsry'].sem(), width=1, label='Pd', color='white', edgecolor='black',)
        ax.bar('PdAu$_{10}$', PDAu10['adsry'].mean(),yerr=PDAu10['adsry'].sem(),width=1,zorder=1, label='PdAu$_{10}$', color='0.8', edgecolor='black')
        ax.bar('PdAu$_{20}$', PdAu20['adsry'].mean(),yerr=PdAu20['adsry'].sem(),width=1,zorder=1, label='PdAu$_{20}$',color='0.6', edgecolor='black')
        ax.bar('PdAg$_{23}$', PdAg23['adsry'].mean(),yerr=PdAg23['adsry'].sem(),width=1,zorder=1, label='PdAg$_{23}$',color='0.3', edgecolor='black')
        ax.bar('Pd$_{80}$Cu$_{20}$', Pd80Cu20['adsry'].mean(),yerr=Pd80Cu20['adsry'].sem(),width=1,zorder=1, label='Pd$_{80}$Cu$_{20}$',color='0.8', edgecolor='black', hatch='//')
        ax.bar('Pd$_{60}$Cu$_{40}$', Pd60Cu40['adsry'].mean(),yerr=Pd60Cu40['adsry'].sem(),width=1,zorder=1, label='Pd$_{60}$Cu$_{40}$', color='0.6', edgecolor='black', hatch='+')
        ax.bar('PdZr$_{10}$', PdZr10['adsry'].mean(),yerr=PdZr10['adsry'].sem(),width=1,zorder=1, label='PdZr$_{10}$',color='0.3', edgecolor='black', hatch='*')
        ax.bar('PdZr$_{20}$', PdZr20['adsry'].mean(),yerr=PdZr20['adsry'].sem(),width=1,zorder=1, label='PdZr$_{20}$',color='1', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Au$_{20}$Ag$_{10}$', Pd70Au20Ag10['adsry'].mean(),yerr=Pd70Au20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='+')
        ax.bar('Pd$_{70}$Au$_{20}$Cu$_{10}$', Pd70Au20Cu10['adsry'].mean(),yerr=Pd70Au20Cu10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Cu$_{10}$',color='0.6', edgecolor='black', hatch='*')
        ax.bar('Pd$_{70}$Au$_{20}$Zr$_{10}$', Pd70Au20Zr10['adsry'].mean(),yerr=Pd70Au20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Zr$_{10}$',color='0.3', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Cu$_{20}$Ag$_{10}$', Pd70Cu20Ag10['adsry'].mean(),yerr=Pd70Cu20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Cu$_{20}$Zr$_{10}$', Pd70Cu20Zr10['adsry'].mean(),yerr=Pd70Cu20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Zr$_{10}$',color='0.6', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Zr$_{20}$Ag$_{10}$', Pd70Zr20Ag10['adsry'].mean(),yerr=Pd70Zr20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Zr$_{20}$Ag$_{10}$',color='0.3', edgecolor='black', hatch='+')
        
        ax.set(xlabel="Simulated metal")
        ax.set(ylabel="Adsorption energy (Ry)")
        ax.axes.xaxis.set_visible(False)
        fig.suptitle('NH$_3$ adsorption', fontsize=24)
        ax.autoscale(tight=False)
        plt.legend()
        fig.show()
        fig.savefig('NH3ads.jpg', dpi=300)

NH3_graphs()

def Formaldehyde_graphs():

    df = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/Formaldehyde_adsorption.csv')

    dfH2 = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/Hydrogen_adsorption.csv')

    dfH2

    df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))
    dfH2['adsry'] = dfH2['Adsorption energy(kJ)'] /(2.179872*10**(-21))


    isPd = df['Metal'] == 'Pd'
    isPdAu10 = df['Metal'] == 'PdAu10'
    isPdAg23 = df['Metal'] == 'PdAg23'
    isPd80Cu20 = df['Metal'] == 'Pd80Cu20'
    isPd60Cu40 = df['Metal'] == 'Pd60Cu40'
    isPdAu20 = df['Metal'] == 'PdAu20'
    isPdZr10 = df['Metal'] == 'PdZr10'
    isPdZr20 = df['Metal'] == 'PdZr20'
    isPd70Au20Ag10 = df['Metal'] == 'Pd70Au20Ag10'


    PD = df[isPd]
    PDAu10 = df[isPdAu10]
    PdAg23 = df[isPdAg23]
    Pd80Cu20 = df[isPd80Cu20]
    Pd60Cu40 = df[isPd60Cu40]
    PdAu20 = df[isPdAu20]
    PdZr10 = df[isPdZr10]
    PdZr20 = df[isPdZr20]
    Pd70Au20Ag10 = df[isPd70Au20Ag10]
    Pd70Au20Cu10 = df[ df['Metal'] == 'Pd70Au20Cu10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Ag10 = df[ df['Metal'] == 'Pd70Cu20Ag10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Zr10 = df[ df['Metal'] == 'Pd70Cu20Zr10']
    Pd70Zr20Ag10 = df[ df['Metal'] == 'Pd70Zr20Ag10']

    h2PD = dfH2[ dfH2['Metal'] == 'Pd']
    h2PDAu10 = dfH2[ dfH2['Metal'] == 'PdAu10']
    h2PdAg23 = dfH2[ dfH2['Metal'] == 'PdAg23']
    h2Pd80Cu20 = dfH2[ dfH2['Metal'] == 'Pd80Cu20']
    h2Pd60Cu40 = dfH2[ dfH2['Metal'] == 'Pd60Cu40']
    h2PdAu20 = dfH2[ dfH2['Metal'] == 'PdAu20']
    h2PdZr10 = dfH2[ dfH2['Metal'] == 'PdZr10']
    h2PdZr20 = dfH2[ dfH2['Metal'] == 'PdZr20']
    h2Pd70Au20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Ag10']
    h2Pd70Au20Cu10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Cu10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Ag10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Zr10']
    h2Pd70Zr20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Zr20Ag10']

    PD

    PDAu10

    # spl = make_interp_spline(x, data, k=3)  # type: BSpline
    # power_smooth = spl(x_new)



    plt.style.use('science')


    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(15,8))
        ax.bar('Pd', PD['adsry'].mean(),yerr=PDAu10['adsry'].sem(), width=1, label='Pd', color='white', edgecolor='black',)
        ax.bar('PdAu$_{10}$', PDAu10['adsry'].mean(),yerr=PDAu10['adsry'].sem(),width=1,zorder=1, label='PdAu$_{10}$', color='0.8', edgecolor='black')
        ax.bar('PdAu$_{20}$', PdAu20['adsry'].mean(),yerr=PdAu20['adsry'].sem(),width=1,zorder=1, label='PdAu$_{20}$',color='0.6', edgecolor='black')
        ax.bar('PdAg$_{23}$', PdAg23['adsry'].mean(),yerr=PdAg23['adsry'].sem(),width=1,zorder=1, label='PdAg$_{23}$',color='0.3', edgecolor='black')
        ax.bar('Pd$_{80}$Cu$_{20}$', Pd80Cu20['adsry'].mean(),yerr=Pd80Cu20['adsry'].sem(),width=1,zorder=1, label='Pd$_{80}$Cu$_{20}$',color='0.8', edgecolor='black', hatch='//')
        ax.bar('Pd$_{60}$Cu$_{40}$', Pd60Cu40['adsry'].mean(),yerr=Pd60Cu40['adsry'].sem(),width=1,zorder=1, label='Pd$_{60}$Cu$_{40}$', color='0.6', edgecolor='black', hatch='+')
        ax.bar('PdZr$_{10}$', PdZr10['adsry'].mean(),yerr=PdZr10['adsry'].sem(),width=1,zorder=1, label='PdZr$_{10}$',color='0.3', edgecolor='black', hatch='*')
        ax.bar('PdZr$_{20}$', PdZr20['adsry'].mean(),yerr=PdZr20['adsry'].sem(),width=1,zorder=1, label='PdZr$_{20}$',color='1', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Au$_{20}$Ag$_{10}$', Pd70Au20Ag10['adsry'].mean(),yerr=Pd70Au20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='+')
        ax.bar('Pd$_{70}$Au$_{20}$Cu$_{10}$', Pd70Au20Cu10['adsry'].mean(),yerr=Pd70Au20Cu10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Cu$_{10}$',color='0.6', edgecolor='black', hatch='*')
        ax.bar('Pd$_{70}$Au$_{20}$Zr$_{10}$', -Pd70Au20Zr10['adsry'].mean(),yerr=Pd70Au20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Zr$_{10}$',color='0.3', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Cu$_{20}$Ag$_{10}$', -Pd70Cu20Ag10['adsry'].mean(),yerr=Pd70Cu20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Cu$_{20}$Zr$_{10}$', Pd70Cu20Zr10['adsry'].mean(),yerr=Pd70Cu20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Zr$_{10}$',color='0.6', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Zr$_{20}$Ag$_{10}$', -Pd70Zr20Ag10['adsry'].mean(),yerr=Pd70Zr20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Zr$_{20}$Ag$_{10}$',color='0.3', edgecolor='black', hatch='+')
        
        ax.scatter('Pd', h2PD['adsry'].mean(),color='red', zorder=2, label='Average H $E_{ads}$')
        ax.scatter('PdAu$_{10}$', h2PDAu10['adsry'].mean(),color='red', zorder=2)
        ax.scatter('PdAu$_{20}$', h2PdAu20['adsry'].mean(), color='red', zorder=2)
        ax.scatter('PdAg$_{23}$', h2PdAg23['adsry'].mean(),color='red', zorder=2)
        ax.scatter('Pd$_{80}$Cu$_{20}$', h2Pd80Cu20['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{60}$Cu$_{40}$', h2Pd60Cu40['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('PdZr$_{10}$', h2PdZr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('PdZr$_{20}$', h2PdZr20['adsry'].mean(),color='red', zorder=2)
        ax.scatter('Pd$_{70}$Au$_{20}$Ag$_{10}$', h2Pd70Au20Ag10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Au$_{20}$Cu$_{10}$', h2Pd70Au20Cu10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Au$_{20}$Zr$_{10}$', h2Pd70Au20Zr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Cu$_{20}$Ag$_{10}$', h2Pd70Cu20Ag10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Cu$_{20}$Zr$_{10}$', h2Pd70Cu20Zr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Zr$_{20}$Ag$_{10}$', h2Pd70Zr20Ag10['adsry'].mean(),color='red', zorder=2, )

        ax.set(xlabel="Simulated metal")
        ax.set(ylabel="Adsorption energy (Ry)")
        ax.axes.xaxis.set_visible(False)
        fig.suptitle('Formaldehyde adsorption', fontsize=24)
        ax.autoscale(tight=False)
        plt.legend()
        fig.show()
        fig.savefig('Formaldehydeads.jpg', dpi=300)

Formaldehyde_graphs()

def O2_graphs():

    df = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/O2_adsorption.csv')

    df

    dfH2 = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/Hydrogen_adsorption.csv')

    dfH2

    df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))
    dfH2['adsry'] = dfH2['Adsorption energy(kJ)'] /(2.179872*10**(-21))

    isPd = df['Metal'] == 'Pd'
    isPdAu10 = df['Metal'] == 'PdAu10'
    isPdAg23 = df['Metal'] == 'PdAg23'
    isPd80Cu20 = df['Metal'] == 'Pd80Cu20'
    isPd60Cu40 = df['Metal'] == 'Pd60Cu40'
    isPdAu20 = df['Metal'] == 'PdAu20'
    isPdZr10 = df['Metal'] == 'PdZr10'
    isPdZr20 = df['Metal'] == 'PdZr20'
    isPd70Au20Ag10 = df['Metal'] == 'Pd70Au20Ag10'


    PD = df[isPd]
    PDAu10 = df[isPdAu10]
    PdAg23 = df[isPdAg23]
    Pd80Cu20 = df[isPd80Cu20]
    Pd60Cu40 = df[isPd60Cu40]
    PdAu20 = df[isPdAu20]
    PdZr10 = df[isPdZr10]
    PdZr20 = df[isPdZr20]
    Pd70Au20Ag10 = df[isPd70Au20Ag10]
    Pd70Au20Cu10 = df[ df['Metal'] == 'Pd70Au20Cu10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Ag10 = df[ df['Metal'] == 'Pd70Cu20Ag10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Zr10 = df[ df['Metal'] == 'Pd70Cu20Zr10']
    Pd70Zr20Ag10 = df[ df['Metal'] == 'Pd70Zr20Ag10']

    h2PD = dfH2[ dfH2['Metal'] == 'Pd']
    h2PDAu10 = dfH2[ dfH2['Metal'] == 'PdAu10']
    h2PdAg23 = dfH2[ dfH2['Metal'] == 'PdAg23']
    h2Pd80Cu20 = dfH2[ dfH2['Metal'] == 'Pd80Cu20']
    h2Pd60Cu40 = dfH2[ dfH2['Metal'] == 'Pd60Cu40']
    h2PdAu20 = dfH2[ dfH2['Metal'] == 'PdAu20']
    h2PdZr10 = dfH2[ dfH2['Metal'] == 'PdZr10']
    h2PdZr20 = dfH2[ dfH2['Metal'] == 'PdZr20']
    h2Pd70Au20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Ag10']
    h2Pd70Au20Cu10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Cu10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Ag10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Zr10']
    h2Pd70Zr20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Zr20Ag10']

    PD

    PDAu10

    # spl = make_interp_spline(x, data, k=3)  # type: BSpline
    # power_smooth = spl(x_new)



    plt.style.use('science')


    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(15,8))
        ax.bar('Pd', PD['adsry'].mean(),yerr=PDAu10['adsry'].sem(), width=1, label='Pd', color='white', edgecolor='black',)
        ax.bar('PdAu$_{10}$', PDAu10['adsry'].mean(),yerr=PDAu10['adsry'].sem(),width=1,zorder=1, label='PdAu$_{10}$', color='0.8', edgecolor='black')
        ax.bar('PdAu$_{20}$', PdAu20['adsry'].mean(),yerr=PdAu20['adsry'].sem(),width=1,zorder=1, label='PdAu$_{20}$',color='0.6', edgecolor='black')
        ax.bar('PdAg$_{23}$', PdAg23['adsry'].mean(),yerr=PdAg23['adsry'].sem(),width=1,zorder=1, label='PdAg$_{23}$',color='0.3', edgecolor='black')
        ax.bar('Pd$_{80}$Cu$_{20}$', Pd80Cu20['adsry'].mean(),yerr=Pd80Cu20['adsry'].sem(),width=1,zorder=1, label='Pd$_{80}$Cu$_{20}$',color='0.8', edgecolor='black', hatch='//')
        ax.bar('Pd$_{60}$Cu$_{40}$', Pd60Cu40['adsry'].mean(),yerr=Pd60Cu40['adsry'].sem(),width=1,zorder=1, label='Pd$_{60}$Cu$_{40}$', color='0.6', edgecolor='black', hatch='+')
        ax.bar('PdZr$_{10}$', PdZr10['adsry'].mean(),yerr=PdZr10['adsry'].sem(),width=1,zorder=1, label='PdZr$_{10}$',color='0.3', edgecolor='black', hatch='*')
        ax.bar('PdZr$_{20}$', PdZr20['adsry'].mean(),yerr=PdZr20['adsry'].sem(),width=1,zorder=1, label='PdZr$_{20}$',color='1', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Au$_{20}$Ag$_{10}$', Pd70Au20Ag10['adsry'].mean(),yerr=Pd70Au20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='+')
        ax.bar('Pd$_{70}$Au$_{20}$Cu$_{10}$', Pd70Au20Cu10['adsry'].mean(),yerr=Pd70Au20Cu10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Cu$_{10}$',color='0.6', edgecolor='black', hatch='*')
        ax.bar('Pd$_{70}$Au$_{20}$Zr$_{10}$', -Pd70Au20Zr10['adsry'].mean(),yerr=Pd70Au20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Zr$_{10}$',color='0.3', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Cu$_{20}$Ag$_{10}$', -Pd70Cu20Ag10['adsry'].mean(),yerr=Pd70Cu20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Cu$_{20}$Zr$_{10}$', Pd70Cu20Zr10['adsry'].mean(),yerr=Pd70Cu20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Zr$_{10}$',color='0.6', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Zr$_{20}$Ag$_{10}$', -Pd70Zr20Ag10['adsry'].mean(),yerr=Pd70Zr20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Zr$_{20}$Ag$_{10}$',color='0.3', edgecolor='black', hatch='+')
        
        ax.scatter('Pd', h2PD['adsry'].mean(),color='red', zorder=2, label='Average H $E_{ads}$')
        ax.scatter('PdAu$_{10}$', h2PDAu10['adsry'].mean(),color='red', zorder=2)
        ax.scatter('PdAu$_{20}$', h2PdAu20['adsry'].mean(), color='red', zorder=2)
        ax.scatter('PdAg$_{23}$', h2PdAg23['adsry'].mean(),color='red', zorder=2)
        ax.scatter('Pd$_{80}$Cu$_{20}$', h2Pd80Cu20['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{60}$Cu$_{40}$', h2Pd60Cu40['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('PdZr$_{10}$', h2PdZr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('PdZr$_{20}$', h2PdZr20['adsry'].mean(),color='red', zorder=2)
        ax.scatter('Pd$_{70}$Au$_{20}$Ag$_{10}$', h2Pd70Au20Ag10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Au$_{20}$Cu$_{10}$', h2Pd70Au20Cu10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Au$_{20}$Zr$_{10}$', h2Pd70Au20Zr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Cu$_{20}$Ag$_{10}$', h2Pd70Cu20Ag10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Cu$_{20}$Zr$_{10}$', h2Pd70Cu20Zr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Zr$_{20}$Ag$_{10}$', h2Pd70Zr20Ag10['adsry'].mean(),color='red', zorder=2, )


        ax.set(xlabel="Simulated metal")
        ax.set(ylabel="Adsorption energy (Ry)")
        ax.axes.xaxis.set_visible(False)
        fig.suptitle('O$_2$ adsorption', fontsize=24)
        ax.autoscale(tight=False)
        plt.legend()
        fig.show()
        fig.savefig('O2ads.jpg', dpi=300)

O2_graphs()

def FA_graphs():

    df = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/FormicAcid_adsorption.csv')

    df
    
    dfH2 = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/Hydrogen_adsorption.csv')

    dfH2

    df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))
    dfH2['adsry'] = dfH2['Adsorption energy(kJ)'] /(2.179872*10**(-21))

    isPd = df['Metal'] == 'Pd'
    isPdAu10 = df['Metal'] == 'PdAu10'
    isPdAg23 = df['Metal'] == 'PdAg23'
    isPd80Cu20 = df['Metal'] == 'Pd80Cu20'
    isPd60Cu40 = df['Metal'] == 'Pd60Cu40'
    isPdAu20 = df['Metal'] == 'PdAu20'
    isPdZr10 = df['Metal'] == 'PdZr10'
    isPdZr20 = df['Metal'] == 'PdZr20'
    isPd70Au20Ag10 = df['Metal'] == 'Pd70Au20Ag10'


    PD = df[isPd]
    PDAu10 = df[isPdAu10]
    PdAg23 = df[isPdAg23]
    Pd80Cu20 = df[isPd80Cu20]
    Pd60Cu40 = df[isPd60Cu40]
    PdAu20 = df[isPdAu20]
    PdZr10 = df[isPdZr10]
    PdZr20 = df[isPdZr20]
    Pd70Au20Ag10 = df[isPd70Au20Ag10]
    Pd70Au20Cu10 = df[ df['Metal'] == 'Pd70Au20Cu10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Ag10 = df[ df['Metal'] == 'Pd70Cu20Ag10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Zr10 = df[ df['Metal'] == 'Pd70Cu20Zr10']
    Pd70Zr20Ag10 = df[ df['Metal'] == 'Pd70Zr20Ag10']

    h2PD = dfH2[ dfH2['Metal'] == 'Pd']
    h2PDAu10 = dfH2[ dfH2['Metal'] == 'PdAu10']
    h2PdAg23 = dfH2[ dfH2['Metal'] == 'PdAg23']
    h2Pd80Cu20 = dfH2[ dfH2['Metal'] == 'Pd80Cu20']
    h2Pd60Cu40 = dfH2[ dfH2['Metal'] == 'Pd60Cu40']
    h2PdAu20 = dfH2[ dfH2['Metal'] == 'PdAu20']
    h2PdZr10 = dfH2[ dfH2['Metal'] == 'PdZr10']
    h2PdZr20 = dfH2[ dfH2['Metal'] == 'PdZr20']
    h2Pd70Au20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Ag10']
    h2Pd70Au20Cu10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Cu10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Ag10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Zr10']
    h2Pd70Zr20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Zr20Ag10']


    PD

    PDAu10

    # spl = make_interp_spline(x, data, k=3)  # type: BSpline
    # power_smooth = spl(x_new)



    plt.style.use('science')


    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(15,8))
        ax.bar('Pd', PD['adsry'].mean(),yerr=PDAu10['adsry'].sem(), width=1, label='Pd', color='white', edgecolor='black',)
        ax.bar('PdAu$_{10}$', PDAu10['adsry'].mean(),yerr=PDAu10['adsry'].sem(),width=1,zorder=1, label='PdAu$_{10}$', color='0.8', edgecolor='black')
        ax.bar('PdAu$_{20}$', PdAu20['adsry'].mean(),yerr=PdAu20['adsry'].sem(),width=1,zorder=1, label='PdAu$_{20}$',color='0.6', edgecolor='black')
        ax.bar('PdAg$_{23}$', PdAg23['adsry'].mean(),yerr=PdAg23['adsry'].sem(),width=1,zorder=1, label='PdAg$_{23}$',color='0.3', edgecolor='black')
        ax.bar('Pd$_{80}$Cu$_{20}$', Pd80Cu20['adsry'].mean(),yerr=Pd80Cu20['adsry'].sem(),width=1,zorder=1, label='Pd$_{80}$Cu$_{20}$',color='0.8', edgecolor='black', hatch='//')
        ax.bar('Pd$_{60}$Cu$_{40}$', Pd60Cu40['adsry'].mean(),yerr=Pd60Cu40['adsry'].sem(),width=1,zorder=1, label='Pd$_{60}$Cu$_{40}$', color='0.6', edgecolor='black', hatch='+')
        ax.bar('PdZr$_{10}$', PdZr10['adsry'].mean(),yerr=PdZr10['adsry'].sem(),width=1,zorder=1, label='PdZr$_{10}$',color='0.3', edgecolor='black', hatch='*')
        ax.bar('PdZr$_{20}$', PdZr20['adsry'].mean(),yerr=PdZr20['adsry'].sem(),width=1,zorder=1, label='PdZr$_{20}$',color='1', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Au$_{20}$Ag$_{10}$', Pd70Au20Ag10['adsry'].mean(),yerr=Pd70Au20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='+')
        ax.bar('Pd$_{70}$Au$_{20}$Cu$_{10}$', Pd70Au20Cu10['adsry'].mean(),yerr=Pd70Au20Cu10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Cu$_{10}$',color='0.6', edgecolor='black', hatch='*')
        ax.bar('Pd$_{70}$Au$_{20}$Zr$_{10}$', -Pd70Au20Zr10['adsry'].mean(),yerr=Pd70Au20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Zr$_{10}$',color='0.3', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Cu$_{20}$Ag$_{10}$', -Pd70Cu20Ag10['adsry'].mean(),yerr=Pd70Cu20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Cu$_{20}$Zr$_{10}$', Pd70Cu20Zr10['adsry'].mean(),yerr=Pd70Cu20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Zr$_{10}$',color='0.6', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Zr$_{20}$Ag$_{10}$', -Pd70Zr20Ag10['adsry'].mean(),yerr=Pd70Zr20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Zr$_{20}$Ag$_{10}$',color='0.3', edgecolor='black', hatch='+')
        
        ax.scatter('Pd', h2PD['adsry'].mean(),color='red', zorder=2, label='Average H $E_{ads}$')
        ax.scatter('PdAu$_{10}$', h2PDAu10['adsry'].mean(),color='red', zorder=2)
        ax.scatter('PdAu$_{20}$', h2PdAu20['adsry'].mean(), color='red', zorder=2)
        ax.scatter('PdAg$_{23}$', h2PdAg23['adsry'].mean(),color='red', zorder=2)
        ax.scatter('Pd$_{80}$Cu$_{20}$', h2Pd80Cu20['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{60}$Cu$_{40}$', h2Pd60Cu40['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('PdZr$_{10}$', h2PdZr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('PdZr$_{20}$', h2PdZr20['adsry'].mean(),color='red', zorder=2)
        ax.scatter('Pd$_{70}$Au$_{20}$Ag$_{10}$', h2Pd70Au20Ag10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Au$_{20}$Cu$_{10}$', h2Pd70Au20Cu10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Au$_{20}$Zr$_{10}$', h2Pd70Au20Zr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Cu$_{20}$Ag$_{10}$', h2Pd70Cu20Ag10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Cu$_{20}$Zr$_{10}$', h2Pd70Cu20Zr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Zr$_{20}$Ag$_{10}$', h2Pd70Zr20Ag10['adsry'].mean(),color='red', zorder=2, )


        ax.set(xlabel="Simulated metal")
        ax.set(ylabel="Adsorption energy (Ry)")
        ax.axes.xaxis.set_visible(False)
        fig.suptitle('Formic Acid adsorption', fontsize=24)
        ax.autoscale(tight=False)
        plt.legend()
        fig.show()
        fig.savefig('FAads.jpg', dpi=300)

FA_graphs()

def CH4_graphs():

    df = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/CH4_adsorption.csv')

    df
    dfH2 = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/Hydrogen_adsorption.csv')

    dfH2

    df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))
    dfH2['adsry'] = dfH2['Adsorption energy(kJ)'] /(2.179872*10**(-21))

    isPd = df['Metal'] == 'Pd'
    isPdAu10 = df['Metal'] == 'PdAu10'
    isPdAg23 = df['Metal'] == 'PdAg23'
    isPd80Cu20 = df['Metal'] == 'Pd80Cu20'
    isPd60Cu40 = df['Metal'] == 'Pd60Cu40'
    isPdAu20 = df['Metal'] == 'PdAu20'
    isPdZr10 = df['Metal'] == 'PdZr10'
    isPdZr20 = df['Metal'] == 'PdZr20'
    isPd70Au20Ag10 = df['Metal'] == 'Pd70Au20Ag10'


    PD = df[isPd]
    PDAu10 = df[isPdAu10]
    PdAg23 = df[isPdAg23]
    Pd80Cu20 = df[isPd80Cu20]
    Pd60Cu40 = df[isPd60Cu40]
    PdAu20 = df[isPdAu20]
    PdZr10 = df[isPdZr10]
    PdZr20 = df[isPdZr20]
    Pd70Au20Ag10 = df[isPd70Au20Ag10]
    Pd70Au20Cu10 = df[ df['Metal'] == 'Pd70Au20Cu10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Ag10 = df[ df['Metal'] == 'Pd70Cu20Ag10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Zr10 = df[ df['Metal'] == 'Pd70Cu20Zr10']
    Pd70Zr20Ag10 = df[ df['Metal'] == 'Pd70Zr20Ag10']
    h2PD = dfH2[ dfH2['Metal'] == 'Pd']
    h2PDAu10 = dfH2[ dfH2['Metal'] == 'PdAu10']
    h2PdAg23 = dfH2[ dfH2['Metal'] == 'PdAg23']
    h2Pd80Cu20 = dfH2[ dfH2['Metal'] == 'Pd80Cu20']
    h2Pd60Cu40 = dfH2[ dfH2['Metal'] == 'Pd60Cu40']
    h2PdAu20 = dfH2[ dfH2['Metal'] == 'PdAu20']
    h2PdZr10 = dfH2[ dfH2['Metal'] == 'PdZr10']
    h2PdZr20 = dfH2[ dfH2['Metal'] == 'PdZr20']
    h2Pd70Au20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Ag10']
    h2Pd70Au20Cu10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Cu10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Ag10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Zr10']
    h2Pd70Zr20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Zr20Ag10']


    PD

    PDAu10

    # spl = make_interp_spline(x, data, k=3)  # type: BSpline
    # power_smooth = spl(x_new)



    plt.style.use('science')


    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(15,8))
        ax.bar('Pd', PD['adsry'].mean(),yerr=PDAu10['adsry'].sem(), width=1, label='Pd', color='white', edgecolor='black',)
        ax.bar('PdAu$_{10}$', PDAu10['adsry'].mean(),yerr=PDAu10['adsry'].sem(),width=1,zorder=1, label='PdAu$_{10}$', color='0.8', edgecolor='black')
        ax.bar('PdAu$_{20}$', PdAu20['adsry'].mean(),yerr=PdAu20['adsry'].sem(),width=1,zorder=1, label='PdAu$_{20}$',color='0.6', edgecolor='black')
        ax.bar('PdAg$_{23}$', PdAg23['adsry'].mean(),yerr=PdAg23['adsry'].sem(),width=1,zorder=1, label='PdAg$_{23}$',color='0.3', edgecolor='black')
        ax.bar('Pd$_{80}$Cu$_{20}$', Pd80Cu20['adsry'].mean(),yerr=Pd80Cu20['adsry'].sem(),width=1,zorder=1, label='Pd$_{80}$Cu$_{20}$',color='0.8', edgecolor='black', hatch='//')
        ax.bar('Pd$_{60}$Cu$_{40}$', Pd60Cu40['adsry'].mean(),yerr=Pd60Cu40['adsry'].sem(),width=1,zorder=1, label='Pd$_{60}$Cu$_{40}$', color='0.6', edgecolor='black', hatch='+')
        ax.bar('PdZr$_{10}$', PdZr10['adsry'].mean(),yerr=PdZr10['adsry'].sem(),width=1,zorder=1, label='PdZr$_{10}$',color='0.3', edgecolor='black', hatch='*')
        ax.bar('PdZr$_{20}$', PdZr20['adsry'].mean(),yerr=PdZr20['adsry'].sem(),width=1,zorder=1, label='PdZr$_{20}$',color='1', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Au$_{20}$Ag$_{10}$', Pd70Au20Ag10['adsry'].mean(),yerr=Pd70Au20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='+')
        ax.bar('Pd$_{70}$Au$_{20}$Cu$_{10}$', Pd70Au20Cu10['adsry'].mean(),yerr=Pd70Au20Cu10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Cu$_{10}$',color='0.6', edgecolor='black', hatch='*')
        ax.bar('Pd$_{70}$Au$_{20}$Zr$_{10}$', -Pd70Au20Zr10['adsry'].mean(),yerr=Pd70Au20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Zr$_{10}$',color='0.3', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Cu$_{20}$Ag$_{10}$', -Pd70Cu20Ag10['adsry'].mean(),yerr=Pd70Cu20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Cu$_{20}$Zr$_{10}$', Pd70Cu20Zr10['adsry'].mean(),yerr=Pd70Cu20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Zr$_{10}$',color='0.6', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Zr$_{20}$Ag$_{10}$', -Pd70Zr20Ag10['adsry'].mean(),yerr=Pd70Zr20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Zr$_{20}$Ag$_{10}$',color='0.3', edgecolor='black', hatch='+')
        
        ax.scatter('Pd', h2PD['adsry'].mean(),color='red', zorder=2, label='Average H $E_{ads}$')
        ax.scatter('PdAu$_{10}$', h2PDAu10['adsry'].mean(),color='red', zorder=2)
        ax.scatter('PdAu$_{20}$', h2PdAu20['adsry'].mean(), color='red', zorder=2)
        ax.scatter('PdAg$_{23}$', h2PdAg23['adsry'].mean(),color='red', zorder=2)
        ax.scatter('Pd$_{80}$Cu$_{20}$', h2Pd80Cu20['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{60}$Cu$_{40}$', h2Pd60Cu40['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('PdZr$_{10}$', h2PdZr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('PdZr$_{20}$', h2PdZr20['adsry'].mean(),color='red', zorder=2)
        ax.scatter('Pd$_{70}$Au$_{20}$Ag$_{10}$', h2Pd70Au20Ag10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Au$_{20}$Cu$_{10}$', h2Pd70Au20Cu10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Au$_{20}$Zr$_{10}$', h2Pd70Au20Zr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Cu$_{20}$Ag$_{10}$', h2Pd70Cu20Ag10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Cu$_{20}$Zr$_{10}$', h2Pd70Cu20Zr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Zr$_{20}$Ag$_{10}$', h2Pd70Zr20Ag10['adsry'].mean(),color='red', zorder=2, )


        ax.set(xlabel="Simulated metal")
        ax.set(ylabel="Adsorption energy (Ry)")
        ax.axes.xaxis.set_visible(False)
        fig.suptitle('CH4 adsorption', fontsize=24)
        ax.autoscale(tight=False)
        plt.legend()
        fig.show()
        fig.savefig('CH4ads.jpg', dpi=300)

CH4_graphs()

def H2O_graphs():
    df = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/H2O_adsorption.csv')

    dfH2 = pd.read_csv(
        '/Users/marc/Thesis/Chapter3/data/Hydrogen_adsorption.csv')

    dfH2

    df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))
    dfH2['adsry'] = dfH2['Adsorption energy(kJ)'] /(2.179872*10**(-21))


    isPd = df['Metal'] == 'Pd'
    isPdAu10 = df['Metal'] == 'PdAu10'
    isPdAg23 = df['Metal'] == 'PdAg23'
    isPd80Cu20 = df['Metal'] == 'Pd80Cu20'
    isPd60Cu40 = df['Metal'] == 'Pd60Cu40'
    isPdAu20 = df['Metal'] == 'PdAu20'
    isPdZr10 = df['Metal'] == 'PdZr10'
    isPdZr20 = df['Metal'] == 'PdZr20'
    isPd70Au20Ag10 = df['Metal'] == 'Pd70Au20Ag10'


    PD = df[isPd]
    PDAu10 = df[isPdAu10]
    PdAg23 = df[isPdAg23]
    Pd80Cu20 = df[isPd80Cu20]
    Pd60Cu40 = df[isPd60Cu40]
    PdAu20 = df[isPdAu20]
    PdZr10 = df[isPdZr10]
    PdZr20 = df[isPdZr20]
    Pd70Au20Ag10 = df[isPd70Au20Ag10]
    Pd70Au20Cu10 = df[ df['Metal'] == 'Pd70Au20Cu10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Ag10 = df[ df['Metal'] == 'Pd70Cu20Ag10']
    Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
    Pd70Cu20Zr10 = df[ df['Metal'] == 'Pd70Cu20Zr10']
    Pd70Zr20Ag10 = df[ df['Metal'] == 'Pd70Zr20Ag10']


    PD

    PDAu10

    h2PD = dfH2[ dfH2['Metal'] == 'Pd']
    h2PDAu10 = dfH2[ dfH2['Metal'] == 'PdAu10']
    h2PdAg23 = dfH2[ dfH2['Metal'] == 'PdAg23']
    h2Pd80Cu20 = dfH2[ dfH2['Metal'] == 'Pd80Cu20']
    h2Pd60Cu40 = dfH2[ dfH2['Metal'] == 'Pd60Cu40']
    h2PdAu20 = dfH2[ dfH2['Metal'] == 'PdAu20']
    h2PdZr10 = dfH2[ dfH2['Metal'] == 'PdZr10']
    h2PdZr20 = dfH2[ dfH2['Metal'] == 'PdZr20']
    h2Pd70Au20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Ag10']
    h2Pd70Au20Cu10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Cu10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Ag10']
    h2Pd70Au20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Au20Zr10']
    h2Pd70Cu20Zr10 = dfH2[ dfH2['Metal'] == 'Pd70Cu20Zr10']
    h2Pd70Zr20Ag10 = dfH2[ dfH2['Metal'] == 'Pd70Zr20Ag10']

    # spl = make_interp_spline(x, data, k=3)  # type: BSpline
    # power_smooth = spl(x_new)



    plt.style.use('science')


    with plt.style.context(['science']):
        fig, ax = plt.subplots(figsize=(15,8))
        ax.bar('Pd', PD['adsry'].mean(),yerr=PDAu10['adsry'].sem(), width=1, label='Pd', color='white', edgecolor='black',)
        ax.bar('PdAu$_{10}$', PDAu10['adsry'].mean(),yerr=PDAu10['adsry'].sem(),width=1,zorder=1, label='PdAu$_{10}$', color='0.8', edgecolor='black')
        ax.bar('PdAu$_{20}$', PdAu20['adsry'].mean(),yerr=PdAu20['adsry'].sem(),width=1,zorder=1, label='PdAu$_{20}$',color='0.6', edgecolor='black')
        ax.bar('PdAg$_{23}$', PdAg23['adsry'].mean(),yerr=PdAg23['adsry'].sem(),width=1,zorder=1, label='PdAg$_{23}$',color='0.3', edgecolor='black')
        ax.bar('Pd$_{80}$Cu$_{20}$', Pd80Cu20['adsry'].mean(),yerr=Pd80Cu20['adsry'].sem(),width=1,zorder=1, label='Pd$_{80}$Cu$_{20}$',color='0.8', edgecolor='black', hatch='//')
        ax.bar('Pd$_{60}$Cu$_{40}$', Pd60Cu40['adsry'].mean(),yerr=Pd60Cu40['adsry'].sem(),width=1,zorder=1, label='Pd$_{60}$Cu$_{40}$', color='0.6', edgecolor='black', hatch='+')
        ax.bar('PdZr$_{10}$', PdZr10['adsry'].mean(),yerr=PdZr10['adsry'].sem(),width=1,zorder=1, label='PdZr$_{10}$',color='0.3', edgecolor='black', hatch='*')
        ax.bar('PdZr$_{20}$', PdZr20['adsry'].mean(),yerr=PdZr20['adsry'].sem(),width=1,zorder=1, label='PdZr$_{20}$',color='1', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Au$_{20}$Ag$_{10}$', Pd70Au20Ag10['adsry'].mean(),yerr=Pd70Au20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='+')
        ax.bar('Pd$_{70}$Au$_{20}$Cu$_{10}$', Pd70Au20Cu10['adsry'].mean(),yerr=Pd70Au20Cu10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Cu$_{10}$',color='0.6', edgecolor='black', hatch='*')
        ax.bar('Pd$_{70}$Au$_{20}$Zr$_{10}$', Pd70Au20Zr10['adsry'].mean(),yerr=Pd70Au20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Au$_{20}$Zr$_{10}$',color='0.3', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Cu$_{20}$Ag$_{10}$', Pd70Cu20Ag10['adsry'].mean(),yerr=Pd70Cu20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Ag$_{10}$',color='0.8', edgecolor='black', hatch='\\')
        ax.bar('Pd$_{70}$Cu$_{20}$Zr$_{10}$', Pd70Cu20Zr10['adsry'].mean(),yerr=Pd70Cu20Zr10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Cu$_{20}$Zr$_{10}$',color='0.6', edgecolor='black', hatch='//')
        ax.bar('Pd$_{70}$Zr$_{20}$Ag$_{10}$', Pd70Zr20Ag10['adsry'].mean(),yerr=Pd70Zr20Ag10['adsry'].sem(),width=1,zorder=1, label='Pd$_{70}$Zr$_{20}$Ag$_{10}$',color='0.3', edgecolor='black', hatch='+')
        
        ax.scatter('Pd', h2PD['adsry'].mean(),color='red', zorder=2, label='Average H $E_{ads}$')
        ax.scatter('PdAu$_{10}$', h2PDAu10['adsry'].mean(),color='red', zorder=2)
        ax.scatter('PdAu$_{20}$', h2PdAu20['adsry'].mean(), color='red', zorder=2)
        ax.scatter('PdAg$_{23}$', h2PdAg23['adsry'].mean(),color='red', zorder=2)
        ax.scatter('Pd$_{80}$Cu$_{20}$', h2Pd80Cu20['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{60}$Cu$_{40}$', h2Pd60Cu40['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('PdZr$_{10}$', h2PdZr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('PdZr$_{20}$', h2PdZr20['adsry'].mean(),color='red', zorder=2)
        ax.scatter('Pd$_{70}$Au$_{20}$Ag$_{10}$', h2Pd70Au20Ag10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Au$_{20}$Cu$_{10}$', h2Pd70Au20Cu10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Au$_{20}$Zr$_{10}$', h2Pd70Au20Zr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Cu$_{20}$Ag$_{10}$', h2Pd70Cu20Ag10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Cu$_{20}$Zr$_{10}$', h2Pd70Cu20Zr10['adsry'].mean(),color='red', zorder=2, )
        ax.scatter('Pd$_{70}$Zr$_{20}$Ag$_{10}$', h2Pd70Zr20Ag10['adsry'].mean(),color='red', zorder=2, )



        ax.set(xlabel="Simulated metal")
        ax.set(ylabel="Adsorption energy (Ry)")
        ax.axes.xaxis.set_visible(False)
        fig.suptitle('H$_2$O adsorption', fontsize=24)
        ax.autoscale(tight=False)
        plt.legend()
        fig.show()
        fig.savefig('H2Oads.jpg', dpi=300)

H2O_graphs()

# def He_graphs():

#     df = pd.read_csv(
#         '/Users/marc/Thesis/Chapter3/data/Ar_adsorption.csv')

#     df

#     df['adsry'] = df['Adsorption energy(kJ)'] /(2.179872*10**(-21))

#     isPd = df['Metal'] == 'Pd'
#     isPdAu10 = df['Metal'] == 'PdAu10'
#     isPdAg23 = df['Metal'] == 'PdAg23'
#     isPd80Cu20 = df['Metal'] == 'Pd80Cu20'
#     isPd60Cu40 = df['Metal'] == 'Pd60Cu40'
#     isPdAu20 = df['Metal'] == 'PdAu20'
#     isPdZr10 = df['Metal'] == 'PdZr10'
#     isPdZr20 = df['Metal'] == 'PdZr20'
#     isPd70Au20Ag10 = df['Metal'] == 'Pd70Au20Ag10'


#     PD = df[isPd]
#     PDAu10 = df[isPdAu10]
#     PdAg23 = df[isPdAg23]
#     Pd80Cu20 = df[isPd80Cu20]
#     Pd60Cu40 = df[isPd60Cu40]
#     PdAu20 = df[isPdAu20]
#     PdZr10 = df[isPdZr10]
#     PdZr20 = df[isPdZr20]
#     Pd70Au20Ag10 = df[isPd70Au20Ag10]
#     Pd70Au20Cu10 = df[ df['Metal'] == 'Pd70Au20Cu10']
#     Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
#     Pd70Cu20Ag10 = df[ df['Metal'] == 'Pd70Cu20Ag10']
#     Pd70Au20Zr10 = df[ df['Metal'] == 'Pd70Au20Zr10']
#     Pd70Cu20Zr10 = df[ df['Metal'] == 'Pd70Cu20Zr10']
#     Pd70Zr20Ag10 = df[ df['Metal'] == 'Pd70Zr20Ag10']


#     PD

#     PDAu10

#     # spl = make_interp_spline(x, data, k=3)  # type: BSpline
#     # power_smooth = spl(x_new)



#     plt.style.use('science')


#     with plt.style.context(['science']):
#         fig, ax = plt.subplots(figsize=(8,8))
#         ax.plot(PD['Site'], PD['adsry'], label='Pd', linewidth=2)
#         ax.plot(PDAu10['Site'], PDAu10['adsry'], label='PdAu10', linewidth=2)
#         ax.plot(PdAu20['Site'], PdAu20['adsry'], label='PdAu20', linewidth=2)
#         ax.plot(PdAg23['Site'], PdAg23['adsry'], label='PdAg23', linewidth=2)
#         ax.plot(Pd80Cu20['Site'], Pd80Cu20['adsry'], label='Pd80Cu20', linewidth=2)
#         ax.plot(Pd60Cu40['Site'], Pd60Cu40['adsry'], label='Pd60Cu40', linewidth=2)
#         ax.plot(PdZr10['Site'], PdZr10['adsry'], label='PdZr10', linewidth=2)
#         ax.plot(PdZr20['Site'], PdZr20['adsry'], label='PdZr20', linewidth=2)

#         ax.set(xlabel="Adsorption site")
#         ax.set(ylabel="Adsorption energy (Ry)")
#         fig.suptitle('Ar adsorption (Binary)', fontsize=10)
#         ax.autoscale(tight=False)
#         plt.legend(bbox_to_anchor=(1, 1),
#         bbox_transform=plt.gcf().transFigure)
#         fig.show()
#         fig.savefig('h2s_1.jpg', dpi=300)

#     with plt.style.context(['science']):
#         fig, ax = plt.subplots(figsize=(8,8))
#         ax.plot(PD['Site'], PD['adsry'], label='Pd', linewidth=2)
    
#         ax.plot(Pd70Au20Ag10['Site'], Pd70Au20Ag10['adsry'], label='Pd70Au20Ag10', linewidth=2)
#         ax.plot(Pd70Au20Cu10['Site'], Pd70Au20Cu10['adsry'], label='Pd70Au20Cu10', linewidth=2)
#         ax.plot(Pd70Au20Zr10['Site'], Pd70Au20Zr10['adsry'], label='Pd70Au20Zr10', linewidth=2)
#         ax.plot(Pd70Cu20Ag10['Site'], Pd70Cu20Ag10['adsry'], label='Pd70Cu20Ag10', linewidth=2)
#         ax.plot(Pd70Au20Zr10['Site'], Pd70Au20Zr10['adsry'], label='Pd70Au20Zr10', linewidth=2)
#         ax.plot(Pd70Cu20Zr10['Site'], Pd70Cu20Zr10['adsry'], label='Pd70Cu20Zr10', linewidth=2)
#         ax.plot(Pd70Zr20Ag10['Site'], Pd70Zr20Ag10['adsry'], label='Pd70Zr20Ag10', linewidth=2)

#         ax.set(xlabel="Adsorption site")
#         ax.set(ylabel="Adsorption energy (Ry)")
#         fig.suptitle('Ar adsorption (Ternary)', fontsize=10)
#         ax.autoscale(tight=False)
#         plt.legend(bbox_to_anchor=(1, 1),
#         bbox_transform=plt.gcf().transFigure)
#         fig.show()
#         fig.savefig('h2s_2.jpg', dpi=300)

# He_graphs()





# DN34
# B543

# with plt.style.context(['science']):
#     fig, ax = plt.subplots(3, sharex=True, figsize=(8, 11))
#     ax[0].plot(PD['Site'], PD['adsry'], color='black')
#     ax[0].set_title('Pd')
#     ax[0].autoscale(tight=False)

#     ax[1].set_title('PdAu10')
#     ax[1].plot(PDAu10['Site'], PDAu10['adsry'], color='black')
#     ax[1].autoscale(tight=False)

#     ax[2].set_title('PdAg23')
#     ax[2].plot(PdAg23['Site'], PdAg23['adsry'], color='black')
#     ax[2].autoscale(tight=False)

#     fig.suptitle('Hydrogen Adsorption', fontsize=10)

#     plt.xlabel("Adsorption site")
#     plt.ylabel("Adsorption energy(kJ)")
#     fig.show()
#     # fig.savefig('kpoints.jpg', dpi=300)


# # df = pd.read_csv(
# #     '/Users/MarcPlunkett/thesis/Chapter3/data/Hydrogen_adsorption.csv')

# # df


# # isPd = df['Metal'] == 'Pd'
# # isPdAu10 = df['Metal'] == 'PdAu10'

# # PD = df[isPd]
# # PDAu10 = df[isPdAu10]

# # PD

# # PDAu10

# # plt.style.available


# # def set_size(width, fraction=1, subplots=(1, 1)):
# #     """ Set figure dimensions to avoid scaling in LaTeX.

# #     Parameters
# #     ----------
# #     width: float or string
# #             Document width in points, or string of predined document type
# #     fraction: float, optional
# #             Fraction of the width which you wish the figure to occupy
# #     subplots: array-like, optional
# #             The number of rows and columns of subplots.
# #     Returns
# #     -------
# #     fig_dim: tuple
# #             Dimensions of figure in inches
# #     """
# #     if width == 'thesis':
# #         width_pt = 426.79135
# #     elif width == 'beamer':
# #         width_pt = 307.28987
#     elif width == 'pnas':
#         width_pt = 246.09686
#     else:
#         width_pt = width

#     # Width of figure (in pts)
#     fig_width_pt = width_pt * fraction
#     # Convert from pt to inches
#     inches_per_pt = 1 / 72.27

#     # Golden ratio to set aesthetic figure height
#     golden_ratio = (5**.5 - 1) / 2

#     # Figure width in inches
#     fig_width_in = fig_width_pt * inches_per_pt
#     # Figure height in inches
#     fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

#     return (fig_width_in, fig_height_in)


# nice_fonts = {
#     # Use LaTeX to write all text
#     "text.usetex": True,
#     "font.family": "serif",
#     # Use 10pt font in plots, to match 10pt font in document
#     "axes.labelsize": 10,
#     "font.size": 10,
#     # Make the legend/label fonts a little smaller
#     "legend.fontsize": 8,
#     "xtick.labelsize": 8,
#     "ytick.labelsize": 8,
# }

# mpl.rcParams.update(nice_fonts)

# x = np.arange(0, 4, 1)
# fig, ax = plt.subplots(5, 2, figsize=set_size(width='thesis', subplots=(5, 2)))
# y = PD['Adsorption energy(kJ)']
# ax[0, 0].plot(x, y)
# ax[0, 0].set_xlabel('Adsorption site')
# ax[0, 0].set_ylabel('Adsorption energy (kJ)')

# ax[0, 0].set_xticks([0, 1, 2, 3])
# ax[0, 0].set_xticklabels(['FCC', 'HCP', 'Top', 'Bridge'])
# plt.style.use('seaborn-white')
# plt.show()

# fig.savefig('HPd.pdf', format='pdf', bbox_inches='tight')
