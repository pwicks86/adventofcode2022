import sys
import os

with open("input.txt", "r") as f:
    puz = f.readlines()

cur_sum = 0
cals = []
for line in puz:
    if not line.isspace():
        cur_sum += int(line)
    else:
        cals.append(cur_sum)
        cur_sum = 0

print(sum(list(reversed(sorted(cals)))[:3]))
