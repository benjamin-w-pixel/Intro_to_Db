#!/usr/bin/python3
"""
ALX-compliant MySQL Database Creation Script
- Uses mysql.connector
- No SELECT/SHOW statements
- Proper exception handling
"""
import mysql.connector
from mysql.connector import Error
import sys

def create_database():
    conn = None
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2]
        )
        
        cursor = conn.cursor()
        
        # Create database (IF NOT EXISTS prevents errors)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        conn.commit()
        print("Database 'alx_book_store' created successfully!")
        
        # Verify without SELECT/SHOW - attempt to use the database
        try:
            cursor.execute("USE alx_book_store")
            print("✅ Verification: Database is accessible")
        except Error as e:
            print(f"❌ Verification failed: {e}")
            
    except Error as e:
        print(f"🚨 Database error: {e}")
        
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python MySQLServer.py <username> <password>")
    else:
        create_database()