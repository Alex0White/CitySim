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
        num = random.random()
        if num > 0.5:
            num = 1
        else:
            num = 0
        return num

    def choose_to_leave_city(self, the_seed):
        random.seed(the_seed)
        num = random.random()
        if num > 0.8:
            num = 1
        else:
            num = 0
        return num

    def new_seed(self, the_seed):
        random.seed(the_seed)
        num = random.random()
        new_seed = int(num * 100)
        print(new_seed)
        return new_seed

    def circular_list(self, array, index, direction):
        """1 means up the list 0 means down """
        if direction == 1 and index == (len(array) - 1):
            new_index = 0
        elif direction == 0 and index == 0:
            new_index = len(array - 1)
        elif direction == 1:
            new_index = (index + 1)
        else:
            new_index = index - 1
        return array[index], new_index, array[new_index]

    def driver_heading(self, location, direction, roads, driver_number ):
        """Driver 3 heading from Mayfair to Stortford lodge via [option street 3]."""

        driver_number
        roads[location]
        next_location = location
        return "Driver " + str(driver_number) + " heading from "+ location +" to "+ \
               next_location +" lodge via "+ roads +"."



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


##test stuff
seed = int(input("Enter an integer: "))
c = Car(1)

n = []

while(exit == 0):

    n.append(c.choose_direction(seed))
    seed = c.new_seed(seed)
print(n)


four_locations = ["Akina", "Mayfair", "Mahora", "Storford Lodge"]
print(c.circular_list(four_locations, 3, 1))

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

thing1 = [[[0], [0]],
         [[0], [0]]]

thing2 = [[[0], [0], [0]],
         [[0], [0], [0]],
         [[0], [0], [0]]]


##for i in range(1, 5):
  ##  c = Car(i)
    ##c.choose_direction()
    
    
    
