class Restaurant:
    """An attempt to represent a restaurant."""
   
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Tell us the info about the restaurant"""
        print(f"{self.name.title()} is a fantastic {self.type} restaurant.")
    
    def open_restaurant(self):
        """Tell us if it is open"""
        print(f"The restaurant is open.")
    
    def set_number_served(self, number):
        """Set the number of customers that the restaurant has served"""
        self.number_served = number

    def increment_number_served(self, increment):
        """Increment the number of customers that the restaurant has served"""
        self.number_served += increment
    

# Setting a default value for an attribute 
restaurant = Restaurant("Infinity", "Indian")

print(f"The number of customers that the restaurant has served is {restaurant.number_served}")

# Modifying attributes values throught a method
restaurant.set_number_served(20)
print(f"The number of customers that the restaurant has served is {restaurant.number_served}")

# Incrementing an attribute's value through a method
restaurant.increment_number_served(57)
print(f"The number of customers the restaurant had served in a day of business is {restaurant.number_served}.")