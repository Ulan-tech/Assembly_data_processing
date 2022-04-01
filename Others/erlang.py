from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd






#%% Loading data


data = pd.read_csv(r'C:\Users\kazak\PycharmProjects\pythonProject\Data\HookUnconsol.csv')


data=data[data.Components!="Start"]
data=data[data.Edges==8]
data["L1"]=data.r1+data.r2+data.r3+data.r4+data.r5+data.r6+data.r7+data.r8
data["L1"]=data["L1"]*1000

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
# #%% Fitting to Erlang/Gamma distribution
# x=np.linspace(130,220,50)
# shape,loc,scale=gamma.fit(data.L1,floc=0)
# print(shape,loc,scale)
# y=gamma.pdf(x,shape, loc,scale)
# plt.title('Fitted gamma of displacement L1')
# plt.plot(x,y)
# plt.show()

#%% Normal fitting
vrb=scipy.stats.distributions.norm.pdf(data.L1)
# mean, var=vrb
# x=np.linspace(150,220,50)
# fitted_data=scipy.stats.distributions.norm.pdf(x,vrb)
# plt.hist(data.L1,density=True)
# plt.plot(x,fitted_data,'r-')
#%% mean and var
data.L1.describe()
