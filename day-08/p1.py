import sys
import os

grid = []
# with open("test.txt", "r") as f:
with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    grid.append(line.strip())

cols = len(grid[0])
rows = len(grid)

num_vis = 0
vis_set = set()
# above
for col in range(cols):
    highest = -1
    for row in range(rows):
        tree = int(grid[row][col])
        if tree > highest:
            vis_set.add((row,col))
            highest = tree

# bottom
for col in range(cols):
    highest = -1
    for row in range(rows - 1 , 0, -1):
        tree = int(grid[row][col])
        if tree > highest:
            vis_set.add((row,col))
            highest = tree

# left
for row in range(rows):
    highest = -1
    for col in range(cols):
        tree = int(grid[row][col])
        if tree > highest:
            vis_set.add((row,col))
            highest = tree

# right
for row in range(rows):
    highest = -1
    for col in range(cols - 1, 0, -1):
        tree = int(grid[row][col])
        if tree > highest:
            vis_set.add((row,col))
            highest = tree

print(len(vis_set))