import backend.QAIA as QAIA
import backend.database as db
import logging
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    db.connect()
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    for flight in QAIA.get_arrivals_info():
        flight.display_details()
        flight.push_to_db()
        
    for flight in QAIA.get_departures_info():
        flight.display_details()
        flight.push_to_db()
    logger.info('Finished')
