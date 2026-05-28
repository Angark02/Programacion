# Buying cinema tickets!!

buying_tickets = True
total_cost = 0

print("Welcome to Yelmo Cines,")
while buying_tickets:
    age = int(input(f"\nWould u like to buy a ticket? Enter ur age: "))
    if age < 3:
        print(f"\nYour ticket is free!!")
        total_cost += 0
    elif 3 <= age <= 12:
        print(f"Your ticket cost is $10")
        total_cost += 10
    else:
        print(f"Your ticket cost is $15")
        total_cost += 15
    
    repeat = input(f"\nWould u like to buy another ticket?\t(yes/no)  ")
    if repeat.lower() == "no":
        buying_tickets = False

total_cost = print(f"The total cost is: ${total_cost}")