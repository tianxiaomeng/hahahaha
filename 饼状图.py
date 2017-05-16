from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')


b = []

for i in range(64):
    row = [i]*64
    b += [row]

x = np.array(b)
xpos = x.flatten()
ypos = xpos
zpos = xpos


dx = np.ones_like(zpos)
dy = dx.copy()
dz = 


ax.bar3d(xpos,ypos,zpos,dx,dy,dz,color='b',zort='average')
