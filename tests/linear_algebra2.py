def data():
	r = range(-10,10)
	for a in r:
		for b in r:
			for c in r:
				if -a + (2*b) + -c == 0:
					yield (a,b,c)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation

x = np.random.normal(size=(80,3))
df = pd.DataFrame(x, columns=["x","y","z"])


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')


x = []
y = []
z = []

for i in data():
		x.append(i[0])
		y.append(i[1])
		z.append(i[2])

sc = ax.scatter(x,y,z, c='darkblue', alpha=0.5)

def update(i):
	sc._offsets3d = (df.x.values[:i], df.y.values[:i], df.z.values[:i])

lim = 10

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-lim,lim)
ax.set_ylim(-lim,lim)
ax.set_zlim(-lim,lim)

#ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(df), interval=70)

plt.tight_layout()
plt.show()


