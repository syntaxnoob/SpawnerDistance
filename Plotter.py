#!/bin/python3

### Import ###
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sb
import numpy as np


### Vars ###

# blokjes = pd.read_csv("3spawner.csv",index_col=False, )
blokjes = np.genfromtxt('3spawner.csv', delimiter=',')
blokjes = np.delete(blokjes, 0, axis=0)

xblok = []
yblok = []
zblok = []

for d in blokjes:
    xblok.append(d[0])
    yblok.append(d[1])
    zblok.append(d[2])

Spawners = [(370, 28, 886), (365, 37, 945), (359, 39, 917), (381, 42, 917),
            (351, 44, 931), (362, 44, 891), (408, 44, 927), (429, 35, 897)]

# Split axis

Xcoords = []
Ycoords = []
Zcoords = []

for d in Spawners:
    Xcoords.append(d[0])
    Ycoords.append(d[1])
    Zcoords.append(d[2])

# Plotting

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.gca().invert_yaxis()

ax.scatter(Xcoords, Zcoords, Ycoords, c='b', marker='o')
ax.scatter(xblok, zblok, yblok, c='g', marker='o', alpha=0.2)
plt.title('Usefull Blocks Plot')
plt.show()
