from pathlib import Path
import os
import sys
day_num = int(sys.argv[1])
os.mkdir(f"day-{day_num:02d}")

template="""import sys
import os

with open("input.txt", "r") as f:
    lines = f.readlines()
"""

with open(f"day-{day_num:02d}/p1.py", "w") as f:
    f.write(template)

Path(f"day-{day_num:02d}/input.txt").touch()
