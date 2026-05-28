# Removing all instances of specific values
sandwich_orders = ["hummus", "avocado", "cheese", "pastrami", "pastrami"]
finished_sandwiches = []

print(f"The restaurant has run out of pastrami\n")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("Althought the other sandwiches are in the oven:\n")
while sandwich_orders: # Lo mismo que poner while True (hasta que desaparezcan todos)
    sandwich = sandwich_orders.pop()
    print(f"We are making your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")