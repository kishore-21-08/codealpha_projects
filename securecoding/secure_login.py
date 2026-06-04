import sqlite3
import hashlib

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

username = input("Enter Username: ")
password = input("Enter Password: ")

hashed_password = hashlib.sha256(password.encode()).hexdigest()

query = "SELECT * FROM users WHERE username=? AND password=?"

cursor.execute(query, (username, hashed_password))

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Invalid Credentials")

connection.close()
