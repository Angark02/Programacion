""" Classes and Instances: Admin, Privileges and Users """
class Users:
    """It tell us info about users"""
    def __init__(self, first_name, last_name, age, nationality):
        """Initialize attributes of the users"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
    
    def describe_user(self):
        """Tell us all the users information"""
        print(f"User information:\nName: {self.first_name.title()} {self.last_name.title()};\nAge: {self.age};\nNationality: {self.nationality}\n")

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

class Admin(Users):
    """Represent the info of the Admin user, an specific type of user"""
    def __init__(self, first_name, last_name, age, nationality):
        """Initialize atributter of the parent class"""
        super().__init__(first_name, last_name, age, nationality)
        self.privileges = Privileges()
