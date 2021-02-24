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


restaurant_1 = Restaurant('happy', 'international')
restaurant_1.describe_restaurant()
print("\n")

restaurant_2 = Restaurant('luchoni', 'any type')
restaurant_2.describe_restaurant()
print("\n")

restaurant_3 = Restaurant('dominos', 'pizzeria')
restaurant_3.describe_restaurant()