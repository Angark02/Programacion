responses = {}
active = True

while active:
    name = input("Hi!!,\nWrite ur name please: ")
    place = input("If u could visit one place in the world,\nWhere would u go?: ")
    responses[name] = place
    
    repeat = input("Would you like to let other people take the poll?\n Please, enter (yes/no): ")
    if repeat.lower() == "no":
        active = False
  
print("--- Poll Results ---")      
for name, place in responses.items():
    print(f"\n{name.title()} would love to visit {place.title()}.")
    