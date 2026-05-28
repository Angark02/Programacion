class Users:
    """It tell us info about users"""
    def __init__(self, first_name, last_name, age, nationality, login_attemps):
        """Initialize attributes of the users"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.login_attemps = login_attemps
    
    def describe_user(self):
        """Tell us all the users information"""
        print(f"User information:\nName: {self.first_name.title()} {self.last_name.title()};\nAge: {self.age};\nNationality: {self.nationality}\n")

# Adding login attemps   
    def increment_login_attemps(self):
        """It will icrement the number of login attemps by 1"""
        self.login_attemps += 1
    
    def reset_login_attemps(self):
        """It will reset the number of login attemps to 0"""
        self.login_attemps = 0
    
angel = Users("angel", "gomez rodriguez", 23, "spanish", 0)

angel.increment_login_attemps()
angel.increment_login_attemps()
angel.increment_login_attemps()

print(f"The number of login attemps is {angel.login_attemps}")

angel.reset_login_attemps()

print(f"The number of login attemps is {angel.login_attemps}")