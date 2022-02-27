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
# data=data.drop([11,19,39])

data.Duration = (data.Duration / np.timedelta64(1,'s')).astype(float)
print(data.Duration)
ax = data.Duration.plot.hist(bins=12, alpha=0.5)
plt.title("Assembly time trials")
plt.xlabel("Time(s)")
plt.show()

data.Duration.plot()
plt.show()


#%%
data["L1"]=data.r1+data.r2+data.r3+data.r4+data.r5+data.r6+data.r7+data.r8+data.r9+data.r10
data["L1"]=data["L1"]*1000

data["L2"]=data.r1**2+data.r2**2+data.r3**2+data.r4**2 +data.r5**2+data.r6**2+data.r7+data.r8+data.r9+data.r10
data["L2"]=data.L2**0.5
data["L2"]=data["L2"]*1000



r1=data.r1
r2=data.r2
r3=data.r3
r4=data.r4
r5=data.r5
r6=data.r6
r6=data.r6
r7=data.r7
r8=data.r8
r9=data.r9
r10=data.r10

l2 = data.L2
l1 = data.L1
dur = data.Duration
print('r1= ',r1.corr(dur))
print('r2= ',r2.corr(dur))
print('r3= ',r3.corr(dur))
print('r4= ',r4.corr(dur))
print('r5= ',r5.corr(dur))
print('r6= ',r6.corr(dur))
print('r7= ',r7.corr(dur))
print('r8= ',r8.corr(dur))
print('r9= ',r9.corr(dur))
print('r10= ',r10.corr(dur))


print('l1= ',l1.corr(dur))
print('l2= ',l2.corr(dur))


#%% Transformation


dat, lmbda = stats.boxcox(data.Duration)
print('Best lambda parameter = %s' % round(lmbda, 3))

fig, ax1 = plt.subplots(figsize=(8, 4))
prob = stats.boxcox_normplot(dat, -20, 20, plot=ax1)
ax.axvline(lmbda, color='r')
#%% Inspecting the Gaussian fitting
dat.sort()
mean, std = stats.norm.fit(dat, loc=0)
pdf_norm = stats.norm.pdf(dat, mean, std)

fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(dat, bins='auto', density=True)
ax.plot(dat, pdf_norm, label='Fitted normal distribution')
ax.set_xlabel('Assembly time (s)')
ax.set_ylabel('Transformed Probability')
ax.set_title('Box-Cox Transformed Distribution of Assembly time duration')
ax.legend()
plt.show()

data.Duration.value_counts()


