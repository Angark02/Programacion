# Simpler Code: removing temporarty variables such as "lines" and looping directly over a list
from pathlib import Path

path = Path("learning_python.txt")

contents = path.read_text()

line_storing = []

for line in contents.splitlines():
    line_storing.append(line)

print(line_storing)
