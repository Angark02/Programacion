current_users = ["angel", "marina", "miguel", "eli", "admin"]
new_users = ["gemma", "laura", "angel", "marina"]

for user in new_users:
    if user in current_users:
        print(f"We are sorry, {user.title()} already exists, enter a new username")
    else:
        print(f"Congrats, {user.title()} has not been registered yet.")