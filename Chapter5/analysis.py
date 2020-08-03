import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns;
from scipy.interpolate import make_interp_spline, BSpline
from random import random

plt.rcParams.update({'errorbar.capsize': 2})

df = pd.read_csv(
    '/Users/marc/Thesis/Chapter5/krconc.csv')

df

plt.style.use('science')
with plt.style.context(['science']):
    fig, ax = plt.subplots(figsize=(6,5))
    ax.plot(df['P(bar)'], df['n1L'], label='1L', color='black')
    ax.set(xlabel="Sample fill pressure (bar")
    ax.set(ylabel="Krypton concentration ($\mu$mol/mol)")
    ax.autoscale(tight=False)
    fig.suptitle('1L sample vessel', fontsize=14)

    fig.show()
    fig.savefig('1L.jpg', dpi=300)

with plt.style.context(['science']):
    fig, ax = plt.subplots(figsize=(6,5))
    ax.plot(df['P(bar)'], df['n10L'], color='black')
    ax.set(xlabel="Sample fill pressure (bar")
    ax.set(ylabel="Krypton concentration ($\mu$mol/mol)")
    ax.autoscale(tight=False)
    fig.suptitle('10L sample vessel', fontsize=14)
    fig.show()
    fig.savefig('10L.jpg', dpi=300)

with plt.style.context(['science']):
    fig, ax = plt.subplots(figsize=(6,5))
    ax.plot(df['P(bar)'], df['n50L'], color='black')
    ax.set(xlabel="Sample fill pressure (bar")
    ax.set(ylabel="Krypton concentration ($\mu$mol/mol)")
    ax.autoscale(tight=False)
    fig.suptitle('50L sample vessel', fontsize=14)
    fig.show()
    fig.savefig('50L.jpg', dpi=300)


df = pd.read_csv(
    '/Users/marc/Thesis/Chapter5/TC.csv')

df
x_new = np.linspace(1200, 1260, 20000)


spl1 = make_interp_spline(df['Time'],  df['On Off'], k=3)  # type: BSpline
power_smooth1 = spl1(x_new)

spl2 = make_interp_spline(df['Time'], df['PID'], k=3)  # type: BSpline
power_smooth2 = spl2(x_new)



with plt.style.context(['science']):
    fig, ax = plt.subplots(figsize=(6,5))
    ax.plot(x_new, power_smooth1, color='black', linestyle='dashed', label='On/Off controller')
    ax.plot(x_new, power_smooth2, color='black', label='PID controller')
    ax.set(xlabel="Time (Minutes)")
    ax.set(ylabel="Recorded membrane temperature")
    ax.autoscale(tight=False)
    fig.suptitle('Comparison of control methods for enrichment temperature', fontsize=14)
    plt.legend()
    fig.show()
    fig.savefig('TC.jpg', dpi=300)

