pizzas = ["mushrooms", "cheese", "pepperoni"]
for pizza in pizzas:
    print(pizza)

# 4.1.2
for pizza in pizzas:
    print(f"{pizza.title()} pizzas are one of my favourites")
    
# 4.1.3
print("Fuck!, I really love eating pizzas, I could be all the day eating them")

friends_pizzas = pizzas[:]
pizzas.append("eggs")
friends_pizzas.append("salami")

print(f"My favourite pizzas are:")
for i in pizzas:
    print(i)

print("My friend\'s favourite pizzas are:")
for i in friends_pizzas:
    print(i)
