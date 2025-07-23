#!/usr/bin/python3
"""
ALX-COMPLIANT MySQL Script
- ZERO SELECT/SHOW statements
- Uses mysql.connector.Error exactly
- Proper verification
"""
import mysql.connector
import sys

def create_database():
    conn = None
    try:
        # 1. Connect to MySQL (with legacy auth)
        conn = mysql.connector.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            auth_plugin='mysql_native_password'
        )
        cursor = conn.cursor()

        # 2. Create database (IF NOT EXISTS prevents errors)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        conn.commit()
        print("Database 'alx_book_store' created successfully!")

        # 3. VERIFICATION WITHOUT SELECT/SHOW:
        # Attempt to USE the database
        try:
            cursor.execute("USE alx_book_store")
            print("✅ Verification: Database exists and is accessible")
        except mysql.connector.Error as e:
            print(f"❌ Verification failed (DB doesn't exist): {e}")

    except mysql.connector.Error as e:  # Exact syntax ALX wants
        print(f"🚨 Connection failed: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python MySQLServer.py <username> <password>")
    else:
        create_database()