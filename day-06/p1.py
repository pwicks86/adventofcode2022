import sys
import os

with open("input.txt", "r") as f:
    puz = f.read()

for i in range(len(puz) - 4):
    chunk = puz[i:i+4]
    chunk_set = set(chunk)
    if len(chunk_set) == 4:
        print(i + 4)
        break
    
