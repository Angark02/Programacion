class Dog:
    """My first attempt to model a class"""
    
    def __init__(self, name, age): # Self is required in the method definition
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over")

# Making an instance for a class:    
my_dog = Dog("India", 15)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old")

# Calling methods:
my_dog.sit()
my_dog.roll_over()

# Creating Multiple Instances
your_dog = Dog("Molly", 13)

print(f"\nYour dog's name was {your_dog.name}.")
print(f"Your dog was {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()