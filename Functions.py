import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import uniform

#%% Main function
def Infor_con(hook_type, button_1,button_2,button_3):
    if hook_type=='unconsol':
        data=pd.read_csv(r'C:\Users\kazak\PycharmProjects\Assembly_data_processing\Data\HookUnconsol.csv')
        if button_1 is True:
            data['Duration'] = data.Time - data.Time.shift(1)
            data = data[data.Components != "Start"]
            data = data[data.Username == data.shift(1).Username]

            data.Duration = (data.Duration / np.timedelta64(1, 's')).astype(float)

            data = data[data.Duration > 0]
            data = data[data.Duration < 500]
            button_1f(button1)

        if button_2 is True:
            data = data[data.Components != "Start"]
            data = data[data.Edges == 5]
            data["L1"] = data.r1 + data.r2 + data.r3
            data["L1"] = data["L1"] * 1000
            button_2f(button_2)

        if button_3 is True:
            button_3_unconsol(button_3)

    elif hook_type=='half_consol':
        data=pd.read_csv(r'C:\Users\kazak\PycharmProjects\Assembly_data_processing\Data\HookC1.csv')
        if button_1 is True:
            data['Duration'] = data.Time - data.Time.shift(1)
            data = data[data.Components != "Start"]
            data = data[data.Username == data.shift(1).Username]
            data.Duration = (data.Duration / np.timedelta64(1, 's')).astype(float)
            data = data[data.Duration > 0]
            data = data[data.Duration < 500]
            button_1f(button1)
        if button_2 is True:
            data = data[data.Components != "Start"]
            data = data[data.Edges == 8]
            data["L1"] = data.r1 + data.r2 + data.r3 + data.r4 + data.r5 + data.r6
            data["L1"] = data["L1"] * 1000
            button_2f(button_2)
        if button_3 is True:
            button_3_half_consol(button_3)

    else
        if button_1 is True:
            p_nFR1=1.0
        elif button_2 is True:
            p_nFR2=1.0
        else
            button_3_consol(button_3)



    I=-log(nFR1*nFR2*nFR3,2)
    return I


#%% Loading the file:
if
data = pd.read_csv(r'C:\Users\kazak\PycharmProjects\Assembly_data_processing\Data\HookC1.csv')
#%% Shifting data.Time and append Duration series
data['Duration']=data.Time-data.Time.shift(1)

#%% Dropping rows with Start
data=data[data.Components!="Start"]

#%% First guys trials are shifted
data=data[data.Username==data.shift(1).Username]
data.Duration = (data.Duration / np.timedelta64(1,'s')).astype(float)

#%% To remove outliers
data=data[data.Duration>0]
data=data[data.Duration<500]#it is only for hook_con to remove <0 duration >500



#%% Fitting data to Gamma distribution

fit_alpha, fit_loc, fit_beta=stats.gamma.fit(data.Duration)

#%% Finding common range of nFR1
def button_1f(button_1):
    if button_1=='less':
        fit_alpha, fit_loc, fit_beta = stats.gamma.fit(data.Duration)
        DR1=20
        p_nFR1=stats.gamma.cdf(x=DR1,a=fit_alpha, loc=fit_loc, scale=fit_beta)

    if button_1=='moderate':
        fit_alpha, fit_loc, fit_beta = stats.gamma.fit(data.Duration)
        DR1 = 55.561
        p_nFR1 = stats.gamma.cdf(x=DR1, a=fit_alpha, loc=fit_loc, scale=fit_beta)

    if button_1=='more':
        fit_alpha, fit_loc, fit_beta = stats.gamma.fit(data.Duration)
        DR1 = 75
        p_nFR1 = stats.gamma.cdf(x=DR1, a=fit_alpha, loc=fit_loc, scale=fit_beta)
    return p_nFR1

#%% Finding common range of nFR2

def button_2f(button_2):
    if button_2=='less':
        params = stats.lognorm.fit(data.L1)
        DR2=2
        p_nFR2=stats.lognorm.cdf(x=DR1,s=params[0], loc=params[1], scale=params[2])
    if button_2=='moderate':
        params = stats.lognorm.fit(data.L1)
        DR2 = 13.33
        p_nFR2 = stats.lognorm.cdf(x=DR1, s=params[0], loc=params[1], scale=params[2])
    if button_2='more':
        params = stats.lognorm.fit(data.L1)
        DR2 = 30
        p_nFR2 = stats.lognorm.cdf(x=DR1, s=params[0], loc=params[1], scale=params[2])
    return p_nFR2


#Finding common range of nFR3

# There are separated parts
#%% nFR3_unconsol
def button_3_unconsol(button_3):
    if button_3='less':
        DR3 = 20000
        p_nFR3 = uniform.cdf(x=16755.15 , loc=11114.568, scale=(16755.15 - 11114.568)) - uniform.cdf(x=11114.568,
                                                                                                loc=11114.568, scale=(
                        16755.15  - 11114.568))


    if button_3='moderate':
        DR3 = 30000
        p_nFR3 = uniform.cdf(x=16755.15 , loc=11114.568, scale=(16755.15 - 11114.568)) - uniform.cdf(x=11114.568,
                                                                                                loc=11114.568, scale=(
                        16755.15  - 11114.568))


    if button_3='more':
        DR3 = 40000
        p_nFR3 = uniform.cdf(x=16755.15 , loc=11114.568, scale=(16755.15 - 11114.568)) - uniform.cdf(x=11114.568,
                                                                                                loc=11114.568, scale=(
                        16755.15  - 11114.568))
    return p_nFR3





#%% nFR3_half_consol
def button_3_half_consol(button_3):
    if button_3='less':
        DR3=20000
        p_nFR3=uniform.cdf(x=20000,loc=19932.25, scale=(48762.273-19932.25))-uniform.cdf(x=19932.25,loc=19932.25, scale=(48762.273-19932.25))
        # print(cdf_half_consol_10_20)

    elif button_3='moderate':
        DR3=30000
        p_nFR3=uniform.cdf(x=30000,loc=19932.25, scale=(48762.273-19932.25))-uniform.cdf(x=19932.25,loc=19932.25, scale=(48762.273-19932.25))
        # print(cdf_half_consol_10_30)

    elif button_3='more':
        DR3=40000
        p_nFR3=uniform.cdf(x=40000,loc=19932.25, scale=(48762.273-19932.25))-uniform.cdf(x=19932.25,loc=19932.25, scale=(48762.273-19932.25))
    return p_nFR3


def button_3_consol(button_3):
    if button_3='less':
        DR3=20000
        p_nFR3=uniform.cdf(x=DR3,loc=31741.781, scale=(43171.249-31741.781))-uniform.cdf(x=31741.781,loc=31741.781, scale=(43171.249-31741.781))
        # print(cdf_half_consol_10_20)

    elif button_3='moderate':
        DR3=30000
        p_nFR3=uniform.cdf(x=DR3,loc=31741.781, scale=(43171.249-31741.781))-uniform.cdf(x=31741.781,loc=31741.781, scale=(43171.249-31741.781))
        # print(cdf_half_consol_10_30)

    elif button_3='more':
        DR3=40000
        p_nFR3=uniform.cdf(x=DR3,loc=31741.781, scale=(43171.249-31741.781))-uniform.cdf(x=31741.781,loc=31741.781, scale=(43171.249-31741.781))
        # print(cdf_half_consol_10_40)
    return p_nFR3




#%% Finding information content
