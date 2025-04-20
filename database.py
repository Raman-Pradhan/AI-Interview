# database.py
import sqlite3

DB_NAME = "LoginData.db"

def create_tables():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS USERS (
                name TEXT NOT NULL,
                email TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)
        conn.commit()

def add_user(name, email, password):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO USERS (name, email, password) VALUES (?, ?, ?)", (name, email, password))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False  # Email already exists

def get_user_by_email(email):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, email, password FROM USERS WHERE email = ?", (email,))
        return cursor.fetchone()
