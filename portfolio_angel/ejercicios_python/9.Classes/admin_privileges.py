""" Classes Admin and Privileges in a separated file """
from users import Users

class Admin(Users):
    """Represent the info of the Admin user, an specific type of user"""
    def __init__(self, first_name, last_name, age, nationality):
        """Initialize atributter of the parent class"""
        super().__init__(first_name, last_name, age, nationality)
        self.privileges = Privileges()

class Privileges:
    """A simple attemp to represent the privileges of an admin user"""
    def __init__(self, privileges = ["can add post", "can edit passwords", "can delete other users profiles"]):
        """Initialize the privileges attributes"""
        self.privileges = privileges
    
    def show_privileges(self):
        """It will show us which are the privileges of been an admin"""
        print(f"\nThe privileges for been an admin are:")
        for privilege in self.privileges:
            print(f"* {privilege}\n")