from user import User
from privileges import Admin, Privileges

mbur = Admin('mike', 'buratti', 'mbur', 'mbur@gmail.com', 'sofia')
mbur.describe_user()
print("\n")

mbur_privileges = []

mbur.privileges.privileges = mbur_privileges
mbur.privileges.show_privileges()
