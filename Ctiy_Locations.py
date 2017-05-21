class Car(object):

    def __init__(self):
        return None
    def choose_direction(self):
        return None
    def exit_city(self, location):
        if(location == "Karamu Road"):
            message = "the driver has gone to Napier"
        if(location == "Omahu Road"):
            message = "the driver has gone to Flaxmere."
        return message
    
    def met_john_message(self, int met_with_john_number, int driver_number):
        
        message = ""
        if(met_with_john_number == 0):
            message = "Driver " + str(driver_number) + "met with John Jamieson 0 time."
        if(met_with_john_number > 0):
            message = "Driver " + str(driver_number) + "met with John Jamieson " + str(met_with_john_number) + " times."
        return None

        

    def car_final_messages(self, int met_with_john, int driver_number):
        if(met_with_john == 0):


        return " \n -----"


##random.seed(a=None)
