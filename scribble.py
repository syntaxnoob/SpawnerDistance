#!/bin/python3
import math

### Variabel ###
# spawner coordinates (Xcoordinate, Ycoordinate, Zcoordinate)
Spawners = [(370, 28, 886), (365, 37, 945), (359, 39, 917), (381, 42, 917),
            (351, 44, 931), (362, 44, 891), (408, 44, 927), (429, 35, 897)]
Bigsum = 0
Distancelist = []  # List with Blockindex and Distances
Blocklist = []  # List with Blockindex and X/Y/Z coordinates
Sumlist = []  # List with Distances
Blockindex = -3  # Blockindex is the index for the searched block

Xcoords = []
Ycoords = []
Zcoords = []

bestlist = []

### Find Search area ###

for d in Spawners:
    Xcoords.append(d[0])
    Ycoords.append(d[1])
    Zcoords.append(d[2])

Xcoords.sort()
Ycoords.sort()
Zcoords.sort()

minX = Xcoords[0]
minY = Ycoords[0]
minZ = Zcoords[0]
maxX = Xcoords[-1]
maxY = Ycoords[-1]
maxZ = Zcoords[-1]
# Could be optimized

### Brute force the shortest distance ###

for i in range(minX, maxX):  # Xcoords Loop
    Blockindex = Blockindex + 1

    for j in range(minY, maxY):  # Ycoords Loop
        Blockindex = Blockindex + 1

        for k in range(minZ, maxZ):  # Zcoords Loop
            Blockindex = Blockindex + 1
            for l in range(0, 7):

                # Pythagorean.
                distance = math.sqrt(
                    math.pow((Spawners[l][0] - i), 2) + math.pow((Spawners[l][1] - j), 2) + math.pow((Spawners[l][2] - k), 2))

                if (distance > 16):
                    # Later used to calculate the amount of spawners that will be activated.
                    Bigsum = 100000 + Bigsum
                else:  # Distance is allways positive
                    Bigsum = distance + Bigsum

            Distancelist.append(Blockindex)
            Distancelist.append(Bigsum)
            Sumlist.append(Bigsum)
            Blocklist.append(Blockindex)
            Blocklist.append(i)
            Blocklist.append(j)
            Blocklist.append(k)
            Bigsum = 0

Sumlist.sort()
ID = (Distancelist.index(Sumlist[0]))
DI = Blocklist.index(ID)
print ("The closest block to all spawners is:", Blocklist[DI + 1], ",",
       Blocklist[DI + 2], ",", Blocklist[DI + 3], ".", "And you activate:", round((700000 - Distancelist[ID]) / 100000), "Spawners.")
for i in range(len(Distancelist)):
    if (Distancelist[i] > 100000):
        if (Distancelist[i] < 500000):
            bestlist.append(Distancelist[(i - 1)])
        else:continue
    else:continue
print("blocks dat 3 spawners activeren: ",bestlist)
