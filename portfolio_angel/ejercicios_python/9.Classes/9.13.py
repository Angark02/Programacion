from random import randint

class Die:
    """A simple attempt to make a dice"""
    def __init__(self):
        """Initialize the attributes of the dice"""
        self.sides = 6
    
    def roll_die(self):
        """It will simulate rolling the die"""
        print(f"You rolled the die and got a {randint(1, self.sides)}")

die = Die()
for roll in range(10):
    die.roll_die()

die.sides = 10
for roll in range(10):
    die.roll_die()

die.sides = 20
for roll in range(10):
    die.roll_die()
    