import mysql.connector
from mysql.connector import Error

try:

    connection_SQL = mysql.connector.connect(    # I am using mysql.connector library for "is_connected, cursor"
        host='localhost',
        user='root',
        password='MySQL(2025)'
    )

    if connection_SQL.is_connected():
        cursor = connection_SQL.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except Error as e:
            print(f"Failed to create database: {e}")
        finally:
            cursor.close()
            connection_SQL.close()
        
except Error as e:
    print(f"Error while connecting to MySQL: {e}")


