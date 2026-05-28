# Using the replace() method
from pathlib import Path

path = Path("learning_python.txt")
contents = path.read_text()

print(contents)

lines = contents.splitlines()
line_storing = []

print("The new lines are:")
for line in lines:
    new_line = line.replace("Python", "C")
    print(f"{new_line}\n")
    