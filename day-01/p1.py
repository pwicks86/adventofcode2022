import sys
import os

with open("input.txt", "r") as f:
    puz = f.readlines()

max_val = 0
cur_sum = 0
for line in puz:
    if not line.isspace():
        cur_sum += int(line)
    else:
        max_val = max(max_val, cur_sum)
        cur_sum = 0

print(max_val)
