class Restaurant:
    """An attempt to represent a restaurant."""
   
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def describe_restaurant(self):
        """Tell us the info about the restaurant"""
        print(f"{self.name.title()} is a fantastic {self.type} restaurant.")
    
    def open_restaurant(self):
        """Tell us if it is open"""
        print(f"The restaurant is open.")
    
restaurant = Restaurant("Infinity", "Indian")
print(f"The restaurant's name is {restaurant.name}.")
print(f"It has {restaurant.type}'s cuisine.")

restaurant.describe_restaurant()
restaurant.open_restaurant()
