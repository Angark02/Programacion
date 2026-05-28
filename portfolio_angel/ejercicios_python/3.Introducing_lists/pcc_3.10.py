things = ["pen", "dog", "trousers", "gym", "book", "apple"]

print(things) # Creating a list

print(things[2]) # Accesing a certain element in a list

print(things[-2]) # Accesing a certain element starting by the end of the list

message = f"My {things[1]} is a little idiot" # Using individual values
print(message)

# Modifying elements i a list
things[3] = "sausage"
print(things)

# Adding elements in a list (append() and insert() methods)
things.append("gym")
print(things)

things.insert(4, "mouse")
print(things)

# Removing elements in a list (del, pop()), remove() methods)
del things[3]
print(things)

popped_things = things.pop() # This method remove the last item inserted
print(things)
print(popped_things) # To see which element we have popped

things.pop(0)
print(things)

things.remove("mouse") # Useful if we cant remember the position of the value
print(things)

# Sorting a list
things.sort() # It sort the list in alphabetical order
print(things)

things.sort(reverse=True) 
print(things)

print(sorted(things)) # If we want to maintain the original order

print(sorted(things, reverse=True)) # Reversing the sorted list

things.reverse() # It reverses the order
print(things)

# Finding the length
print(len(things))