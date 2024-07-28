import requests
from bs4 import BeautifulSoup as bs
from Flight import Flight


class QAIA:
    BASE_URL ='https://qaiairport.com/en/flight-information/Pages/'
    
    def __init__(self):
        self.flights:list[Flight] = []
    def fetch_data(self,url):
        try:
            self.resp = requests.get(url)
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

class QAIA_Arrivals(QAIA):
    BASE_URL = QAIA.BASE_URL+'Arrivals.aspx'

    def __init__(self):
        self.time = 0
        super().__init__()

        self.fetch_data(QAIA_Arrivals.BASE_URL)
        self.parse_data()


class QAIA_Departures(QAIA):
    BASE_URL = QAIA.BASE_URL+'Departures.aspx'
    
    def __init__(self):
        self.time = 0
        super().__init__()
        self.fetch_data(QAIA_Departures.BASE_URL)
        self.parse_data()



