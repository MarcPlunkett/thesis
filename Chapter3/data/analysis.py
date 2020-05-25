import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv(
    '/Users/MarcPlunkett/thesis/Chapter3/data/Hydrogen_adsorption.csv')

df


isPd = df['Metal'] == 'Pd'
isPdAu10 = df['Metal'] == 'PdAu10'

PD = df[isPd]
PDAu10 = df[isPdAu10]

PD

PDAu10

plt.style.available


def set_size(width, fraction=1, subplots=(1, 1)):
    """ Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float or string
            Document width in points, or string of predined document type
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    subplots: array-like, optional
            The number of rows and columns of subplots.
    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    if width == 'thesis':
        width_pt = 426.79135
    elif width == 'beamer':
        width_pt = 307.28987
    elif width == 'pnas':
        width_pt = 246.09686
    else:
        width_pt = width

    # Width of figure (in pts)
    fig_width_pt = width_pt * fraction
    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    golden_ratio = (5**.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    return (fig_width_in, fig_height_in)


nice_fonts = {
    # Use LaTeX to write all text
    "text.usetex": True,
    "font.family": "serif",
    # Use 10pt font in plots, to match 10pt font in document
    "axes.labelsize": 10,
    "font.size": 10,
    # Make the legend/label fonts a little smaller
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
}

mpl.rcParams.update(nice_fonts)

x = np.arange(0, 4, 1)
fig, ax = plt.subplots(5, 2, figsize=set_size(width='thesis', subplots=(5, 2)))
y = PD['Adsorption energy(kJ)']
ax[0, 0].plot(x, y)
ax[0, 0].set_xlabel('Adsorption site')
ax[0, 0].set_ylabel('Adsorption energy (kJ)')

ax[0, 0].set_xticks([0, 1, 2, 3])
ax[0, 0].set_xticklabels(['FCC', 'HCP', 'Top', 'Bridge'])
plt.style.use('seaborn-white')
plt.show()

fig.savefig('HPd.pdf', format='pdf', bbox_inches='tight')
