from datetime import datetime
import backend.database as db
import logging
logger = logging.getLogger(__name__)

class Flight:
    def __init__(self, flight_content, flight_type, sql_statement) :

        self.list_of_items = flight_content.find_all("td")
        self.airline = self.__get_airline()
        self.location = self.__get_distance()
        self.flight_type = flight_type
        self.flight_number = self.__get_flight_number()
        self.scheduled_time = self.__get_schedule_time()
        self.estimated_time = self.__get_estimated_time()
        self.gate = self.__get_gate()
        self.status = self.__get_status()
        self.cursor = db.get_connection().get_cursor()
        self.SQL_statement = sql_statement
   
    def __get_airline(self):
        return self.list_of_items[1].string
        
    def __get_distance(self):
        return self.list_of_items[2].string
        
    def __get_flight_number(self):
        return self.list_of_items[3].string
        
    def __get_schedule_time(self):
        datetime_scheduled_time = datetime.strptime(self.list_of_items[4].string, "%d/%m/%Y %H:%M")
        if datetime_scheduled_time.date() != datetime.today().date():
            logger.info(f"Skipped the flight {self.flight_number} because it isnt today, its on {str(datetime_scheduled_time)}| {self.flight_type}")
            raise ValueError(f"The flight isnt scheduled today, the flight is {str(datetime_scheduled_time)}")
        return datetime_scheduled_time
        
        
    def __get_estimated_time(self):
        datetime_estimated_time = datetime.strptime(self.list_of_items[5].string, "%d/%m/%Y %H:%M")

        return datetime_estimated_time
        
    def __get_gate(self):
        return self.list_of_items[6].string
        
    def __get_status(self):
        return self.list_of_items[7].string
    
    def display_details(self):
        print( self.airline,'|', self.location,'|', self.flight_number,'|', self.scheduled_time,'|', self.estimated_time ,'|',self.gate ,'|',self.status,'|', self.flight_type)

    def push_to_db(self):

        try:
            self.cursor.execute(self.SQL_statement, (self.airline, self.location, self.flight_number, str(self.scheduled_time),
                                        str(self.estimated_time), self.gate, self.status))
        except Exception as e:
            logger.critical(e)
            print(f"Error in pushing the data to the db {e}")
        
        