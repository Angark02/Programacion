# Exporting different classes from a module
from users import Users, Admin, Privileges

marina = Admin("marina", "gomez rodriguez", 20, "spanish")
marina.privileges.show_privileges()