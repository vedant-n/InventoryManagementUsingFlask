import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="P@ni0000",
        database="inventory_db"
    )
