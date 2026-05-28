# Modifying a list without using functions
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}") # Simulate printing each design, until none are left.
    completed_models.append(current_design) # Move each design to completed_models after printing.

print("\nThe following models have been printed:")
for completed_model in completed_models: # Display all completed models.
    print(completed_model)
    
# We can use two functions instead, each of which does one specific job.
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that where printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

"""
This program is easier to extend and maintain than the version with-out functions. 
If we need to print more designs later on, we can simply call print_models() again
"""

# If we dont want to empty the list of unprinted designs we can call print_models() like this:
# print_models(unprinted_designs[:], completed_models)