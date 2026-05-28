# Importing from different modules: Admin, Privileges and Users
from users import Users
from admin_privileges import Admin, Privileges

marina = Admin("marina", "gomez rodriguez", 20, "spanish")
marina.privileges.show_privileges()
