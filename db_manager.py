import sqlite3
import os
import hashlib

class DatabaseManager:
    def __init__(self):
        self.db_path = 'pos_database.db'

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
        conn = self.get_connection()
        try:
            with open('database/schema.sql', 'r') as f:
                conn.executescript(f.read())
            conn.commit()
        finally:
            conn.close()

    def create_admin_user(self):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            # Check if admin user exists
            cursor.execute('SELECT id FROM users WHERE username = ?', ('admin',))
            if cursor.fetchone() is None:
                # Create admin user with password 'admin123'
                password_hash = hashlib.sha256('admin123'.encode()).hexdigest()
                cursor.execute(
                    'INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)',
                    ('admin', password_hash, 'admin')
                )
                conn.commit()
        finally:
            conn.close()

    def verify_login(self, username, password):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            cursor.execute(
                'SELECT id, role FROM users WHERE username = ? AND password_hash = ?',
                (username, password_hash)
            )
            result = cursor.fetchone()
            if result:
                return {'id': result[0], 'username': username, 'role': result[1]}
            return None
        finally:
            conn.close()
