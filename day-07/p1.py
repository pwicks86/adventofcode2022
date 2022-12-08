import sys
import os
from pprint import pp
from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.readlines()

cur_dir = None

fs = {}
top_level = fs

for num, l in enumerate(lines):
    words = l.split()
    if words[0] == "$":
        command = words[1]
        if command == "cd":
            new_dir = words[2]
            if new_dir == "/":
                cur_dir = "/"
                fs = top_level
            elif new_dir == "..":
                cur_dir = cur_dir[0:cur_dir.rfind("/")]
                if (cur_dir == ""):
                    cur_dir = "/"
                fs = top_level
                for d in [x for x in cur_dir.split("/") if x]:
                    fs = fs[d]
            else:
                if cur_dir[-1] == "/":
                    cur_dir = cur_dir + new_dir  
                else:
                    cur_dir = cur_dir + "/" + new_dir  

                fs = fs[new_dir]
        elif command == "ls":
            pass
    else:
        if words[0] == "dir":
            if words[1] not in fs:
                fs[words[1]] = {}
        else:
            fs[words[1]] = int(words[0])


cool_dirs = 0

def process(fdir):
    global cool_dirs
    dir_size = 0
    for key, val in fdir.items():
        if type(val) is dict:
            dir_size += process(val)
        else:
            dir_size += val
    if (dir_size <= 100000):
        cool_dirs += dir_size

    return dir_size

process(top_level)
print(cool_dirs)
