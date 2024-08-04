import requests
from bs4 import BeautifulSoup as bs
from .Flight import Flight
import logging
logger = logging.getLogger(__name__)

def get_arrivals_info():
    return QAIA_Arrivals()

def get_departures_info():
    return QAIA_Departures()

class QAIA:
    BASE_URL ='https://qaiairport.com/en/flight-information/Pages/'
    
    def __init__(self):
        self.flights:list[Flight] = []

    def __iter__(self):
        return iter(self.flights)
    def fetch_data(self,url):
        try:
            self.resp = requests.get(url)
        except requests.exceptions as e:
            print('Fetching data failed', e)

    def parse_data(self, flight_type, sql_statement):
        try:
            soup = bs(self.resp.text, features='html.parser')

            flights = soup.find_all("tbody")[0]
        except Exception as e:
            print('Parsing data failed', e)
        for flight in flights:
            if flight.string =='\n':
                continue
            try:
                self.flights.append(Flight(flight, flight_type, sql_statement))
            except ValueError as e:
                pass




class QAIA_Arrivals(QAIA):
    SQL_ARRIVALS =f"""INSERT INTO Arrivals(airline,
                            origin ,
                            Flight_number ,
                            scheduled_time ,
                            estimated_time ,
                            gate ,
                            flight_status ) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    BASE_URL = QAIA.BASE_URL+'Arrivals.aspx'

    def __init__(self):
        self.time = 0
        super().__init__()

        self.fetch_data(QAIA_Arrivals.BASE_URL)
        self.parse_data("Arrivals", QAIA_Arrivals.SQL_ARRIVALS)


class QAIA_Departures(QAIA):
    BASE_URL = QAIA.BASE_URL+'Departures.aspx'
    SQL_DEPARTURES ="""INSERT INTO Departures(airline,
                            destination ,
                            Flight_number ,
                            scheduled_time ,
                            estimated_time ,
                            gate ,
                            flight_status ) VALUES(%s, %s, %s, %s, %s, %s, %s)"""
    def __init__(self):
        self.time = 0
        super().__init__()
        self.fetch_data(QAIA_Departures.BASE_URL)
        self.parse_data("Departures", QAIA_Departures.SQL_DEPARTURES)



