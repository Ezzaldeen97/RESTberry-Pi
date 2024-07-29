import backend.QAIA as QAIA
import backend.database as database
if __name__ == "__main__":
    print(QAIA.get_arrivals_info())
    print("Arrivals...")
    QAIA.get_departures_info()
    print("Departures...")
    
    QAIA.QAIA_Departures()
