import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

#%% Loading data
data = pd.read_csv(r'C:\Users\kazak\PycharmProjects\pythonProject\Data\Table2.csv')


data=data[data.Components!="Start"]
data=data[data.Edges==6]



data["L1"]=data.r1+data.r2+data.r3+data.r4+data.r5+data.r6#+data.r7+data.r8
data["L1"]=data["L1"]*1000
print(data["L1"])

data["L2"]=data.r1**2+data.r2**2+data.r3**2+data.r4**2+data.r5**2+data.r6**2#+data.r7**2+data.r8
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
plt.title("B1 r1")
plt.xlabel("Displacement error(m)")
plt.show()

#%% Plotting r2
data.r2.plot()
plt.show()
ax = data.r2.plot.hist(bins=12, alpha=0.5)
plt.title("B1 r2")
plt.xlabel("Displacement error(m)")
plt.show()

#%% Plotting r3
data.r3.plot()
plt.show()
ax = data.r3.plot.hist(bins=12, alpha=0.5)
plt.title("B1 r3")
plt.xlabel("Displacement error(m)")
plt.show()


#%% Norm fitting L1
mu, std = norm.fit(data.L1)

# Plot the histogram.
plt.hist(data.L1, bins=12, density=True, alpha=0.5, color='b')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

plt.plot(x, p, 'k', linewidth=2)
title = "Fit Values of B1 (L1): {:.4f} and {:.4f}".format(mu, std)
plt.title(title)

plt.show()

#%% Norm fitting L2
mu, std = norm.fit(data.L2)

# Plot the histogram.
plt.hist(data.L2, bins=12, density=True, alpha=0.5, color='b')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

plt.plot(x, p, 'k', linewidth=2)
title = "Fit Values of B1 (L2): {:.4f} and {:.4f}".format(mu, std)
plt.title(title)

plt.show()