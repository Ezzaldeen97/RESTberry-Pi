from datetime import datetime
import backend.database as db
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
        self.cursor = db.get_connection().get_cursor()

   
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

    def push_to_db(self):
        try:
            SQL_statement = f"""INSERT INTO {self.flight_type}(airline,
                            origin ,
                            Flight_number ,
                            scheduled_time ,
                            estimated_time ,
                            gate ,
                            flight_status ) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
            self.cursor.execute(SQL_statement, (self.airline, self.origin, self.flight_number, str(self.scheduled_time),
                                        str(self.estimated_time), self.gate, self.estimated_time))
        except Exception as e:
            print(f"Error in pushing the data to the db {e}")
        
        