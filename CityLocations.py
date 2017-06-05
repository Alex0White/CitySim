"""doc"""
import random




class RNG(object):
    def __init__(self, seed=58):
        self.seed = seed

    def get_set_seed(self):
        self.seed = self.new_seed(self.seed)
        return self.seed

    def get_seed(self):
        return self.seed

    def set_seed(self, a_seed):
        self.seed = a_seed



    def new_seed(self, the_seed):
        random.seed(the_seed)
        num = random.random()
        new_seed = int(num * 100)

        return new_seed




class Car(object):
    """this is a Car"""
    def __init__(self, driver_number):
        self.driver_number = driver_number
        self.location = random.randint(0, 3)
        self.next_location = 0





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


        if the_seed > 49:
            return False
        else:
            return True


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
            new_index = len(array) - 1
        elif direction == 1:
            new_index = (index + 1)
        else:
            new_index = index - 1
        return new_index

    def driver_heading(self, driver_number, location, next_location, roads):
        """Driver 3 heading from Mayfair to Stortford lodge via [option street 3]."""



        return "Driver " + str(driver_number) + " heading from "+ location +" to "+ next_location +" via "+ roads +"."



    def exit_city(self, location=None):
        """doc"""
        if location == 1 or 2:
            message = "the driver has gone to Napier"
        elif location == 2 or 3:
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

def main():
    seed = RNG(int(input("Enter an integer: ")))
    for i in range(1, 6):
        c = Car(i)
        four_locations = ["Akina", "Mayfair", "Mahora", "Storford Lodge"]
        roads = [["Murdoch Rd", "Riverslea Rd" ], ["Windsor Ave", "Grove Rd"], ["Fredrick St", "Pakowhai Rd"], ["Maraekakaho Rd", "Wall Rd => Southland Rd => Murdoch Rd"]]

        stay = True
        while stay:
            direction = c.choose_direction(seed.get_seed())
            c.set_next_location(c.circular_list(four_locations, c.get_location(), direction ))
            road = c.road_picker(roads, c.get_location(), direction)

            first = four_locations[c.get_location()]
            print(first)

            second = four_locations[c.get_next_location()]
            print(second)
            print(c.driver_heading(c.get_driver_number(), first, second, road))

            seed.set_seed(seed.new_seed(seed.get_seed()))
            stay = c.choose_to_leave_city(seed.get_seed())
            seed.set_seed(seed.new_seed(seed.get_seed()))


            c.set_location(c.get_next_location())

        print("exit city " + str(c.get_driver_number()))

if __name__ == '__main__':
    main()


##test stuff

##seed = int(input("Enter an integer: "))
##c = Car(1)

##n = []

# while(exit == 0):
#
#     n.append(c.choose_direction(seed))
#     seed = c.new_seed(seed)
# print(n)
#
#
# four_locations = ["Akina", "Mayfair", "Mahora", "Storford Lodge"]


##print(c.circular_list(four_locations, 3, 1))

##print(c.circular_list(four_locations, 0, 0))
##print(c.circular_list(four_locations, 1, 0))
##print(c.circular_list(four_locations, 4, 1))


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
    
    
    
