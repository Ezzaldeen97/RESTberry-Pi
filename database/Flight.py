class Flight:
    def __init__(self, flight_content) :

        self.list_of_items = flight_content.find_all("td")
        self.airline = self.__get_airline()
        self.origin = self.__get_distance()
        self.flight_number = self.__get_flight_number()
        self.scheduled_time = self.__get_schedule_time()
        self.estimated_time = self.__get_estimated_time()
        self.gate = self.__get_gate()
        self.status = self.__get_status()
    def __str__(self):
        return self.airline,'|', self.origin,'|', self.flight_number,'|', self.scheduled_time,'|', self.estimated_time ,'|',self.gate ,'|',self.status

    def __get_airline(self):
        return self.list_of_items[1].string
        
    def __get_distance(self):
        return self.list_of_items[2].string
        
    def __get_flight_number(self):
        return self.list_of_items[3].string
        
    def __get_schedule_time(self):
        return self.list_of_items[4].string
        
    def __get_estimated_time(self):
        return self.list_of_items[5].string
        
    def __get_gate(self):
        return self.list_of_items[6].string
        
    def __get_status(self):
        return self.list_of_items[7].string
        