# Reading and printing from a file
from pathlib import Path
path = Path("learning_python.txt")
contents = path.read_text()

print(contents)

lines = contents.splitlines()
line_storing = []

for line in lines:
    line_storing.append(line)

print(line_storing)
