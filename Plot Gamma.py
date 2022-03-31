import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from matplotlib.patches import Polygon
from scipy.stats import uniform


#%% Plotting gamma distribution

def system_range_gamma_pdf(min, max):
    y = gamma.pdf(x, fit_alpha, fit_loc, fit_beta)
    hook_gamma_pdf=stats.gamma.cdf(x=55.5605,a=fit_alpha, loc=fit_loc, scale=fit_beta)

    return hook_gamma_pdf


def plot_unifor(min_srange,max_srange, min_drange, drange):
    pdf_half_consol_10_20 = system_range_gamma_pdf(min_srange, max_srange)
    x, y = uniform_step_axis(min_srange, max_srange, pdf_half_consol_10_20, tol=1000, num_points=1000)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'black', linewidth=2, label='Uniform Distribution')
    ax.set_ylim(bottom=0)
    ax.set_ylim(0, pdf_half_consol_10_20 * 2)
    plt.legend()

    # Shaded region
    ix = np.linspace(min_drange, drange)
    iy = stats.uniform.pdf(x=ix, loc=min_srange, scale=(max_srange - min_srange))
    # iy=iy*np.ones(ix.shape)
    iy = np.max(iy) * np.ones(ix.shape)
    verts = [(min_drange, 0), *zip(ix, iy), (drange, 0)]
    poly = Polygon(verts, facecolor='azure', edgecolor='0.5')
    ax.add_patch(poly)

    plt.xlabel("Support Volume (mm3)", fontsize=12)
    plt.ylabel("Probability \n Density", fontsize=12)

    plt.show()


def uniform_step_axis(start, end, value=1,tol=10000,num_points=100):
    x = np.linspace(start-tol,end+tol,num_points)
    y= uniform_step(x,start,end, value)
    return x,y

def uniform_step(x, start, end, value=1):
    up=np.heaviside(x - start, 0)
    down=np.heaviside(end - x, 0)
    return up * down * value