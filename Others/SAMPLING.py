import matplotlib.pyplot as plt
import numpy as np

#%%
# b=12
p1 =np.random.normal(0,1,size=(1000,1))
p2 =np.random.normal(6,5,size=(1000,1))

mean= np.mean(p1)
var = np.var(p1)
# p3=np.vstack([p1,p2])
p3 = (p1**2+p2**2)**0.5
# plt.hist(p2,bins=b)
# plt.hist(p1,bins=b)
plt.hist(p3,bins=b)
plt.show()