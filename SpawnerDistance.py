import math

### Variabel ###
#spawner coordinates (Xcoordinate, Ycoordinate, Zcoordinate)
Spawners = [(370, 28, 886), (365, 37, 945), (359, 39, 917), (381, 42, 917),
            (351, 44, 931), (362, 44, 891), (408, 44, 927), (429, 35, 897)]
Bigsum = 0
Distancelist = []
Indexlist = []
Ramlist = []
Blockindex = -3

Xcoords = []
Ycoords = []
Zcoords = []

# Find Search area

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

# Brute force the shortest distance

for i in range(minX, maxX):  # Xcoords Loop
    Blockindex = Blockindex + 1

    for j in range(minY, maxY):  # Ycoords Loop
        Blockindex = Blockindex + 1

        for k in range(minZ, maxZ):  # Zcoords Loop
            Blockindex = Blockindex + 1
            for l in range(0, 7):
                #print (i, j, k)
                x = (Spawners[l][0] - i)
                y = (Spawners[l][1] - j)
                z = (Spawners[l][2] - k)

                distance = math.sqrt(
                    math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2))  # pitagoras
                if (distance > 16):
                    Bigsum = 100000 + Bigsum
                else:
                    Bigsum = distance + Bigsum
            Distancelist.append(Blockindex)  # Nummering toevoegen, optioneel.
            Distancelist.append(Bigsum)
            Ramlist.append(Bigsum)
            Bigsum = 0
            Indexlist.append(Blockindex)
            Indexlist.append(i)
            Indexlist.append(j)
            Indexlist.append(k)

Ramlist.sort()
ID = (Distancelist.index(Ramlist[0]))
DI = Indexlist.index(ID)
print ("The closest block to all spawners is: ", Indexlist[DI + 1],
       Indexlist[DI + 2], Indexlist[DI + 3], " and you activate: ", round((700000 - Distancelist[ID]) / 100000), " Spawners.")
