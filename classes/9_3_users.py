class User:
    """Representing a user profile."""
    def __init__(self, first_name, last_name, username, email, location):
        """Take the user`s information."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Print a summary of the user`s information."""
        print(f"{self.first_name} {self.last_name}:")
        print(f"Username: {self.username}")
        print(f"The profile is registered with the email: {self.email}.")
        print(f"And {self.location} is the location of the registration.")

    def greet_user(self):
        """Printing a personalized greeting to the user."""
        print(f"\nWelcome, {self.username}! We are happy to join us!")

user_1 = User('simon', 'buratti', 'sbur', 'sbur@gmail.com', 'sofia')
user_1.describe_user()
user_1.greet_user()
print("\n")

user_2 = User('mike', 'baldi', 'miba', 'miba@abv.bg', 'sofia')
user_2.describe_user()
user_2.greet_user()
print("\n")

user_3 = User('ivan', 'ivanov', 'iv', 'iv@abv.bg', 'sofia')
user_3.describe_user()
user_3.greet_user()