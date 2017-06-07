"""doc"""
import random

class RNG(object):
    def __init__(self, seed=58):
        self.seed = seed

    def get_seed(self):
        return self.seed

    def set_seed(self, a_seed):
        self.seed = a_seed

    def new_seed(self, the_seed):
        """create a new seed using a seed"""
        random.seed(the_seed + 1)
        num = random.random()
        new_seed = int(num * 100)
        return new_seed

class Car(object):
    """this is a Car"""
    def __init__(self, driver_number):
        self.driver_number = driver_number
        self.location = 1
        self.next_location = 0
        self.meet_with_john_num = 0

    def meet_with_john_num_plusone(self):
        self.meet_with_john_num += 1

    def set_driver_number(self, num):
        """sets the driver number 1 through to 5 according to the requirements"""
        self.driver_number = num

    def get_driver_number(self):
        return self.driver_number

    def set_location(self, num):
        """sets location should be a number 0 to 3"""
        self.location = num

    def get_location(self):
        return self.location

    def set_next_location(self, num):
        """sets location should be a number 0 to 3"""
        self.next_location = num

    def get_next_location(self):
        return self.next_location

    def choose_direction(self, the_seed):  # seed must be a int
        """psudo randomly chooses between 1 and 2"""
        if the_seed > 50:
            num = 1
        else:
            num = 0
        return num

    def road_picker(self, roads, location, direction):

        two_roads = roads[location]
        the_road = two_roads[direction]
        return the_road

    def choose_to_leave_city(self, the_seed):

        if the_seed > 70:
            return False
        else:
            return True

    def circular_list(self, array, index, direction):
        """1 means up the list 0 means down """
        if direction == 1 and index == (len(array) - 1):
            new_index = 0
        elif direction == 0 and index == 0:
            new_index = len(array) - 1
        elif direction == 1:
            new_index = (index + 1)
        else:
            new_index = index - 1
        return new_index

    def exit_circular_list(self, array, index, direction):
        """1 means up the list 0 means down """

        if direction == 1 and index == 0:
            new_index = len(array) - 1
        elif direction == 1:
            new_index = (index - 1)
        else:
            new_index = index
        return new_index

    def driver_heading(self, driver_number, location, next_location, roads):
        """Driver 3 heading from Mayfair to Stortford lodge via [option street 3]."""
        return "Driver " + str(driver_number) + " heading from "+ location \
               +" to "+ next_location +" via "+ roads +"."

    def exit_city_street(self, location, street):
        return "Driver " + str(self.driver_number) + " heading from " +\
               location + " to Outside City via " + street + "."

    def exit_city(self, exit_road=None):
        """doc"""
        if exit_road == "Karamu Rd":
            message = "Driver " + str(self.driver_number) + " has gone to Napier"
        elif exit_road == "Omahu Rd":
            message = message = "Driver " + str(self.driver_number) + " has gone to Flaxmere"
        else:
            message = None
        return message

    def met_john_message(self):
        """doc"""
        if self.meet_with_john_num == 0:
            message = "Driver " + str(self.driver_number) + \
                " met with John Jamieson 0 time."
            return message
        if self.meet_with_john_num == 1:
            message = "Driver " + \
                str(self.driver_number) + " met with John Jamieson " + \
                str(self.meet_with_john_num) + " time."
            return message
        if self.meet_with_john_num > 1:
            message = "Driver " + \
                str(self.driver_number) + " met with John Jamieson " + \
                str(self.meet_with_john_num) + " times."
            return message
        return None

    def car_final_messages(self):
        """doc"""
        if self.meet_with_john_num == 0:
            return "That passenger missed out!" + "\n-----"
        return "-----"

def main():
    with open('file.txt', 'a') as f:
        while True:
            try:
                the_input = (int(input("Enter an integer: ")))
                break
            except ValueError:
                print("Oops! that was not a interger try again")
        seed = RNG(the_input)

        for i in range(1, 6):
            c = Car(i)
            four_locations = ["Akina", "Mayfair", "Mahora", "Storford Lodge"]
            roads = [["Murdoch Rd", "Riverslea Rd" ], ["Windsor Ave", "Grove Rd"], \
                     ["Fredrick St", "Pakowhai Rd"], ["Maraekakaho Rd", "Wall Rd => Southland Rd => Murdoch Rd"]]
            exits = ["Heratanga St / Havelock Rd", "Karamu Rd", "Omahu Rd", "Railway Rd"]
            stay = True

            while stay:
                direction = c.choose_direction(seed.get_seed())
                c.set_next_location(c.circular_list(four_locations, c.get_location(), direction ))
                road = c.road_picker(roads, c.get_location(), direction)
                first = four_locations[c.get_location()]
                #print(first)
                second = four_locations[c.get_next_location()]
                #print(second)
                print(c.driver_heading(c.get_driver_number(), first, second, road), file=f)
                seed.set_seed(seed.new_seed(seed.get_seed()))
                stay = c.choose_to_leave_city(seed.get_seed())
                ##seed.set_seed(seed.new_seed(seed.get_seed()))
                c.set_location(c.get_next_location())
                if c.location == 0:
                    c.meet_with_john_num_plusone()

            exit_direction = c.choose_direction(seed.get_seed())
            exit_street = exits[c.exit_circular_list(exits, c.get_location(), exit_direction)]
            current_location = four_locations[c.get_location()]
            print(c.exit_city_street(current_location, exit_street), file=f)
            if c.exit_city(exit_street) != None:
                print(c.exit_city(exit_street), file=f)
            print(c.met_john_message(), file=f)
            print(c.car_final_messages(), file=f)

if __name__ == '__main__':
    main()






    
    
