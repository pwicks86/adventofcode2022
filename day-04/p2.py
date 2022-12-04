import sys
import os

with open("input.txt", "r") as f:
    lines = f.readlines()

def overlap(outer, inner):
    return outer[0] <= inner[0] <= outer[1] or outer[0] <= inner[1] <= outer[1]

count = 0
for l in lines:
    a, b = [[int(v) for v in r.split("-")] for r in l.split(",")]
    if overlap(a,b) or overlap(b,a):
        count += 1

print(count)
