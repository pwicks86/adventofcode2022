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

scores = []

for col in range(cols):
    for row in range(rows):
        tree = int(grid[row][col])
        # up
        uscore = 0
        for i in range(row - 1, -1, -1):
            utree = int(grid[i][col])
            uscore += 1
            if utree >= tree:
                break

        # down
        dscore = 0
        for i in range(row + 1, rows):
            dtree = int(grid[i][col])
            dscore += 1
            if dtree >= tree:
                break
        # left
        lscore = 0
        for i in range(col - 1, -1, -1):
            ltree = int(grid[row][i])
            lscore += 1
            if ltree >= tree:
                break
        # right
        rscore = 0
        for i in range(col + 1, cols):
            rtree = int(grid[row][i])
            rscore += 1
            if rtree >= tree:
                break
        scores.append(uscore * dscore * lscore * rscore)

print(sorted(scores)[-1])