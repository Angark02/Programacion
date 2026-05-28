# Exit method of 7.4 exercise
print("\nHi!! Welcome to TelePizza,")

topping = " "
while topping != "quit":
    topping = input("\nWhich topping would u like to add to ur pizza?\nWrite 'quit' if u wanna exit: ")
    
    if topping != "quit":
        print("We will add that topping to your pizza")
        
# Exit method conditional statement


# Exit with active variable
print("\nHi!! Welcome to TelePizza,")

active = True
while active:
    topping = input("\nWhich topping would u like to add to ur pizza?\nWrite 'quit' if u wanna exit: ")

    if topping == "quit":
        active = False
    else:
        print("We will add that topping to your pizza")
        
# Exit with break
while True:
    topping = input("\nWhich topping would u like to add to ur pizza?\nWrite 'quit' if u wanna exit: ")
    if topping == "quit":
        break
    else:
        print("We will add that topping to your pizza")   