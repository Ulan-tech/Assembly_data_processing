import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

#%% Loading data
data = pd.read_csv(r'C:\Users\USER\pythonProject\Data\HookUnconsol.csv')


data=data[data.Components!="Start"]
data=data[data.Edges==8]



data["L1"]=data.r1+data.r2+data.r3+data.r4+data.r5+data.r6#+data.r7+data.r8+data.r9+data.r10
data["L1"]=data["L1"]*1000
print(data["L1"])

data["L2"]=data.r1**2+data.r2**2+data.r3**2+data.r4**2+data.r5**2+data.r6**2#+data.r7**2+data.r8**2+data.r9**2+data.r10**2
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
plt.title("hook_un r1")
plt.xlabel("Displacement error(m)")
plt.show()

#%% Plotting r2
data.r2.plot()
plt.show()
ax = data.r2.plot.hist(bins=12, alpha=0.5)
plt.title("hook_un r2")
plt.xlabel("Displacement error(m)")
plt.show()

#%% Plotting r3
data.r3.plot()
plt.show()
ax = data.r3.plot.hist(bins=12, alpha=0.5)
plt.title("hook_un r3")
plt.xlabel("Displacement error(m)")
plt.show()


#%% Norm fitting L1
# mu, std = norm.fit(data.L1)
#
# # Plot the histogram.
# plt.hist(data.L1, bins=12, density=True, alpha=0.5, color='b')
#
# xmin, xmax = plt.xlim()
# x = np.linspace(xmin, xmax, 100)
# p = norm.pdf(x, mu, std)
#
# plt.plot(x, p, 'k', linewidth=2)
# title = "Fit Values of Hook_un (L1): {:.3f} and {:.3f}".format(mu, std)
# plt.title(title)
#
# plt.show()

#%% Norm fitting L2
# mu, std = norm.fit(data.L2)
#
# # Plot the histogram.
# plt.hist(data.L2, bins=12, density=True, alpha=0.5, color='b')
#
# xmin, xmax = plt.xlim()
# x = np.linspace(xmin, xmax, 100)
# p = norm.pdf(x, mu, std)
#
# plt.plot(x, p, 'k', linewidth=2)
# title = "Fit Values of Hook_un (L2): {:.3f} and {:.3f}".format(mu, std)
# plt.title(title)
#
# plt.show()

#%%Plotting common range_L1
fig, ax = plt.subplots()
lessthanX=norm.cdf(x=18.306, loc=23.910, scale=8.150)
print(lessthanX)
px=np.arange(0,18.306,0.1)
ax.set_ylim(0,0.06)
ax.fill_between(px,norm.pdf(px,loc=23.910, scale=8.150),alpha=0.5, color='b')
ax.text(0.055,0.055, "p= ", fontsize=18)
ax.text(4,0.055, round(lessthanX,3), fontsize=15)
ax.text(16,0.005, 18.306, fontsize=10)






#%% Norm fitting_L1
mu, std = norm.fit(data.L1)

# Plot the histogram.
# plt.hist(data.Duration, bins=12, density=True, alpha=0.5, color='b')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(0, 50, 100)
p = norm.pdf(x, mu, std)

plt.plot(x, p, 'k', linewidth=2)
title = "Hook_uncon (L1) [\u03BC: {:.3f} and \u03C3: {:.3f}]".format(mu, std)
plt.xlabel("L1-norm (mm)", fontsize=15)
plt.ylabel("Probability Density", fontsize=15)


plt.title(title)

plt.show()


#%%Plotting common range_L2
fig, ax = plt.subplots()
lessthanX=norm.cdf(x=8.880, loc=10.309, scale=3.518)
print(lessthanX)
px=np.arange(0,8.880,0.1)
ax.set_ylim(0,0.12)
ax.fill_between(px,norm.pdf(px,loc=10.309, scale=3.518),alpha=0.5, color='b')
ax.text(0.055,0.11, "p= ", fontsize=18)
ax.text(2.5,0.11, round(lessthanX,3), fontsize=15)
ax.text(8,0.005,8.880, fontsize=10)






#%% Norm fitting_L2
mu, std = norm.fit(data.L2)

# Plot the histogram.
# plt.hist(data.Duration, bins=12, density=True, alpha=0.5, color='b')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(0, 30, 100)
p = norm.pdf(x, mu, std)

plt.plot(x, p, 'k', linewidth=2)
title = "Hook_uncon (L2) [\u03BC: {:.3f} and \u03C3: {:.3f}]".format(mu, std)
plt.xlabel("L2-norm (mm)", fontsize=15)
plt.ylabel("Probability Density", fontsize=15)


plt.title(title)

plt.show()
