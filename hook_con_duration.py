import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy.stats import gamma
from scipy.stats import norm
from matplotlib.patches import Polygon
from scipy.stats import uniform
#%% Loading data
data = pd.read_csv('.\Data\HookC1.csv')
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
data=data[data.Duration>0]
data=data[data.Duration<500]#it is only for hook_con to remove <0 duration >500
#%%plot
ax = data.Duration.plot.hist(bins=12, alpha=0.5)
plt.title("Assembly time trials")
plt.xlabel("Time(s)")
plt.show()

# data.Duration.plot()
plt.show()

#%%
data["L1"]=data.r1+data.r2+data.r3##+data.r5+data.r6+data.r7+data.r8+data.r9+data.r10
data["L1"]=data["L1"]*1000

data["L2"]=data.r1**2+data.r2**2+data.r3**2#+data.r4**2# +data.r5**2+data.r6**2+data.r7+data.r8+data.r9+data.r10
data["L2"]=data.L2**0.5
data["L2"]=data["L2"]*1000



r1=data.r1
r2=data.r2
r3=data.r3

l2 = data.L2
l1 = data.L1
dur = data.Duration
print('r1= ',r1.corr(dur))
print('r2= ',r2.corr(dur))
print('r3= ',r3.corr(dur))

print('l1= ',l1.corr(dur))
print('l2= ',l2.corr(dur))
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

#%% Plotting common range of Gamma distribution
fig, ax = plt.subplots()
lessthanX=stats.gamma.cdf(x=77.23608,a=fit_alpha, loc=fit_loc, scale=fit_beta)
print(lessthanX)
px=np.arange(0,100,250)
ax.set_ylim(0,0.02)
ax.fill_between(px,stats.gamma.pdf(px,a=fit_alpha,loc=fit_loc,scale=fit_beta))
ax.text(-0.5,0.011, "p= ", fontsize=18)
ax.text(15,0.011, round(lessthanX,3), fontsize=15)
ax.text(85,0.001, 90, fontsize=10)

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
x = np.linspace(0, 250, 250)
p = norm.pdf(x, mu, std)

plt.plot(x, p, label='Normal Distribution', linewidth=2)
title = "Hook_con [\u03BC: {:.3f} and \u03C3: {:.3f}]".format(mu, std)
plt.xlabel("Assembly time (s)", fontsize=15)
plt.ylabel("Probability Density", fontsize=15)


plt.title(title)
plt.legend()

# plt.show()

#%% Fitting data to Gamma distribution
fit_alpha, fit_loc, fit_beta=stats.gamma.fit(data.Duration)
print(fit_alpha, fit_loc, fit_beta)
print(stats.gamma.mean(*(fit_alpha, fit_loc, fit_beta)))

#%% Plot
x=np.linspace(0,250,250)
y=gamma.pdf(x,fit_alpha,fit_loc,fit_beta)

# plt.plot(x, p, label='Normal Distribution')
plt.plot(x, y, label='Gamma Distribution', color="Orange")
plt.legend()
plt.plot(x,y)
plt.show()

#%% Goodness test of fit results

stats.kstest(data.Duration, 'gamma', args=(fit_alpha,fit_loc, fit_beta))





#%% Finding probability density of Gamma distribution
fig, ax = plt.subplots()
lessthanX=stats.gamma.cdf(x=55.5605,a=fit_alpha, loc=fit_loc, scale=fit_beta)
print(lessthanX)
px=np.arange(0,100,250)
ax.set_ylim(0,0.02)
ax.fill_between(px,stats.gamma.pdf(px,a=fit_alpha,loc=fit_loc,scale=fit_beta))
ax.text(-0.5,0.011, "p= ", fontsize=18)
ax.text(15,0.011, round(lessthanX,3), fontsize=15)
ax.text(85,0.001, 90, fontsize=10)


#%% IT IS THE MAIN CODE TO PLOT-2 "Area under curve"

a,b=0,55.561  #It is the average of the two hooks
x=np.linspace(0,200,100)
gamma_pdf=stats.gamma.pdf(x,fit_alpha,fit_loc,fit_beta)
fig, ax = plt.subplots()
ax.plot(x,gamma_pdf,'black', linewidth=2, label='Gamma Distribution')
ax.set_ylim(bottom=0)
plt.legend()
#Shaded region
ix=np.linspace(a,b)
iy=stats.gamma.pdf(ix,fit_alpha,fit_loc,fit_beta)
verts=[(a,0),*zip(ix,iy),(b,0)]
poly=Polygon(verts,facecolor='azure',edgecolor='0.5')
ax.add_patch(poly)

# ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
#         horizontalalignment='center', fontsize=20)

# fig.text(0.9, 0.05, '$x$')
# fig.text(0.1, 0.9, '$y$')

ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.xaxis.set_ticks_position('bottom')
# plt.plot(x, gamma_pdf, label='Gamma Distribution', color="Blue")

ax.set_xticks([a, b], labels=['$0$', '$55.561$'])
# ax.set_yticks([])
plt.xlabel("Assembly time (s)", fontsize=12)
plt.ylabel("Probability \n Density", rotation='horizontal', fontsize=12)
ax.yaxis.set_label_coords(-0.05,1)

ax.text(20.5,0.0015, "p= ", fontsize=12)
ax.text(31,0.0015, round(lessthanX,3), fontsize=12)

plt.show()
print(lessthanX)


#%% Finding the mode of gamma dist
max_y=max(gamma_pdf)
max_x=x[gamma_pdf.argmax()]
print (max_x, max_y)

#%% Finding pd of support volume of half-consol
from scipy.stats import uniform
cdf_half_consol_10_20=uniform.cdf(x=20000,loc=19932.25, scale=(48762.273-19932.25))-uniform.cdf(x=19932.25,loc=19932.25, scale=(48762.273-19932.25))
print(cdf_half_consol_10_20)
cdf_half_consol_10_30=uniform.cdf(x=30000,loc=19932.25, scale=(48762.273-19932.25))-uniform.cdf(x=19932.25,loc=19932.25, scale=(48762.273-19932.25))
print(cdf_half_consol_10_30)
cdf_half_consol_10_40=uniform.cdf(x=40000,loc=19932.25, scale=(48762.273-19932.25))-uniform.cdf(x=19932.25,loc=19932.25, scale=(48762.273-19932.25))
print(cdf_half_consol_10_40)





