# SpawnerDistance
Script that calculates the optimal distance between a player and a certain amount of mobspawners for the game Minecraft.
### Method ###
The method that I used is a brute force method.
The script starts with creating a search area with potential blocks.(min/max of X/Y/Z)(could be optimized)

In the second stage it will loop around all the potential blocks and save the sum of distances from the spawners to that block IF the distance<16(A player can only activate a spawner when he/she is 16 blocks away from af spawner).

All important information will be appended into a list, some lists are sorted(the distance to find shortest Bigsum).

The last step will find the blocks that are linked to a specific distance(Blockindex)

### Requirements ###
1. python (3 preferred)
2. spawner coordinates (X, Y and Z)

### Usage ###

1. Download the script.
2. Edit the (TODO) Coordinate file
3. Open a terminal(Windows, OSX, Linux) and execute the following command: `python3 SpawnerDistance.py`
4. The output will look like this (an example): `The closest block to all spawners is: 364 , 35 , 928 . and you activate: 3  Spawners.`
