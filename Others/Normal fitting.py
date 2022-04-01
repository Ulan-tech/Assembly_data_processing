import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#%% Loding data
data = pd.read_csv(r'C:\Users\kazak\PycharmProjects\pythonProject\Data\Table11.csv')
print(data.Time)
#%% converting to time
data['Time'] =  pd.to_datetime(data['Time'], format='%H:%M:%S %p')

#%% Duration
data['Duration']=data.Time-data.Time.shift(1)
print(data['Duration'])



#%% Filter start
print(data.Components)
data=data[data.Components!="Start"]
print(data.Duration)
#%% First in trial , first rep

data=data[data.Username==data.shift(1).Username]
# print(data.Username==data.shift(1).Username)
print(data)

data.Duration = (data.Duration / np.timedelta64(1,'s')).astype(float)
print(data.Duration)
ax = data.Duration.plot.hist(bins=12, alpha=0.5)
plt.title("Assembly time trials")
plt.xlabel("Time(s)")
plt.show()

data.Duration.plot()
plt.show()

#%%Normal fitting
mean, std = stats.norm.fit(data.Duration, loc=0)
pdf_norm = stats.norm.pdf(data.Duration, mean, std)

fig, ax1 = plt.subplots(figsize=(8, 4))
ax.hist(data, bins='auto', density=True)

ax1.plot(data.Duration, pdf_norm, label='normal')
ax1.set_xlabel('X values')
ax1.set_ylabel('probability')
ax1.legend()
plt.show()