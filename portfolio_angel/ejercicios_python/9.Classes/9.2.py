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

# Adding another two instances
restaurant2 = Restaurant("Karmela", "Alternative")
restaurant3 = Restaurant("La Despensa Familiar", "Spanish")

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
