#!/usr/bin/python3

# Test for equality and inequality / lower() and upper() methods
laptop = "Macbook"
gaming_pc = "Asus"

print(laptop.lower() == "macbook")
print(gaming_pc.upper() != "Asus")


# Numerical tests and the "and" / "or" keywords

age = 18
age2 = 21

if age >= 18 and age2 <=21:
    print("You two have been admitted")

# Using lists

colors = ["blue", "red", "green"]

color = "blue"

if color not in colors:
    print(f"fuck, i thoght {color} was the good one")
else:
    print(f"I knew {color} was the right choice")
 
