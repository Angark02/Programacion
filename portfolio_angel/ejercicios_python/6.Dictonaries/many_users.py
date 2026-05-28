# Dictonaries in a Dictionary
users = {
'angel': {
'first': 'angel',
'last': 'gomez rodriguez',
'location': 'malaga',
},
'marina': {
'first': 'marina',
'last': 'gomez rodriguez',
'location': 'malaga',
},
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    # Las siguientes dos variables podriamos no definirlas, pero es verdad que asi es más sencillo
    full_name = f"{user_info["first"]} {user_info["last"]}"
    location = user_info["location"]
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")