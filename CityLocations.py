"""doc"""
import random


class Car(object):
    """this is a Car"""
    def __init__(self, driver_number):
        self.driver_number = driver_number
        self.location = random.randint(1, 4)
    def set_driver_number(self, num):
        """sets the driver number 1 through to 5 according to the requirements"""
        self.driver_number = num

    def choose_direction(self, the_seed):  # seed must be a int
        """psudo randomly chooses between 1 and 2"""
        random.seed(the_seed)
        num = random.randint(0, 1)
        return num

    def exit_city(self, location=None):
        """doc"""
        if location == "Karamu Rd":
            message = "the driver has gone to Napier"
        elif location == "Omahu Rd":
            message = "the driver has gone to Flaxmere."
        else:
            message = None
        return message

    def met_john_message(self, met_with_john_number, driver_number):
        """doc"""
        if met_with_john_number == 0:
            message = "Driver " + str(driver_number) + \
                "met with John Jamieson 0 time."
        if met_with_john_number > 0:
            message = "Driver " + \
                str(driver_number) + "met with John Jamieson " + \
                str(met_with_john_number) + " times."
        return None

    def car_final_messages(self, met_with_john, driver_number):
        """doc"""
        if met_with_john == 0:
            return None
        return " \n -----"

c = Car(1)
n = []
for i in range(30, 41):
    print(i)
    n.append(c.choose_direction(i))
print(n)


four_locations = ["Akina", "Mayfair", "Mahora", "Storford Lodge"]

exits = [ "Heratanga St / Havelock Rd", "Karamu Rd", "Omahu Rd", "Railway Rd"] 
            #Right          #left
"Akina" "Riverslea Rd" "Murdoch Rd" 
            #Right          #left
"Mahora" "Pakowhai Rd" "Fredrick St"
            #Right          #left
"Mayfair" "Grove Rd" "Windsor Ave"
            #Right                                          #left
"Stortford Lodge" "Wall Rd => Southland Rd => Murdoch Rd" "Maraekakaho Rd"

roads = [["Riverslea Rd", "Murdoch Rd"], ["Grove Rd", "Windsor Ave"], ["Pakowhai Rd", "Fredrick St"], ["Wall Rd => Southland Rd => Murdoch Rd" "Maraekakaho Rd"]]

thing = [[[0], [0]],
         [[0], [0]]]

thing = [[[0], [0], [0]],
         [[0], [0], [0]],
         [[0], [0], [0]]]


for i in range(1, 5):
    c = Car(i)
    