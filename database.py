"""
Module to handle Database for user authentication
"""

import sqlite3

class Database:
    """Class to handle database operations for user management"""
    
    def __init__(self, db_name='users.db'):
        """Initialize database and create tables"""
        self.db_name = db_name
        self.create_database()

    def create_database(self):
        """Create database schema if not exists and insert a sample user"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Create users table if not exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        
        # Insert default test user (prevent duplicates with INSERT OR IGNORE)
        cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ('test_user', '123456'))
        conn.commit()
        conn.close()

    def authenticate_user(self, username, password):
        """Verify user credentials against database"""
        
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        # Get user entry from database against the credentials
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        
        return user is not None     # Return True if user exists with given credentials
        