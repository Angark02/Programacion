# Simple Value
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('angel', 'gomez') # When returning a value its necessary to provide a variable to be assigned to
print(musician)

# Optional arguments (if we want it to be optional, we need to make it a default value)
def get_formatted_name(first_name, last_name, middle_name=""): # Using empty strings make Python interprets it like False
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('angel', 'gomez') # When returning a value its necessary to provide a variable to be assigned to
print(musician)

musician = get_formatted_name("gemma", "martlew", "cecile") # We have to make sure that middle name is the last argument
print(musician)

# Returning a dictionary
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    return person

musician = build_person('angel', 'gomez')
print(musician)

# Returning a dictionary with optional arguments
def build_person(first_name, last_name, age=None): # None evalues to false (think about it like a placeholder value)
    """Return a dictionary of information about a person."""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person

musician = build_person('angel', 'gomez', 23)
print(musician)

# Using it with while loops
def get_formatted_name(first_name, last_name): # De function definition block doesnt´t change
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name,\nYou can enter 'quit' at any time to leave: ")
    f_name = input("First Name: ")
    if f_name == "quit": # If we dont make the break statement it would be an infinite loop
        break
    l_name = input("Last Name: ")
    if l_name == "quit":
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name.title()}!")