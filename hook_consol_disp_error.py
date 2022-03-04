import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

#%% Loading data
data = pd.read_csv(r'C:\Users\kazak\PycharmProjects\pythonProject\Data\HookC1.csv')


data=data[data.Components!="Start"]
data=data[data.Edges==5]



data["L1"]=data.r1+data.r2+data.r3+data.r4+data.r5
data["L1"]=data["L1"]*1000
print(data["L1"])

data["L2"]=data.r1**2+data.r2**2+data.r3**2+data.r4**2+data.r5**2
data["L2"]=data.L2**0.5
data["L2"]=data["L2"]*1000


print(data)


#%% Plotting L1
data.L1.plot()
plt.show()
ax = data.L1.plot.hist(bins=12, alpha=0.5)

plt.title("L1")
plt.xlabel("Hook_consol_disp_error(mm)")
plt.show()

#%% Plotting L2
print(data)
plt.plot(data.L2)
plt.show()
ax = data.L2.plot.hist(bins=12, alpha=0.5)
plt.title("L2")
plt.xlabel("Hook_consol_disp_error(mm)")
plt.show()

#%% Plotting r1
data.r1=data.r1*1000
data.r1.plot()
plt.show()
ax = data.r1.plot.hist(bins=12, alpha=0.5)
plt.title("HookCon r1")
plt.xlabel("Hook_consol_disp_error(mm)")
plt.show()

#%% Plotting r2
data.r2=data.r2*1000
data.r2.plot()
plt.show()
ax = data.r2.plot.hist(bins=12, alpha=0.5)
plt.title("HookCon r2")
plt.xlabel("Hook_consol_disp_error(mm)")
plt.show()



# #%% Erlang distribution
#
# x=data.r1
# y=stats.gamma.pdf(x, a=5, scale=3)
# plt.plot(x,y)
#
# plt.show()