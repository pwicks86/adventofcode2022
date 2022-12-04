import sys
import os

with open("input.txt", "r") as f:
    lines = f.readlines()

out = 0
for lg in zip(*(iter(lines),) * 3):
    lg_sets = []
    for l in lg:
        lg_sets.append(set(list(l.strip())))
    common = (lg_sets[0] &  lg_sets[1] & lg_sets[2]).pop()
    if common.islower():
        pri = (ord(common) - ord('a')) + 1
    else:
        pri = (ord(common) - ord('A')) + 27
    out += pri

print(out)

