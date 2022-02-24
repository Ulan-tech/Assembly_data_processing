import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%% Loding data
data = pd.read_csv(r'C:\Users\kazak\PycharmProjects\pythonProject\Data\HookC1.csv')
print(data.Time)
#%% converting to time
data['Time'] =  pd.to_datetime(data['Time'], format='%H:%M:%S %p')
# data.Time=data.Time + np.timedelta64(1,'h')
#%% Duration
data['Duration']=data.Time-data.Time.shift(1)
print(data['Duration'])



#%% Foilter start
print(data.Components)
data=data[data.Components!="Start"]
print(data.Duration)
#%% First in trial , first rep

data=data[data.Username==data.shift(1).Username]
# print(data.Username==data.shift(1).Username)
print(data)
# data=data.drop([11,19,39])

data.Duration = (data.Duration / np.timedelta64(1,'s')).astype(float)
print(data.Duration)
ax = data.Duration.plot.hist(bins=12, alpha=0.5)
plt.show()
data.Duration.plot()
plt.show()



