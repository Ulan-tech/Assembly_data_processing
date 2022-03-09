import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

#%% Loading data
data = pd.read_csv(r'C:\Users\USER\pythonProject\Data\HookUnconsol.csv')


data=data[data.Components!="Start"]
data=data[data.Edges==8]



data["L1"]=data.r1+data.r2+data.r3+data.r4+data.r5+data.r6+data.r7+data.r8
data["L1"]=data["L1"]*1000
print(data["L1"])

data["L2"]=data.r1**2+data.r2**2+data.r3**2+data.r4**2+data.r5**2+data.r6**2+data.r7**2+data.r8
data["L2"]=data.L2**0.5
data["L2"]=data["L2"]*1000

#data["L3"]=np.max([data.r1,data.r2,data.r3,data.r4,data.r5,data.r6],0)

print(data)


#%% Plotting L1
data.L1.plot()
plt.show()
ax = data.L1.plot.hist(bins=12, alpha=0.5)

plt.title("L1")
plt.xlabel("Displacement error(mm)")
plt.show()

#%% Plotting L2
print(data)
plt.plot(data.L2)
plt.show()
ax = data.L2.plot.hist(bins=12, alpha=0.5)
plt.title("L2")
plt.xlabel("Displacement error(mm)")
plt.show()

#%% Plotting r1
data.r1.plot()
plt.show()
ax = data.r1.plot.hist(bins=12, alpha=0.5)
plt.title("HookUnCon r1")
plt.xlabel("Displacement error(m)")
plt.show()

#%% Plotting r2
data.r2.plot()
plt.show()
ax = data.r2.plot.hist(bins=12, alpha=0.5)
plt.title("HookUnCon r2")
plt.xlabel("Displacement error(m)")
plt.show()

#%% Counts of disp_errors
sum= sum(data.r1.value_counts())
print(sum)

# #%% Erlang distribution
#
# x=data.r1
# y=stats.gamma.pdf(x, a=5, scale=3)
# plt.plot(x,y)
#
# plt.show()


#%% Norm fitting
mu, std = norm.fit(data.L2)

# Plot the histogram.
plt.hist(data.L1, bins=12, density=True, alpha=0.5, color='b')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

plt.plot(x, p, 'k', linewidth=2)
title = "Fit Values of Hook_Unconsol (L1): {:.3f} and {:.3f}".format(mu, std)
plt.title(title)

plt.show()

#%% Norm fitting
mu, std = norm.fit(data.L2)

# Plot the histogram.
plt.hist(data.L1, bins=12, density=True, alpha=0.5, color='b')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

plt.plot(x, p, 'k', linewidth=2)
title = "Fit Values of Hook_Unconsol (L2): {:.3f} and {:.3f}".format(mu, std)
plt.title(title)

plt.show()