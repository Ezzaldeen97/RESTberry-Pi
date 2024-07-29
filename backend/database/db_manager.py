import mysql.connector
import json

def get_connection():
    config = get_config()
    try:
        connection = mysql.connector.connect(
            host=config['db_host'],
            port=config['db_port'],
            user=config['db_user'],
            password=config['db_password'],
            database=config['db_name']
        )
        return connection
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)
        return None
    
def get_config():
    config_path = "config.json"
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config