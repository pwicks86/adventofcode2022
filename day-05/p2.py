from collections import defaultdict
import sys
import os

with open("input.txt", "r") as f:
    puz = f.read()


stack, moves = [x.strip() for x in puz.split("\n\n")]

stacks = defaultdict(list)

stack_rows = stack.count("\n")
for idx, c in enumerate(stack.splitlines()[-1]): 
    if not c.isspace():
        for row in range(stack_rows - 1, -1, -1):
            stack_letter = stack.splitlines()[row][idx]
            if stack_letter.isspace():
                break
            stacks[int(c)].append(stack_letter)

for m in moves.splitlines():
    val, start, end = [int(x) for x in m.split() if x.isdigit()]
    move_list = []
    for i in range(val):
        move_list.append((stacks[start].pop()))
    stacks[end].extend(reversed(move_list))

out = ""
for i in range(1, 10):
    out += stacks[i][-1]
print(out)