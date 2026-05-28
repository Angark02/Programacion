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

# Adding Admin class
class Admin(Users):
    """Represent the info of the Admin user, an specific type of user"""
    def __init__(self, first_name, last_name, age, nationality):
        """Initialize atributter of the parent class"""
        super().__init__(first_name, last_name, age, nationality)
        self.privileges = ["can add post", "can edit passwords", "can delete other users profiles"]
    
    def show_privileges(self):
        """It will show us which are the privileges of been an admin"""
        print(f"\nThe privileges {self.first_name.title()} has for been and admin are:")
        for admin in self.privileges:
            print(f"* {admin}\n")

angel = Users("angel", "gomez rodriguez", 23, "spanish")
gemma = Users("gemma", "martlew", 23, "english")
marina = Admin("marina", "gomez rodriguez", 20, "spanish")

marina.show_privileges()