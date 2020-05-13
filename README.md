# SpawnerDistance
Script that calculates the optimal distance between a player and a certain amount of mobspawners for the game Minecraft.
### Method ###
The method that I used is a brute force method.
The script starts with creating a search area with potential blocks.(min/max of X/Y/Z)(could be optimized)

In the second stage it will loop around all the potential blocks and save the sum of distances from the spawners to that block IF the distance<16(A player can only activate a spawner when he/she is 16 blocks away from af spawner).

All distances will be appended into a list, sorted.
(TODO finish the method)
### Requirements ###
1. python
2. spawner coordinates
