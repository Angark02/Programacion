alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])

new_points = alien_0["points"]
print(f"Congrats!!, u just earned {new_points} points")

# Adding cordinates to our alien
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# Modifying our alien's values
alien_0["color"] = "yellow"
alien_0["points"] = 10
print(f"WOW, now u killed a {alien_0["color"]} alien, u just earned {alien_0["points"]}points")

# Determining how far to the right aour alien should move
alien_0["speed"] = "medium"
print(f"The original position: {alien_0["x_position"]}")

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"The new position of our alien is {alien_0["x_position"]}")

# It's cool 'cause changing one value, we can change the overall behavior of the alien