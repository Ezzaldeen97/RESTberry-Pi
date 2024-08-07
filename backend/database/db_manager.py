import mysql.connector
import json
import logging
logger = logging.getLogger(__name__)
import os

def connect():
    cnx = Database.get_instance()

    if cnx is None:
        cnx = Database()

    return cnx


def get_connection() :
    """
    Getter function for current Database instance.
    """
    return Database.get_instance()


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        
        self.__config = self.get_config()
        self.__cnx= None
        self.connect_db()  
    
    def connect_db(self) -> None:

        try:
            self.__cnx  = mysql.connector.connect(
            host=self.__config['db_host'],
            port=self.__config['db_port'],
            user=self.__config['db_user'],
            password=self.__config['db_password'],
            database=self.__config['db_name'], autocommit= True)
            print("Connected to the Mysql database")
        except mysql.connector.Error as e:
            logger.critical(e)
            print("Error connecting to MySQL database:", e)
        
    def get_cursor(self) :
        return self.get_connection().cursor()
    
    def get_connection(self) :
        return self.__cnx

    @staticmethod
    def get_instance() :
        return Database._instance
    
    def get_config(self):
        current_dir = os.path.dirname(__file__)
        parent_dir = os.path.dirname(os.path.dirname(current_dir))
        config_path = os.path.join(parent_dir, "config.json")
        
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config