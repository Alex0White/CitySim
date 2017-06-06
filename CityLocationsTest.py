import unittest
from CityLocations import Car

class TestCar(unittest.TestCase):
    def test_meet_with_john_num_plusone(self):
        c = Car(1)
        n = c.meet_with_john_num
        c.meet_with_john_num_plusone()
        self.assertEqual(c.meet_with_john_num, n)

    def test_exit_city_Karamu_Road(self):
        c = Car(1)
        self.assertEqual(c.exit_city("Karamu Rd"), "the driver has gone to Napier")

    def test_exit_city_Omahu_Road(self):
        c = Car(1)
        self.assertEqual(c.exit_city("Omahu Rd"), "the driver has gone to Flaxmere.")

    def test_exit_city_None(self):
        c = Car(1)
        self.assertEqual(c.exit_city(),None)




        
