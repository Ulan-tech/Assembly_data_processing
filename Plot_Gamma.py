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
    gamma_pdf=stats.gamma.pdf(x=gamma_drange, a=fit_shape, loc=fit_loc, scale=fit_scale)
    x, y = graph_of_actual_gamma(fit_shape, fit_loc, gamma_pdf, tol=150, num_points=1000)

    fig, ax = plt.subplots()
    ax.plot(x, gamma_pdf, 'black', linewidth=2, label='Gamma Distribution')
    ax.set_ylim(bottom=0)
    ax.set_ylim(0, gamma_pdf )
    plt.legend()

    min_gamma=0
    # Shaded region
    ix = np.linspace(0, gamma_drange)
    iy = stats.gamma.pdf(ix,fit_shape,fit_loc,fit_scale)
    # iy=iy*np.ones(ix.shape)
    # iy = np.max(iy) * np.ones(ix.shape)
    verts = [(min_gamma, 0), *zip(ix, iy), (gamma_drange, 0)]
    poly = Polygon(verts, facecolor='azure', edgecolor='0.5')
    ax.add_patch(poly)

    plt.xlabel("Assembly time (s)", fontsize=12)
    plt.ylabel("Probability \n Density", fontsize=12)

    plt.show()


def graph_of_actual_gamma (shape, location, scale, tol=150, num_points=1000):
    myu=stats.gamma.mean(*(shape, location, scale))
    x = np.linspace(0, myu + tol, num_points)
    y= stats.gamma.pdf(x, shape, location, scale)
    return x,y


#%% To illustrate the gamma distribution
drange = 75
halfconsol_data = loadData("./Data/HookC1.csv")
plot_gamma(drange, halfconsol_data)


