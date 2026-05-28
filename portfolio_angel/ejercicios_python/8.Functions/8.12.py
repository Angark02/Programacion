def sandwich_toppings(*toppings):
    """Summary of the sandwich that is being ordered"""
    print("You have ordered your sandwich with the next toppings:")
    for topping in toppings:
        print(f" - {topping.title()}")

sandwich_toppings("tuna", "tomato", "lettuce")
sandwich_toppings("hummus", "ham", "extra salt")
sandwich_toppings("avocado", "lettuce", "ham", "tomato")
