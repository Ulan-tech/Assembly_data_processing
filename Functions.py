import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import uniform
import math


#%% Main function
def infor_con(hook_type, button_1,button_2,button_3):
    p_nFR1, p_nFR2, p_nFR3 = 0, 0, 0

    if hook_type == 'unconsol':
        data = pd.read_csv(r'C:\Users\kazak\PycharmProjects\Assembly_data_processing\Data\HookUnconsol.csv')
        data = data[data.Components != "Start"]
        data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S %p')

        if button_1 in ('less', 'moderate', 'more'):
            data['Duration'] = data.Time - data.Time.shift(1)
            data = data[data.Username == data.shift(1).Username]

            data.Duration = (data.Duration / np.timedelta64(1, 's')).astype(float)

            data = data[data.Duration > 0]
            data = data[data.Duration < 500]
            p_nFR1 = button_1f(button_1, data)

        elif button_2 in ('less', 'moderate', 'more'):
            data = data[data.Edges == 8]
            data["L1"] = data.r1 + data.r2 + data.r3+data.r4+data.r5+data.r6
            data["L1"] = data["L1"] * 1000
            button_2f(button_2, data)

        elif button_3 in ('less', 'moderate', 'more'):
            p_nFR3 = 1

    elif hook_type == 'half_consol':
        data = pd.read_csv(r'C:\Users\kazak\PycharmProjects\Assembly_data_processing\Data\HookC1.csv')
        data = data[data.Components != "Start"]
        data['Time'] = pd.to_datetime(data['Time'], format='%H:%M:%S %p')

        if button_1 in ('less', 'moderate', 'more'):
            data['Duration'] = data.Time - data.Time.shift(1)
            data = data[data.Username == data.shift(1).Username]
            data.Duration = (data.Duration / np.timedelta64(1, 's')).astype(float)
            data = data[data.Duration > 0]
            data = data[data.Duration < 500]
            p_nFR1 = button_1f(button_1, data)

        if button_2  in ('less', 'moderate', 'more'):
            data = data[data.Edges == 5]
            data["L1"] = data.r1 + data.r2 + data.r3
            data["L1"] = data["L1"] * 1000
            p_nFR2 = button_2f(button_2, data)

        if button_3:
            p_nFR3 = button_3_half_consol(button_3)

    elif hook_type == 'consol':
        p_nFR1, p_nFR2 = 1.0,  1.0
        p_nFR3 = button_3_consol(button_3)

    return p_nFR1, p_nFR2, p_nFR3 #, -math.log(p_nFR1 * p_nFR2 * p_nFR3, 2)


#%% Finding common range of nFR1
def button_1f(button_1, data):
    if button_1 == 'less': x = 20
    elif button_1 == 'moderate': x = 55.561
    elif button_1 == 'more': x = 75

    fit_alpha, fit_loc, fit_beta = stats.gamma.fit(data.Duration)
    p_nFR1 = stats.gamma.cdf(x=x, a=fit_alpha, loc=fit_loc, scale=fit_beta)

    return p_nFR1


#%% Finding common range of nFR2
def button_2f(button_2, data):
    if button_2 == 'less': x = 2
    elif button_2 == 'moderate': x = 13.33
    elif button_2 == 'more': x = 15

    params = stats.lognorm.fit(data.L1)
    p_nFR2 = stats.lognorm.cdf(x=x, s=params[0], loc=params[1], scale=params[2])

    return p_nFR2


#%% nFR3_half_consol
def button_3_half_consol(button_3):
    if button_3 == 'less': x = 20000
    elif button_3 == 'moderate': x = 30000
    elif button_3 == 'more': x = 40000

    p_nFR3 = uniform.cdf(x=x, loc=19932.25, scale=(48762.273-19932.25))\
                 - uniform.cdf(x=19932.25, loc=19932.25, scale=(48762.273-19932.25))

    return p_nFR3


def button_3_consol(button_3):
    if button_3 == 'less': x = 20000
    elif button_3 == 'moderate': x = 30000
    elif button_3 == 'more': x = 40000

    p_nFR3 = uniform.cdf(x=x, loc=31741.781, scale=(43171.249-31741.781))\
                 - uniform.cdf(x=31741.781,loc=31741.781, scale=(43171.249-31741.781))

    return p_nFR3


results_df = pd.DataFrame()

for cons in ['unconsol', 'half_consol', 'consol']:
    for btn1 in ['less', 'moderate', 'less']:
        for btn2 in ['less', 'moderate', 'less']:
            for btn3 in ['less', 'moderate', 'less']:
                p_nFR1, p_nFR2, p_nFR3 = infor_con(cons, btn1, btn2, btn3)
                results_df = results_df.append([[cons, btn1, btn2, btn3, p_nFR1, p_nFR2, p_nFR3]], ignore_index=False)

print(results_df.shape)
results_df.to_excel('results.xlsx')
