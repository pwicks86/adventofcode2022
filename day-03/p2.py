import sys
import os

with open("input.txt", "r") as f:
    lines = f.readlines()

out = 0
for l in lines:
    first, second = l[:len(l)//2], l[len(l)//2:]
    fs = set(list(first))
    ss = set(list(second))
    common = (fs & ss).pop()
    if common.islower():
        pri = (ord(common) - ord('a')) + 1
    else:
        pri = (ord(common) - ord('A')) + 27
    out += pri

print(out)

