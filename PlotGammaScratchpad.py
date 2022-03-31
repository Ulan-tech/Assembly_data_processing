#%%
import numpy as np
import pandas as pd

from Plot_Gamma import plot_gamma


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

#%%% init test
consolidated_data = loadData("./Data/HookUnconsol.csv")
halfconsol_data = loadData("./Data/HookC1.csv")

#%% Test 3
plot_gamma(75, consolidated_data)

#%% Test 3
plot_gamma(75, halfconsol_data)
