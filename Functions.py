import pandas as pd
from scipy.stats import uniform
#%% Loading the file:
data = pd.read_csv(r'C:\Users\kazak\PycharmProjects\Assembly_data_processing\Data\HookC1.csv')
#%% Shifting data.Time and append Duration series
data['Duration']=data.Time-data.Time.shift(1)

#%% DR1opping rows with Start
data=data[data.Components!="Start"]

#%% First guys trials are shifted
data=data[data.Username==data.shift(1).Username]
data.Duration = (data.Duration / np.timedelta64(1,'s')).astype(float)

#%% To remove outliers
data=data[data.Duration>0]
data=data[data.Duration<500]#it is only for hook_con to remove <0 duration >500



#%% Fitting data to Gamma distribution
fit_alpha, fit_loc, fit_beta=stats.gamma.fit(data.Duration)

#%% Finding prob. density
if button_1='less':
    if file=load_file():
        DR1=20
        p_nFR1=stats.gamma.cdf(x=DR1,a=fit_alpha, loc=fit_loc, scale=fit_beta)
if button_1='moderate':
    if file=load_file():
        DR1 = 55.561
        p_nFR1 = stats.gamma.cdf(x=DR1, a=fit_alpha, loc=fit_loc, scale=fit_beta)
if button_1='more':
    if file=load_file():
        DR1 = 75
        p_nFR1 = stats.gamma.cdf(x=DR1, a=fit_alpha, loc=fit_loc, scale=fit_beta)


#%% Finding L1 value
data["L1"]=data.r1+data.r2+data.r3##+data.r5+data.r6+data.r7+data.r8+data.r9+data.r10
data["L1"]=data["L1"]*1000


#%% Finding common range of nFR3
if
# There are separated parts
#%% nFR3_unconsol
if file=unconsol:
    if button_3='less':
        DR2 = 20000
        p_nFR3 = uniform.cdf(x=16755.15 , loc=11114.568, scale=(16755.15 - 11114.568)) - uniform.cdf(x=11114.568,
                                                                                                loc=11114.568, scale=(
                        16755.15  - 11114.568))
        # print(cdf_half_consol_10_20)

    if button_3='moderate':
        DR2 = 30000
        p_nFR3 = uniform.cdf(x=16755.15 , loc=11114.568, scale=(16755.15 - 11114.568)) - uniform.cdf(x=11114.568,
                                                                                                loc=11114.568, scale=(
                        16755.15  - 11114.568))
        # print(cdf_half_consol_10_30)

    if button_3='more':
        DR2 = 40000
        p_nFR3 = uniform.cdf(x=16755.15 , loc=11114.568, scale=(16755.15 - 11114.568)) - uniform.cdf(x=11114.568,
                                                                                                loc=11114.568, scale=(
                        16755.15  - 11114.568))
        # print(cdf_half_consol_10_40)





#%% nFR3_half_consol
if file=half_consol:
    if button_3='less':
        DR2=20000
        p_nFR3=uniform.cdf(x=20000,loc=19932.25, scale=(48762.273-19932.25))-uniform.cdf(x=19932.25,loc=19932.25, scale=(48762.273-19932.25))
        # print(cdf_half_consol_10_20)

    if button_3='moderate':
        DR2=30000
        p_nFR3=uniform.cdf(x=30000,loc=19932.25, scale=(48762.273-19932.25))-uniform.cdf(x=19932.25,loc=19932.25, scale=(48762.273-19932.25))
        # print(cdf_half_consol_10_30)

    if button_3='more':
        DR2=40000
        p_nFR3=uniform.cdf(x=40000,loc=19932.25, scale=(48762.273-19932.25))-uniform.cdf(x=19932.25,loc=19932.25, scale=(48762.273-19932.25))
        # print(cdf_half_consol_10_40)

#%% nFR3_consol
if file=half_consol:
    if button_3='less':
        DR2=20000
        p_nFR3=uniform.cdf(x=DR2,loc=31741.781, scale=(43171.249-31741.781))-uniform.cdf(x=31741.781,loc=31741.781, scale=(43171.249-31741.781))
        # print(cdf_half_consol_10_20)

    if button_3='moderate':
        DR2=30000
        p_nFR3=uniform.cdf(x=DR2,loc=31741.781, scale=(43171.249-31741.781))-uniform.cdf(x=31741.781,loc=31741.781, scale=(43171.249-31741.781))
        # print(cdf_half_consol_10_30)

    if button_3='more':
        DR2=40000
        p_nFR3=uniform.cdf(x=DR2,loc=31741.781, scale=(43171.249-31741.781))-uniform.cdf(x=31741.781,loc=31741.781, scale=(43171.249-31741.781))
        # print(cdf_half_consol_10_40)




#%% Finding information content
