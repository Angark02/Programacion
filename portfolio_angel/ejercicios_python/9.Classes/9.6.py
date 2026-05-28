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
        
# Adding a class that inherit from Restaurant
class IceCreamStand(Restaurant):
    """An attempt to represent an ice cream stand, a specific type of restaurant"""
    def __init__(self, name, type):
        """Initialize attributes of the parent class"""
        super().__init__(name, type)
        self.flavors = ["chocolate", "vanilla", "strawberry"]
    
    def display_flavors(self):
        """Display the flavors of the ice cream stand"""
        print(f"The ice cream flavors {self.name.title()} can offer are:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

ice_cram_stand = IceCreamStand("Kalua", "Ice Cream")
ice_cram_stand.display_flavors()
