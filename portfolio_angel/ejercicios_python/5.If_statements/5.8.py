# If statement + lists
usernames = ["angel", "marina", "miguel", "eli", "admin"]

for username in usernames:
    if username == "admin":
        print("Hello admin, would u like to see a status report?")
    else:
        print(f"Hello {username}, thank u for logging in again")