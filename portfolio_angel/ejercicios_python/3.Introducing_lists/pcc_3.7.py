dinner_members = ["Spiderman", "Napoleon", "Melendi"]
print (f"Hello {dinner_members[0]}, are you fighting for world protection? or are you free this night?")
print (f"Hello {dinner_members[1]}, i know you are in your laboeur exploring new horizones, but would you like to come to my dinner party this night?")
print (f"Hello {dinner_members[2]}, i have hear that you have been looking for greens in Holanda, maybe you could give me some this night?. Love u xxx")

print(f"{dinner_members[1]} cant come to dinner, so i would have to look for another member")
dinner_members[1] = "Madonna"
print(f"Hello {dinner_members[1]}, how are you? Would you like to have a good night? Would u like to have a dinner with Melendi and Spiderman? see you this night")

print("Hey guys!!, I found a bigger table so i think im gonna invite three more guests to dinner")
dinner_members.insert(3, "Rihanna")
dinner_members.insert(4, "The Rock")
dinner_members.insert(5, "Doctor Strange")
print(f"Hello {dinner_members[3]}, would you like to come to dinner this night?")
print(f"Hello {dinner_members[4]}, would you like to come to dinner this night?")
print(f"Hello {dinner_members[5]}, would you like to come to dinner this night?")

print("Fuck, now i can only invite two guests, the new table is not arriving on time")
for guests in dinner_members[2:]:
    popped_guests = dinner_members.pop()
    print (f"Im sorry {popped_guests}, you finally cant come to dinner this night")
print (dinner_members)

for guests in dinner_members:
    print (f"Congratulations {guests}, you still can come to dinner")

del dinner_members[:]
print (dinner_members)

