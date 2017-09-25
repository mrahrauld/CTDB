from scipy.interpolate import interp1d
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt('points.txt',usecols=(0, 1),unpack=True)
f = interp1d(x, y, kind='cubic')
root = fsolve(f,-1)
print('founded roots: ',root)
print('f(roots): ', f(root))



xnew = np.linspace(-20, 19, num=100000, endpoint=True)
plt.plot(x, y, 'o', xnew, f(xnew), '-',root, f(root),'x')
plt.axis([-3, 3, -20, 20])
plt.legend(['data','cubic','root'], loc='best')
plt.axhline(y=0, color='k')
plt.show()