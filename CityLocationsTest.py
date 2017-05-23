import unittest
from CityLocations import Car

class CarTest(unittest.TestCase):
    def test_exit_city_Karamu_Road(self):
        c = Car(1)
        self.assertEqual(c.exit_city("Karamu Road"), "the driver has gone to Napier")

    def test_exit_city_Omahu_Road(self):
        c = Car(1)
        self.assertEqual(c.exit_city("Omahu Road"), "the driver has gone to Flaxmere.")

    def test_exit_city_None(self):
        c = Car(1)
        self.assertEqual(c.exit_city(),None)
        
