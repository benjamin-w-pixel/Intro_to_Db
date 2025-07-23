#!/usr/bin/python3
"""
ALX MySQL Database Creator
- Uses mysql.connector
- NO SELECT/SHOW statements
- Proper error handling
"""
import mysql.connector
import sys

def create_database():
    try:
        # Connect to MySQL (without specifying a database)
        conn = mysql.connector.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            auth_plugin='mysql_native_password'
        )
        cursor = conn.cursor()

        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        conn.commit()
        print("Database 'alx_book_store' created successfully!")

        # Verification method that doesn't use SELECT/SHOW
        # Just attempt a harmless operation
        cursor.execute("SET @dummy = 1")
        print("✅ Database connection verified")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python MySQLServer.py <username> <password>")
    else:
        create_database()