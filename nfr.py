
GAMMA_GRAPH_FILENAME = "gamma.png"
LOG_GRAPH_FILENAME = "log.png"
UNIFORM_GRAPH_FILENAME = "uniform.png"
import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import uniform

from Plot_Gamma import plot_gamma
from Uniform_plot import plot_unifor
from plot_lognorm import plot_lognorm

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
    MORE: 90
}

nfx2for = {
    LESS: 2,
    MODERATE: 13.33,
    MORE: 24
}

nfx3for = {
    LESS: 23000,
    MODERATE: 33000,
    MORE: 43000,
}

datafilenames = {
    UNCONSOL: "./Data/HookUnconsol.csv",
    HALFCONSOL: "./Data/HookC1.csv",
    CONSOL: None
}


edgesOfhook = {
    UNCONSOL: 8,
    HALFCONSOL: 5,
    CONSOL: None
}

def get_duration_data(assembly_type):
    data=  get_data_file(assembly_type)
    if assembly_type == CONSOL:
        return None

    data['Duration'] = data.Time - data.Time.shift(1)
    data = data[data.Username == data.shift(1).Username]
    data.Duration = (data.Duration / np.timedelta64(1, 's')).astype(float)
    data = data[data.Duration > 0]
    data = data[data.Duration < 500]
    return data

def get_disp_data(assembly_type):
    data= get_data_file (assembly_type)
    if assembly_type == CONSOL:
        return None
    # Edge Filter
    edges = edgesOfhook[assembly_type]
    data = data[data.Edges == edges]
    # L1 filter
    if UNCONSOL == assembly_type:
        data["L1"] = data.r1 + data.r2 + data.r3 + data.r4 + data.r5 + data.r6
        data["L1"] = data["L1"] * 1000
    elif HALFCONSOL == assembly_type:
        data["L1"] = data.r1 + data.r2 + data.r3
        data["L1"] = data["L1"] * 1000
    return data

def get_data_file (assembly_type):
    file_name = datafilenames[assembly_type]
    if file_name == None:
        return None
    data = pd.read_csv(file_name)
    data = data[data.Components != "Start"]
    data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S %p')
    return data





def infor_con(hook_type, nfr1_range, nfr2_range, nfr3_range):

    assert assemblyTypes.__contains__(hook_type), "Assembly type does not match"
    p_nFR1 = nFR1(nfr1_range, hook_type)
    p_nFR2 = nFR2(nfr2_range, hook_type)
    p_nFR3 = nFR3(nfr3_range, hook_type)


    try:
        information_con = -math.log(p_nFR1 * p_nFR2 * p_nFR3, 2)
    except:
        information_con = "Infinite"

    return p_nFR1, p_nFR2, p_nFR3, information_con



#%% Finding common range of nFR1
def nFR1(nfr_range, assembly_type):
    if CONSOL == assembly_type:
        return 1.0
    data=get_duration_data(assembly_type)
    x = nfx1for[nfr_range]

    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(data.Duration)
    p_nFR1 = stats.gamma.cdf(x=x, a=fit_alpha, loc=fit_loc, scale=fit_beta)

    return p_nFR1


#%% Finding common range of nFR2
def nFR2(nfr_range, assembly_type):
    if CONSOL == assembly_type:
        return 1.0
    data = get_disp_data(assembly_type)
    x = nfx2for[nfr_range]

    params = stats.lognorm.fit(data.L1)
    p_nFR2 = stats.lognorm.cdf(x=x, s=params[0], loc=params[1], scale=params[2])

    return p_nFR2


#%% nFR3_half_consol

srange_of_assembly_types ={
    CONSOL: (31741.781,43171.249),
    UNCONSOL: (11114.568,16755.15),
    HALFCONSOL: (19932.25, 48762.273)
}



def nFR3 (nfr_range, assembly_type):
    x = nfx3for[nfr_range]
    min, max  = srange_of_assembly_types[assembly_type]
    p_nFR3 = uniform.cdf(x=x, loc=min, scale=(max - min)) \
             - uniform.cdf(x=min, loc=min, scale=(max - min))
    return p_nFR3


def uniform_distrb(nfr3_range,hook_type):
    min_srange,max_srange= srange_of_assembly_types[hook_type]
    drange=nfx3for[nfr3_range]
    min_drange = min_srange
    fig =plot_unifor(min_srange, max_srange, min_drange, drange)
    fig.savefig(UNIFORM_GRAPH_FILENAME)



def gamma_distrb(nfr1_range, assembly_type):
    data = get_duration_data(assembly_type)
    gamma_drange=nfx1for[nfr1_range]
    fig =plot_gamma(gamma_drange, data)
    fig.savefig(GAMMA_GRAPH_FILENAME)


def lognorm_distrb(nfr2_range,assembly_type):
    data = get_disp_data(assembly_type)
    lognorm_drange=nfx2for[nfr2_range]
    fig =plot_lognorm(lognorm_drange,data)
    fig.savefig(LOG_GRAPH_FILENAME)

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
