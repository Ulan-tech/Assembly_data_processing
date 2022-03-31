import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from matplotlib.patches import Polygon
from scipy.stats import gamma
#%% Fitting values

#%% Plotting gamma distribution

def find_gamma_prob(drange, data):
    fit_shape, fit_loc, fit_scale = stats.gamma.fit(data.Duration)
    hook_gamma_prob=stats.gamma.cdf(x=drange,a=fit_shape, loc=fit_loc, scale=fit_scale)

    return hook_gamma_prob

def plot_gamma(fit_shape, fit_loc, fit_scale, gamma_drange):
    common_range = find_gamma_prob(gamma_drange, data)
    x, y = graph_of_actual_gamma(fit_shape, fit_loc, common_range, tol=1000, num_points=1000)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'black', linewidth=2, label='Uniform Distribution')
    ax.set_ylim(bottom=0)
    ax.set_ylim(0, common_range * 2)
    plt.legend()

    # Shaded region
    ix = np.linspace(fit_scale, gamma_drange)
    iy = stats.gamma.pdf(ix,fit_shape,fit_loc,fit_scale)
    # iy=iy*np.ones(ix.shape)
    iy = np.max(iy) * np.ones(ix.shape)
    verts = [(0, 0), *zip(ix, iy), (gamma_drange, 0)]
    poly = Polygon(verts, facecolor='azure', edgecolor='0.5')
    ax.add_patch(poly)

    plt.xlabel("Support Volume (mm3)", fontsize=12)
    plt.ylabel("Probability \n Density", fontsize=12)

    plt.show()


def graph_of_actual_gamma(start, end, tol=10000, num_points=100):
    x = np.linspace(start-tol,end+tol,num_points)
    y= stats.gamma.pdf(x,start,end, value)
    return x,y

