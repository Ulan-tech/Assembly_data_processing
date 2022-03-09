import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.stats import gamma

#%% Loading data
data = pd.read_csv(r'C:\Users\kazak\PycharmProjects\Assembly_data_processing\Data\HookC1.csv')
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
# mu, std = norm.fit(data.Duration)
#
# # Plot the histogram.
# plt.hist(data.Duration, bins=12, density=True, alpha=0.5, color='b')
#
# # Plot the PDF.
# xmin, xmax = plt.xlim()
# x = np.linspace(0, xmax, 100)
# p = norm.pdf(x, mu, std)
#
# plt.plot(x, p, 'k', linewidth=2)
# title = "Fit Values of Hook_consol: {:.3f} and {:.3f}".format(mu, std)
# plt.title(title)
#
# plt.show()

#%%Plotting common range
fig, ax = plt.subplots()
lessthanX=norm.cdf(x=72.244, loc=55.058, scale=38.652)
print(lessthanX)
px=np.arange(0,72.244,0.1)
ax.set_ylim(0,0.012)
ax.fill_between(px,norm.pdf(px,loc=55.058, scale=38.652),alpha=0.5, color='b')
ax.text(0,0.011, "p= ", fontsize=18)
ax.text(17,0.011, round(lessthanX,3), fontsize=15)
ax.text(65,0.0005, 72.244, fontsize=10)






#%% Norm fitting
mu, std = norm.fit(data.Duration)

# Plot the histogram.
plt.hist(data.Duration, bins=12, density=True, alpha=0.5, color='b')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(0, 200, 100)
p = norm.pdf(x, mu, std)

plt.plot(x, p, 'k', linewidth=2)
title = "Hook_con [\u03BC: {:.3f} and \u03C3: {:.3f}]".format(mu, std)
plt.xlabel("Assembly time (s)", fontsize=15)
plt.ylabel("Probability Density", fontsize=15)


plt.title(title)

plt.show()
#%% Fitting data to Gamma distribution
fit_alpha, fit_loc, fit_beta=stats.gamma.fit(data.Duration)
print(fit_alpha, fit_loc, fit_beta)
#%% Plotting Gamma distribution from above parameters
# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True
#
# x = np.linspace(0, 10, 10)
# y = stats.gamma.pdf(x, a=5, scale=0.333)
#
# plt.plot(x, y, "ro-", label=(r'$\alpha=0, \beta=3$'))
# plt.legend(loc='upper right')
#
# plt.show()
#%% Plot
x=np.linspace(0,200,100)
y=gamma.pdf(x,fit_alpha,fit_loc,fit_beta)

plt.plot(x,y)


