import sys
import os

with open("input.txt", "r") as f:
    lines = f.readlines()

move_map = {
    ord("A"): "R",
    ord("B"): "P",
    ord("C"): "S",
    ord("X"): "R",
    ord("Y"): "P",
    ord("Z"): "S"
}

score = 0
for line in lines:
    opp, me = [ord(m) for m in line.split()]
    opp = opp - ord('A')
    me = me - ord('X')
    if me == opp:
        score += 3 + me + 1
        continue
    if me == ((opp + 1) % 3):
        # win
        score += 6 + me + 1
    else:
        # loss
        score +=  me + 1

print(score)


