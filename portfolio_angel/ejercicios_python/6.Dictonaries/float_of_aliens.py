# We will make an empty list for storing our aliens
aliens = []

# Making 30 green aliens
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# We will show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...") # Esto es solo decorativo, para indicar que la cuenta sigue

# Showing how many aliens have been created
print(f"\nThe total number of aliens in the float is {len(aliens)}")

# Changing values
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

# Showing the first 5 aliens again
for alien in aliens[:5]:
    print(alien)
print("...")

# Editing more and more values... Red aliens are comming!!
for alien in aliens[:6]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    else:
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

for alien in aliens[:9]:
    print(alien)
print("...")