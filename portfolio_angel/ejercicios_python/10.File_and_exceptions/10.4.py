# Guest: Registration book
from pathlib import Path

path = Path("guest.txt")

guest_name = input("Tell me ur name: ")

path.write_text(guest_name)