class Restaurant:
    """Describing a restaurant and message for opening."""

    def __init__(self, restaurant_name, cuisine_type):
        """Describing a restaurant"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Printing the restaurant`s information."""
        print(f"{self.restaurant_name} is the restaurant`s name.")
        print(f"The type of the kitchen is {self.cuisine_type}.")

    def open_restaurant(self):
        """Printing a message, indicating that the restaurant is open."""
        print(f"The {self.restaurant_name} is open now!")

    def set_number_surved(self, number_served):
        """Set the number of surved costomers."""
        self.number_served = number_served

    def increment_number_surved (self, customers):
        """Increment the number of surved customer."""
        self.number_served += customers


restaurant = Restaurant('happy', 'international')
restaurant.describe_restaurant()
print(restaurant.number_served)
restaurant.number_served = 5
print(restaurant.number_served)

restaurant.set_number_surved(8)
print(restaurant.number_served)

restaurant.increment_number_surved(15)
print(restaurant.number_served)