import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from matplotlib.patches import Polygon
import pandas as pd


#%%
def loadData(filename):
    data = pd.read_csv(filename)
    data = data[data.Components != "Start"]





#%% Lognormal fitting

def plot_lognorm(lognorm_drange, data)
    params=stats.lognorm.fit(data.L1)

    x_pdf=np.linspace(0,40,100)
    lognormal_pdf=stats.lognorm.pdf(x_pdf,s=params[0],loc=params[1],scale=params[2])

    plt.plot(x_pdf, lognormal_pdf, label='Lognorm Distribution')
    plt.legend()
    plt.plot(x,y)

#%% Shaded region
    min_lognorm = 0
    ix=np.linspace(a,lognorm_drange)
    iy=stats.lognorm.pdf(ix,params[0],params[1],params[2])
    verts=[(min_lognorm,0),*zip(ix,iy),(lognorm_drange,0)]
    poly=Polygon(verts,facecolor='peachpuff',edgecolor='0.5')
    ax.add_patch(poly)

    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.xaxis.set_ticks_position('bottom')

    plt.xlabel("Displacement error (mm)", fontsize=12)
    plt.ylabel("Probability \n Density", rotation='horizontal', fontsize=12)
    ax.yaxis.set_label_coords(-0.05,1)

    plt.legend()
    plt.show()



#%% To illustrate the gamma distribution
drange = 13.33
halfconsol_data = loadData("./Data/HookC1.csv")
plot_lognorm(drange, halfconsol_data)