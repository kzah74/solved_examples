import unittest
from city_functions import get_city_country

class NamesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""
    def test_city_country(self):
        """Do city_country_name like 'Santiago, Chile' work?"""
        city_country_name = get_city_country('santiago', 'chile')
        self.assertEqual(city_country_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do city_country_name_population like"""
        """'Santiago, Chile - population 5000000' work?"""
        city_country_population = get_city_country('santiago', 'chile', '5000000')
        self.assertEqual(city_country_population, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()