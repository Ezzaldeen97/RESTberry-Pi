import requests
from bs4 import BeautifulSoup as bs
from Flight import Flight

class QAIA:
    BASE_URL = 'https://qaiairport.com/en/flight-information/Pages/Arrivals.aspx'

    def __init__(self):
        self.time = 0
        self.flights:list[Flight] = []
        self.fetch_data()
        self.parse_data()
    def fetch_data(self):
        try:
            self.resp = requests.get(QAIA.BASE_URL)
        except requests.exceptions as e:
            print('Fetching data failed', e)

    def parse_data(self):
        try:
            soup = bs(self.resp.text, features='html.parser')

            flights = soup.find_all("tbody")[0]
        except Exception as e:
            print('Parsing data failed', e)
        for flight in flights:
            if flight.string =='\n':
                continue
            self.flights.append(Flight(flight))
            # print(flights[0])
        # for index, i in enumerate(self.flights):
        #     print(index, '|', i.airline,'|', i.origin,'|', i.flight_number,'|', i.scheduled_time,'|', i.estimated_time ,'|',i.gate ,'|',i.status,'|')




