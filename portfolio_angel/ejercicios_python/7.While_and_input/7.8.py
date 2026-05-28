# Moving items from one list to another
sandwich_orders = ["hummus", "avocado", "cheese"]
finished_sandwiches = []

while sandwich_orders: # Lo mismo que poner while True (hasta que desaparezcan todos)
    sandwich = sandwich_orders.pop()
    print(f"We are making your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")