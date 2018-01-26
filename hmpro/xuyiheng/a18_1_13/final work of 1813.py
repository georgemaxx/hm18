import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

x1=np.arange(0,2,1)
x2=np.arange(0,2,1)
A=np.array([7,1])
X, Y = np.meshgrid(x1, x2)
R=X*A[0]+Y*A[1]
Z=1/(1+np.exp(-1*R))
ZXOR=np.logical_xor(X,Y)

ZERR=ZXOR-Z

#ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = plt.get_cmap('rainbow'))
#ax.plot_surface(X, Y, ZXOR, rstride = 1, cstride = 1, cmap = plt.get_cmap('rainbow'))
ax.plot_surface(X, Y, ZERR, rstride = 1, cstride = 1, cmap = plt.get_cmap('rainbow'))
ax.contour(X,Y,Z,offset=-0.5,cmap='rainbow') #从三维曲面到底部的投影

ax.set_zlim(-1,1)
plt.show()
