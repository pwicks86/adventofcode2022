import sys
import os

with open("input.txt", "r") as f:
    puz = f.read()

for i in range(len(puz) - 14):
    chunk = puz[i:i+14]
    chunk_set = set(chunk)
    if len(chunk_set) == 14:
        print(i + 14)
        break
    
