class User:
    """Representing a user profile."""
    def __init__(self, first_name, last_name, username, email, location):
        """Take the user`s information."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user`s information."""
        print(f"{self.first_name} {self.last_name}:")
        print(f"Username: {self.username}")
        print(f"The profile is registered with the email: {self.email}.")
        print(f"And {self.location} is the location of the registration.")

    def greet_user(self):
        """Printing a personalized greeting to the user."""
        print(f"\nWelcome, {self.username}! We are happy to join us!")

    def increment_login_attempts(self):
        """Increment the value of login attempts by 1."""
        self.login_attempts += 1

    def reset_loging_attempts(self):
        """Resets the value of loging attempts to 0."""
        self.login_attempts = 0

class Admin(User):
    """Representing an administrator profile."""
    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin"""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        print("Privileges of the administrator profile:")
        for privilege in self.privileges:
            print("- " + privilege)

admin_user = Admin('kristiyan', 'alexiev', 'kristal', 'kristal@abv.bg', 'sofia')
admin_user.describe_user()
print("\n")

admin_user.privileges = [
            'can add post',
            'can delete post',
            'can ban user',
            ]

admin_user.show_privileges()
