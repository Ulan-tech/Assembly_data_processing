import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import stats
import numpy as np

#%% Loading data
data = pd.read_csv(r'C:\Users\kazak\PycharmProjects\Assembly_data_processing\Data\HookC1.csv')


data=data[data.Components!="Start"]
data=data[data.Edges==5]



data["L1"]=data.r1+data.r2+data.r3#+data.r4+data.r5#+data.r6+data.r7+data.r8
data["L1"]=data["L1"]*1000
print(data["L1"])

data["L2"]=data.r1**2+data.r2**2+data.r3**2#+data.r4**2+data.r5**2#+data.r6**2+data.r7**2+data.r8
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
plt.title("HookCon r1")
plt.xlabel("Displacement error(m)")
plt.show()

#%% Plotting r2
data.r2.plot()
plt.show()
ax = data.r2.plot.hist(bins=12, alpha=0.5)
plt.title("HookCon r2")
plt.xlabel("Displacement error(m)")
plt.show()

#%% Plotting r3
data.r3.plot()
plt.show()
ax = data.r3.plot.hist(bins=12, alpha=0.5)
plt.title("HookCon r3")
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
# title = "Fit Values of Hook_consol (L1): {:.4f} and {:.4f}".format(mu, std)
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
# title = "Fit Values of Hook_consol (L2): {:.3f} and {:.3f}".format(mu, std)
# plt.title(title)
#
# plt.show()

#%%Plotting common range_L1
fig, ax = plt.subplots()
lessthanX=norm.cdf(x=18.306, loc=12.702, scale=6.941)
print(lessthanX)
px=np.arange(0,18.306,0.1)
ax.set_ylim(0,0.06)
ax.fill_between(px,norm.pdf(px,loc=12.702, scale=6.941),alpha=0.5, color='b')
ax.text(0.055,0.055, "p= ", fontsize=18)
ax.text(4,0.055, round(lessthanX,3), fontsize=15)
ax.text(16,0.005, 18.306, fontsize=10)






#%% Norm fitting_L1
mu, std = norm.fit(data.L1)

# Plot the histogram.
plt.hist(data.L1, bins=12, density=True, alpha=0.5, color='b'#, normed=True)

# Plot the PDF.
# xmin, xmax = plt.xlim()
x = np.linspace(0, 50, 100)
p = norm.pdf(x, mu, std)
#
plt.plot(x, p, 'k', linewidth=2)
title = "Hook_con (L1) [\u03BC: {:.3f} and \u03C3: {:.3f}]".format(mu, std)
plt.xlabel("L1-norm (mm)", fontsize=15)
plt.ylabel("Probability Density", fontsize=15)


plt.title(title)

plt.show()


#%%Plotting common range_L2
fig, ax = plt.subplots()
lessthanX=norm.cdf(x=8.880, loc=7.452, scale=3.964)
print(lessthanX)
px=np.arange(0,8.880,0.1)
ax.set_ylim(0,0.11)
ax.fill_between(px,norm.pdf(px,loc=7.452, scale=3.964),alpha=0.5, color='b')
ax.text(0.055,0.1, "p= ", fontsize=18)
ax.text(2.5,0.1, round(lessthanX,3), fontsize=15)
ax.text(8,0.005,8.880, fontsize=10)






#%% Norm fitting_L2
mu, std = norm.fit(data.L2)

# Plot the histogram.
plt.hist(data.Duration, bins=12, density=True, alpha=0.5, color='b', normed=True)

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(0, 30, 100)
# p = norm.pdf(x, mu, std)
#
# plt.plot(x, p, 'k', linewidth=2)
# title = "Hook_con (L2) [\u03BC: {:.3f} and \u03C3: {:.3f}]".format(mu, std)
# plt.xlabel("L2-norm (mm)", fontsize=15)
# plt.ylabel("Probability Density", fontsize=15)
#
#
# plt.title(title)

# plt.show()
#%% Lognormal fitting
params=stats.lognorm.fit(data.L1)
print(params)

x=np.linspace(0,40,100)
y=stats.lognorm.pdf(x,s=params[0],loc=params[1],scale=params[2])

# plt.plot(x, p, label='Normal Distribution')
plt.plot(x, y, label='Lognorm Distribution')
plt.legend()
plt.plot(x,y)
# plt.show()
mu,sigma=np.log(params[2]),params[0]

#%% Goodness fit of lognormal to data.L1
stats.kstest(data.L1, 'lognorm', stats.lognorm.fit(data.L1))

#%% IT IS THE MAIN CODE TO PLOT-1 "Finding probability density of Gamma distribution"
fig, ax = plt.subplots()
lessthanX=stats.lognorm.cdf(x=13.33,s=params[0], loc=params[1], scale=params[2])
print(lessthanX)
px=np.arange(0,200,250)
ax.set_ylim(0,0.02)
# ax.fill_between(px,stats.gamma.pdf(px,s=params[0], loc=params[1], scale=params[2))
ax.text(-0.5,0.009, "p= ", fontsize=18)
ax.text(15,0.009, round(lessthanX,3), fontsize=15)
# ax.text(85,0.001, 90, fontsize=10)


#%% IT IS THE MAIN CODE TO PLOT-2 "Area under curve"

a,b=0,13.33  #It is the average of the two hooks
x=np.linspace(0,60,100)
lognormal_pdf=stats.lognorm.pdf(x,params[0],params[1],params[2])
fig, ax = plt.subplots()
ax.plot(x,lognormal_pdf,'red', linewidth=2, label='Lognorm Distribution')
ax.set_ylim(bottom=0)
plt.legend()

#Shaded region
ix=np.linspace(a,b)
iy=stats.lognorm.pdf(ix,params[0],params[1],params[2])
verts=[(a,0),*zip(ix,iy),(b,0)]
poly=Polygon(verts,facecolor='peachpuff',edgecolor='0.5')
ax.add_patch(poly)

# ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
#         horizontalalignment='center', fontsize=20)

# fig.text(0.9, 0.05, '$x$')
# fig.text(0.1, 0.9, '$y$')

ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks([a, b], labels=['$0$', '$13.33$'])
# ax.set_yticks([])
plt.xlabel("Displacement error (mm)", fontsize=12)
plt.ylabel("Probability \n Density", rotation='horizontal', fontsize=12)
ax.yaxis.set_label_coords(-0.05,1)

ax.text(3,0.005, "p= ", fontsize=12)
ax.text(6,0.005, round(lessthanX,3), fontsize=12)


plt.show()
print(lessthanX)
#%% Finding the mode of lognormal dist

max_y=max(lognormal_pdf)
max_x=x[lognormal_pdf.argmax()]
print (max_x, max_y)
