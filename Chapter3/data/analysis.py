import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/marc/Thesis/Chapter3/data/Hydrogen_adsorption.csv')

df


isFCC = df['Site'] == 'FCC'

FCC = df[isFCC]

FCC
plt.plot(FCC['Site'], FCC['Adsorption energy(kJ)'])