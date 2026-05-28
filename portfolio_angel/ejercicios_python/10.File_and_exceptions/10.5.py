# Guest: Registration book
from pathlib import Path

path = Path("guest_book.txt")
guests = " "

while True:
    guest_name = input("Tell me ur name:\nType 'q' if you want to quit registration process: ")
    if guest_name == "q":
        break
    else:
        guests += f"Guest: {guest_name.title()}\n"

path.write_text(guests)