import numpy as np
import pandas as pd


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


consolidated_data = loadData("./Data/HookUnconsol.csv")
