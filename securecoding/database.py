# setup_database.py

import sqlite3
import hashlib

# Connect database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
""")

# Sample user
username = "kishore"

# Hash password
password = "kis123"
hashed_password = hashlib.sha256(password.encode()).hexdigest()

# Insert user
cursor.execute(
    "INSERT INTO users (username, password) VALUES (?, ?)",
    (username, hashed_password)
)

conn.commit()

print("Database and user created successfully!")

conn.close()
