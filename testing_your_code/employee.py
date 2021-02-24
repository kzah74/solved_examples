class Employee:
    """Collect the first name, last name and annual salary and store them."""

    def __init__(self, first_name, last_name, annual_salary):
        """Take the information for the employee."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Giving a raise amount by default."""
        self.annual_salary += amount

