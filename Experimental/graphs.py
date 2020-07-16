import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
from random import random


data = [-6654.586+random()*10000,-6654.586+random()*100,-6654.586+random()*10,-6654.586+random()*0.1,-6654.586, -6654.586-random()*0.1, -6654.586-random()*0.01, -6654.586-random()*0.01, -6654.586-random()*0.001, -6654.586-random()*0.01]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_new = np.linspace(1, 10, 20000)

data = [2812.672200403207,
 -1558.900711592671,
 -5553.824989750957,
 -6454.519539066461,
 -6654.586,
 -6654.636371363977,
 -6654.592336277526,
 -6654.592254632649,
 -6654.586233523928,
 -6654.595330804439]

spl = make_interp_spline(x, data, k=3)  # type: BSpline
power_smooth = spl(x_new)



plt.style.use('science')


with plt.style.context(['science']):
    fig, ax = plt.subplots()
    ax.plot(x_new, power_smooth, color='black')
    ax.set(xlabel='K-Points')
    ax.set(ylabel='Total energy (Ry)')
    fig.suptitle('Total energy for MxMxM k-points', fontsize=10)
    ax.autoscale(tight=False)
    fig.show()
    # fig.savefig('figures/fig1.pdf')
    fig.savefig('kpoints.jpg', dpi=300)





