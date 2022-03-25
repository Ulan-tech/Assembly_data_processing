import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import uniform
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

LESS = 'LESS'
MODERATE = 'MODERATE'
MORE = 'MORE'

nfrRanges = [
    LESS, MODERATE, MORE
]

UNCONSOL = 'unconsol'
CONSOL = "consol"
HALFCONSOL = 'half_consol'

assemblyTypes = [
    UNCONSOL,
    CONSOL,
    HALFCONSOL

]

nfx1for = {
    LESS: 20,
    MODERATE: 55.561,
    MORE: 75
}

nfx2for = {
    LESS: 2,
    MODERATE: 13.33,
    MORE: 15
}

nfx3for = {
    LESS: 20000,
    MODERATE: 30000,
    MORE: 40000,
}


#%% Main function
def plot_infor(hook_type, nfr1_range, nfr2_range, nfr3_range):
    fit_value = {
        CONSOL: (1, 2, 3)
    }
    fit_alpha, fit_loc, fit_beta = fit_value[hook_type]
    b1=nfx1for[nfr1_range]

    time_range = np.linspace(0, 50, 100)

    gamma_pdf = stats.gamma.pdf(time_range, fit_alpha, fit_loc, fit_beta)
    fig, ax = plt.subplots()
    ax.plot(time_range, gamma_pdf, 'black', linewidth=2, label='Gamma Distribution')
    ax.set_ylim(bottom=0)
    plt.legend()

    # Shaded region
    a=0
    ix = np.linspace(a, b1)
    iy = stats.gamma.pdf(ix, fit_alpha, fit_loc, fit_beta)
    verts = [(a, 0), *zip(ix, iy), (b1, 0)]
    poly = Polygon(verts, facecolor='azure', edgecolor='0.5')
    ax.add_patch(poly)

    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.xaxis.set_ticks_position('bottom')

    #ax.set_xticks([a, b1], labels=['$0$', b1])
    plt.xlabel("Assembly time (s)", fontsize=12)
    plt.ylabel("Probability \n Density", rotation='horizontal', fontsize=12)
    ax.yaxis.set_label_coords(-0.05, 1)

    plt.show()


















def infor_con(hook_type, nfr1_range, nfr2_range, nfr3_range):
    p_nFR1, p_nFR2, p_nFR3 = 0, 0, 0
    assert assemblyTypes.__contains__(hook_type), "Assembly type does not match"

    if hook_type == UNCONSOL:
        data = pd.read_csv("./Data/HookUnconsol.csv")
        data = data[data.Components != "Start"]
        data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S %p')

        if nfr1_range in nfrRanges:
            data['Duration'] = data.Time - data.Time.shift(1)
            data = data[data.Username == data.shift(1).Username]

            data.Duration = (data.Duration / np.timedelta64(1, 's')).astype(float)

            data = data[data.Duration > 0]
            data = data[data.Duration < 500]
            p_nFR1 = nFR1(nfr1_range, data)

        elif nfr2_range in nfrRanges:
            data = data[data.Edges == 8]
            data["L1"] = data.r1 + data.r2 + data.r3+data.r4+data.r5+data.r6
            data["L1"] = data["L1"] * 1000
            p_nFR2 = nFR2(nfr2_range, data)

        elif nfr3_range in nfrRanges:
            p_nFR3 = 1

    elif hook_type == HALFCONSOL:
        data = pd.read_csv('./Data/HookC1.csv')
        data = data[data.Components != "Start"]
        data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S %p')

        if nfr1_range in nfrRanges:
            data['Duration'] = data.Time - data.Time.shift(1)
            data = data[data.Username == data.shift(1).Username]
            data.Duration = (data.Duration / np.timedelta64(1, 's')).astype(float)
            data = data[data.Duration > 0]
            data = data[data.Duration < 500]
            p_nFR1 = nFR1(nfr1_range, data)

        if nfr2_range  in nfrRanges:
            data = data[data.Edges == 5]
            data["L1"] = data.r1 + data.r2 + data.r3
            data["L1"] = data["L1"] * 1000
            p_nFR2 = nFR2(nfr2_range, data)

        if nfr3_range:
            p_nFR3 = nFR3_half_consol(nfr3_range)

    elif hook_type == CONSOL:
        p_nFR1, p_nFR2 = 1.0,  1.0
        p_nFR3 = nFR3_consol(nfr3_range)
    else: raise Exception("Unknown assembly")

    return p_nFR1, p_nFR2, p_nFR3, -math.log(p_nFR1 * p_nFR2 * p_nFR3, 2)


#%% Finding common range of nFR1
def nFR1(nfr_range, data):

    x = nfx1for[nfr_range]

    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(data.Duration)
    p_nFR1 = stats.gamma.cdf(x=x, a=fit_alpha, loc=fit_loc, scale=fit_beta)

    return p_nFR1


#%% Finding common range of nFR2
def nFR2(nfr_range, data):

    x = nfx2for[nfr_range]

    params = stats.lognorm.fit(data.L1)
    p_nFR2 = stats.lognorm.cdf(x=x, s=params[0], loc=params[1], scale=params[2])

    return p_nFR2


#%% nFR3_half_consol
def nFR3_half_consol(nfr_range):

    x=nfx3for[nfr_range]

    p_nFR3 = uniform.cdf(x=x, loc=19932.25, scale=(48762.273-19932.25))\
                 - uniform.cdf(x=19932.25, loc=19932.25, scale=(48762.273-19932.25))

    return p_nFR3


def nFR3_consol(nfr_range):

    x=nfx3for[nfr_range]
    p_nFR3 = uniform.cdf(x=x, loc=31741.781, scale=(43171.249-31741.781))\
                 - uniform.cdf(x=31741.781,loc=31741.781, scale=(43171.249-31741.781))

    return p_nFR3


# results_df = pd.DataFrame()
#
# for cons in ['unconsol', 'half_consol', 'consol']:
#     for btn1 in ['less', 'moderate', 'less']:
#         for btn2 in ['less', 'moderate', 'less']:
#             for btn3 in ['less', 'moderate', 'less']:
#                 p_nFR1, p_nFR2, p_nFR3 = infor_con(cons, btn1, btn2, btn3)
#                 results_df = results_df.append([[cons, btn1, btn2, btn3, p_nFR1, p_nFR2, p_nFR3]], ignore_index=False)
#
# print(results_df.shape)
# results_df.to_excel('results.xlsx')
