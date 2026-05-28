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
    
angel = Users("angel", "gomez rodriguez", 23, "spanish")
gemma = Users("gemma", "martlew", 23, "english")

angel.describe_user()
gemma.describe_user()
        