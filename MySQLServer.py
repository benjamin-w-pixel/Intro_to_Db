#!/usr/bin/python3
"""
ALX MySQL Database Creation Script using mysql.connector
"""
import mysql.connector
from mysql.connector import Error
import sys

def create_database():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user=sys.argv[1],  # First argument: username
            password=sys.argv[2]  # Second argument: password
        )
        
        cursor = conn.cursor()
        
        # Create database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        
        # Verify creation
        cursor.execute("SHOW DATABASES LIKE 'alx_book_store'")
        result = cursor.fetchone()
        if result:
            print("✅ Verification: Database exists in MySQL!")
        else:
            print("❌ Database creation failed")
            
    except Error as e:
        print(f"Error: {e}")
        
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python MySQLServer.py <username> <password>")
    else:
        create_database()