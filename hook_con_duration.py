import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

#%% Loading data
data = pd.read_csv(r'C:\Users\kazak\PycharmProjects\pythonProject\Data\HookC1.csv')
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

data.Duration = (data.Duration / np.timedelta64(1,'s')).astype(float)
print(data.Duration)
data=data[data.Duration>0] #it is only for hook_con to remove <0 duration
#%%plot
ax = data.Duration.plot.hist(bins=12, alpha=0.5)
plt.title("Assembly time trials")
plt.xlabel("Time(s)")
plt.show()

data.Duration.plot()
plt.show()


#%% Norm fitting
mu, std = norm.fit(data.Duration)

# Plot the histogram.
plt.hist(data.Duration, bins=12, density=True, alpha=0.5, color='b')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(0, xmax, 100)
p = norm.pdf(x, mu, std)

plt.plot(x, p, 'k', linewidth=2)
title = "Fit Values of Hook_consol: {:.2f} and {:.2f}".format(mu, std)
plt.title(title)

plt.show()