#!/bin/python3

### Import ###
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sb

### Vars ###

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

ax.scatter(Xcoords, Ycoords, Zcoords, c='b', marker='o')
plt.title('Blockscatter')
plt.show()
