from datetime import datetime
class Flight:
    def __init__(self, flight_content, flight_type) :

        self.list_of_items = flight_content.find_all("td")
        self.airline = self.__get_airline()
        self.origin = self.__get_distance()
        self.flight_number = self.__get_flight_number()
        self.scheduled_time = self.__get_schedule_time()
        self.estimated_time = self.__get_estimated_time()
        self.gate = self.__get_gate()
        self.status = self.__get_status()
        self.flight_type = flight_type
    # def __str__(self):
    #     return self.airline,'|', self.origin,'|', self.flight_number,'|', self.scheduled_time,'|', self.estimated_time ,'|',self.gate ,'|',self.status

    def __get_airline(self):
        return self.list_of_items[1].string
        
    def __get_distance(self):
        return self.list_of_items[2].string
        
    def __get_flight_number(self):
        return self.list_of_items[3].string
        
    def __get_schedule_time(self):
        datetime_scheduled_time = datetime.strptime(self.list_of_items[4].string, "%d/%m/%Y %H:%M")
        return datetime_scheduled_time
        
    def __get_estimated_time(self):
        datetime_estimated_time = datetime.strptime(self.list_of_items[5].string, "%d/%m/%Y %H:%M")

        return datetime_estimated_time
        
    def __get_gate(self):
        return self.list_of_items[6].string
        
    def __get_status(self):
        return self.list_of_items[7].string
    
    def display_details(self):
        print( self.airline,'|', self.origin,'|', self.flight_number,'|', self.scheduled_time,'|', self.estimated_time ,'|',self.gate ,'|',self.status,'|', self.flight_type)

