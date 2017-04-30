# Evaluate the S-curves
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def S(s,r,b):
	return 1-(1-s**r)**b

ds = np.linspace(0.1,0.9,9)

plt.plot(ds, S(ds,3,10))
plt.plot(ds, S(ds,6,20))
plt.plot(ds, S(ds,5,50))
plt.title('S-curves')
plt.xlabel('s')
plt.legend(['r=3 and b=10','r=6 and b=20','r=5 and b=50'], loc='best')
plt.show()
