from unittest import TestCase
from CityLocations import Car


class TestCar(TestCase):
    def test_choose_direction(self):
        c = Car(1)
        self.assertEqual(c.choose_direction(30), 0)

    def test_choose_direction_fifty(self):
        c = Car(1)
        self.assertEqual(c.choose_direction(50), 0)

    def test_choose_direction_fifty_one(self):
        c = Car(1)
        self.assertEqual(c.choose_direction(51), 1)

    def test_road_picker(self):
        c = Car(1)
        roads = [["Murdoch Rd", "Riverslea Rd"], ["Windsor Ave", "Grove Rd"], \
                 ["Fredrick St", "Pakowhai Rd"], ["Maraekakaho Rd", "Wall Rd => Southland Rd => Murdoch Rd"]]

        self.assertEqual(c.road_picker(roads, 1, 1), "Grove Rd")

    def test_road_picker_zero(self):
        c = Car(1)
        roads = [["Murdoch Rd", "Riverslea Rd"], ["Windsor Ave", "Grove Rd"], \
                 ["Fredrick St", "Pakowhai Rd"], ["Maraekakaho Rd", "Wall Rd => Southland Rd => Murdoch Rd"]]

        self.assertEqual(c.road_picker(roads, 1, 0), "Windsor Ave")

    def test_choose_to_leave_city(self):
        c = Car(1)
        self.assertEqual(c.choose_to_leave_city(70), True)

    def test_choose_to_leave_city_false(self):
        c = Car(1)
        self.assertEqual(c.choose_to_leave_city(71), False)

    def test_circular_list(self):
        """edge test going from front to back. Returns index not items from array"""
        c = Car(1)
        array = [1, 2, 3, 4]
        self.assertEqual(c.circular_list(array, 0, 0), 3)

    def test_circular_list_index_three(self):
        """edge test going from back to front. Returns index not items from array"""
        c = Car(1)
        array = [1, 2, 3, 4]
        self.assertEqual(c.circular_list(array, 3, 1), 0)

    def test_exit_circular_list(self):
        """either iterates backward or returns the same index as input"""
        c = Car(1)
        array = [1, 2, 3, 4]
        self.assertEqual(c.exit_circular_list(array, 3, 0), 3)

    def test_exit_circular_list_index_zero(self):
        """either iterates backward or returns the same index as input"""
        c = Car(1)
        array = [1, 2, 3, 4]
        self.assertEqual(c.exit_circular_list(array, 0, 1), 3)

    def test_exit_city(self):
        c = Car(1)
        self.assertEqual(c.exit_city(None), None)

    def test_exit_city_karamu(self):
        c = Car(1)
        self.assertEqual(c.exit_city("Karamu Rd"), "Driver 1 has gone to Napier")

    def test_exit_city_omahu(self):
        c = Car(1)
        self.assertEqual(c.exit_city("Omahu Rd"), "Driver 1 has gone to Flaxmere")

    def test_met_john_message(self):
        c = Car(1)
        self.assertEqual(c.met_john_message(),"Driver 1 met with John Jamieson 0 time.")

    def test_met_john_message_once(self):
        """if test fails could be due to meet_with_john_num_plusone function being changed"""
        c = Car(1)
        c.meet_with_john_num_plusone()
        self.assertEqual(c.met_john_message(),"Driver 1 met with John Jamieson 1 time.")

    def test_met_john_message_more_than_once(self):
        """if test fails could be due to meet_with_john_num_plusone function being changed"""
        c = Car(1)
        c.meet_with_john_num_plusone()
        c.meet_with_john_num_plusone()
        self.assertEqual(c.met_john_message(), "Driver 1 met with John Jamieson 2 times.")


