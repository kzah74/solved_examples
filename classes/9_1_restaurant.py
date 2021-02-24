class Restaurant:
    """Describing a restaurant and message for opening."""

    def __init__(self, restaurant_name, cuisine_type):
        """Describing a restaurant"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Printing the restaurant`s information."""
        print(f"{self.restaurant_name} is the restaurant`s name.")
        print(f"The type of the kitchen is {self.cuisine_type}.")

    def open_restaurant(self):
        """Printing a message, indicating that the restaurant is open."""
        print(f"The {self.restaurant_name} is open now!")

restaurant = Restaurant('happy', 'international')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print("\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()

