# Rivers
rivers = {
    "guadalquivir": "spain",
    "sena": "france",
    "nile": "egypt",
}
for river, country in rivers.items():
    print(f"\nThe river {river.title()}, in {country.title()}, is known for been so tourist atractive")

print("The most famous rivers are:")
for river in rivers.keys():
    print(f"\n{river.title()}")

print("\nThe countries where the most famous rivers are located are:")
for country in rivers.values():
    print(f"\n{country.title()}")