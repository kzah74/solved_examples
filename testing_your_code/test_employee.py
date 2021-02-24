import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Testing for the class Employee."""

    def setUp(self):
        """Creating an instance."""
        self.mike = Employee('mike', 'buratti', 65_000)

    def test_give_default_raise(self):
        """Testing for the default raising of salary."""
        self.mike.give_raise()
        self.assertEqual(self.mike.annual_salary, 70_000)

    def test_give_custom_raise(self):
        """Testing for giving a custom raising of salary."""
        self.mike.give_raise(10_000)
        self.assertEqual(self.mike.annual_salary, 75_000)

if __name__ == '__main__':
    unittest.main()
