import backend.QAIA as QAIA
import backend.database as database
if __name__ == "__main__":

    for flight in QAIA.get_arrivals_info():
        flight.display_details()
        
    for flight in QAIA.get_arrivals_info():
        flight.display_details()
