import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%% Loding data
data = pd.read_csv(r'C:\Users\kazak\PycharmProjects\pythonProject\Data\Table2.csv')


data=data[data.Components!="Start"]
data=data[data.Edges==5]
data["L1"]=data.r1+data.r2+data.r3#+data.r4#+data.r5+data.r6
data["L1"]=data["L1"]*1000

data["L2"]=data.r1**2+data.r2**2+data.r3#**2+data.r4**2 #+data.r5**2+data.r6**2
data["L2"]=data.L2**0.5
data["L2"]=data["L2"]*1000

#data["L3"]=np.max([data.r1,data.r2,data.r3,data.r4,data.r5,data.r6],0)

print(data)


#%% Plotting L1
data.L1.plot()
plt.show()
ax = data.L1.plot.hist(bins=12, alpha=0.5)

plt.title("L1")
plt.xlabel("mm")
plt.show()

#%% Plotting L2
print(data)
plt.plot(data.L2)
plt.show()
ax = data.L2.plot.hist(bins=12, alpha=0.5)
plt.title("L2")
plt.xlabel("mm")
plt.show()

#%% Plotting r1
data.r1.plot()
plt.show()
ax = data.r1.plot.hist(bins=12, alpha=0.5)
plt.show()

#%% Plotting r2
data.r2.plot()
plt.show()
ax = data.r2.plot.hist(bins=12, alpha=0.5)
plt.show()