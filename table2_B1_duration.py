import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

#%% Loding data
data = pd.read_csv(r'C:\Users\kazak\PycharmProjects\Assembly_data_processing\Data\Table2.csv')
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





#%%Plotting common range
fig, ax = plt.subplots()
lessthanX=norm.cdf(x=95.933, loc=99.63, scale=38.82)
print(lessthanX)
px=np.arange(0,95.9325,0.1)
ax.set_ylim(0,0.012)
ax.fill_between(px,norm.pdf(px,loc=99.63, scale=38.82),alpha=0.5, color='b')
ax.text(-0.5,0.011, "p= ", fontsize=18)
ax.text(15,0.011, round(lessthanX,3), fontsize=15)
ax.text(85,0.001, 95.933, fontsize=10)






#%% Norm fitting
mu, std = norm.fit(data.Duration)

# Plot the histogram.
plt.hist(data.Duration, bins=12, density=True, alpha=0.5, color='b')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(0, 200, 100)
p = norm.pdf(x, mu, std)

plt.plot(x, p, 'k', linewidth=2)
title = "B1 [\u03BC: {:.3f} and \u03C3: {:.3f}]".format(mu, std)
plt.xlabel("Assembly time (s)", fontsize=15)
plt.ylabel("Probability Density", fontsize=15)


plt.title(title)

plt.show()

#%% Fitting data to Gamma distribution
fit_alpha, fit_loc, fit_beta=stats.gamma.fit(data.Duration)
print(fit_alpha, fit_loc, fit_beta)

#%% Plot
x=np.linspace(0,200,100)
y=gamma.pdf(x,fit_alpha,fit_loc,fit_beta)

plt.plot(x,y)