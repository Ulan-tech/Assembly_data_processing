import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from matplotlib.patches import Polygon
import pandas as pd
from scipy.stats import gamma



#%% Fitting values
def loadData(filename):
    data = pd.read_csv(filename)
    data = data[data.Components != "Start"]
    data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S %p')
    data['Duration'] = data.Time - data.Time.shift(1)
    data = data[data.Username == data.shift(1).Username]
    data.Duration = (data.Duration / np.timedelta64(1, 's')).astype(float)
    data = data[data.Duration > 0]
    data = data[data.Duration < 500]
    return data

#%% Plotting gamma distribution

def plot_gamma(gamma_drange, data):
    fit_shape, fit_loc, fit_scale = stats.gamma.fit(data.Duration)
    # common_range = stats.gamma.cdf(x=gamma_drange, a=fit_shape, loc=fit_loc, scale=fit_scale)
    x_pdf = np.linspace(0, 200, 1000)
    gamma_pdf=stats.gamma.pdf(x_pdf, a=fit_shape, loc=fit_loc, scale=fit_scale)

    fig, ax = plt.subplots()
    ax.plot(x_pdf, gamma_pdf, 'black', linewidth=2, label='Gamma Distribution')


    # Shaded region
    min_gamma = 0
    ix = np.linspace(0, gamma_drange)
    iy = stats.gamma.pdf(ix,fit_shape,fit_loc,fit_scale)
    verts = [(min_gamma, 0), *zip(ix, iy), (gamma_drange, 0)]
    poly = Polygon(verts, facecolor='azure', edgecolor='0.5')
    ax.add_patch(poly)

    plt.xlabel("Assembly time (s)", fontsize=12)
    plt.ylabel("Probability Density", fontsize=12)
    plt.show()

#%% To illustrate the gamma distribution
# drange = 75
# halfconsol_data = loadData("./Data/HookC1.csv")
# plot_gamma(drange, halfconsol_data)


