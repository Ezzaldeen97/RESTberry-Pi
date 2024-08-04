import backend.QAIA as QAIA
import backend.database as db
import logging
logger = logging.getLogger(__name__)
from datetime import datetime
if __name__ == "__main__":
    db.connect()
    logging.basicConfig(filename=f'logs/logs_{datetime.today().date()}.log', level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s -> %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filemode='w')

    logger.info('Started')
    for flight in QAIA.get_arrivals_info():
        flight.display_details()
        flight.push_to_db()
        
    for flight in QAIA.get_departures_info():
        flight.display_details()
        flight.push_to_db()
    logger.info('Finished')
