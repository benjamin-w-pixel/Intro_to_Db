#!/usr/bin/python3
"""
ALX-COMPLIANT MySQL Database Script
- Uses exact 'except mysql.connector.Error' syntax
- No SELECT/SHOW statements
- Proper connection handling
"""
import mysql.connector
import sys

def create_database():
    conn = None
    try:
        # Connect with required auth plugin
        conn = mysql.connector.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            auth_plugin='mysql_native_password'
        )
        cursor = conn.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        conn.commit()
        print("Database 'alx_book_store' created successfully!")
        
        # Verify without SELECT/SHOW
        try:
            cursor.execute("USE alx_book_store")
            print("✅ Verification passed")
        except mysql.connector.Error as e:  # EXACT SYNTAX REQUIRED
            print(f"❌ Verification failed: {e}")
            
    except mysql.connector.Error as e:  # EXACT SYNTAX REQUIRED
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