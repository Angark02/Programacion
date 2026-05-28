#!/usr/bin/python3
# No es por chulear ni nada pero esto ha sido editado desde "vi" en mi terminal😎

responses = {}

polling_active = True
while polling_active:
    name = input("\nTell me babe, whats ur name?: ")
    game = input("Which game would u like to play this night?: ")
    name = name.title()
    game = game.title()
    responses[name] = game # Aquí básicamente lo que estamos haciendo es que añadimos los dos inputs al diccionario "responses".

    repeat = input("Would u like to let another person respond? (yes/no)")
    if repeat.lower() == "no":
        polling_active = False

print("\n--- The Poll Results Are ---")
for name, game in responses.items():
    print(f"\n{name} would like to play {game} thins night.")

