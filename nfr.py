import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import uniform
import math

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
#%% Main function
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
            p_nFR1 = nFR2(nfr2_range, data)

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
    nf1x = {
        LESS:20,
        MODERATE:55.561,
        MORE: 75
    }
    x = nf1x[nfr_range]

    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(data.Duration)
    p_nFR1 = stats.gamma.cdf(x=x, a=fit_alpha, loc=fit_loc, scale=fit_beta)

    return p_nFR1


#%% Finding common range of nFR2
def nFR2(nfr_range, data):
    nfr2xs={
        LESS : 2,
        MODERATE : 13.33,
        MORE : 15
    }
    x = nfr2xs[nfr_range]

    params = stats.lognorm.fit(data.L1)
    p_nFR2 = stats.lognorm.cdf(x=x, s=params[0], loc=params[1], scale=params[2])

    return p_nFR2


#%% nFR3_half_consol
def nFR3_half_consol(nfr_range):
    xs={
        LESS:20000,
        MODERATE:30000,
        MORE:40000,
    }
    x=xs[nfr_range]

    p_nFR3 = uniform.cdf(x=x, loc=19932.25, scale=(48762.273-19932.25))\
                 - uniform.cdf(x=19932.25, loc=19932.25, scale=(48762.273-19932.25))

    return p_nFR3


def nFR3_consol(nfr_range):
    xs={
        LESS:20000,
        MODERATE:30000,
        MORE:40000,
    }
    x=xs[nfr_range]
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
