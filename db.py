import sqlite3
from pathlib import Path

def get_home_folder():
    return str(Path.home()) + "/.aimp"

def get_db_location():
    return get_home_folder() + "/aidb.sqlite"

def get_db():
    return connection

def get_connection():
    return connection.cursor()
    
def close_db():
    connection.close()

def commit_db():
    connection.commit()

connection = sqlite3.connect(get_db_location())
