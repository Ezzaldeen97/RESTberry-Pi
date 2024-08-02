import backend.QAIA as QAIA
import backend.database as db
if __name__ == "__main__":
    db.connect()
    for flight in QAIA.get_arrivals_info():
        flight.display_details()
        
    for flight in QAIA.get_arrivals_info():
        flight.display_details()
