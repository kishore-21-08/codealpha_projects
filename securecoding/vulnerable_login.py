import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

username = input("Enter Username: ")
password = input("Enter Password: ")

query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

cursor.execute(query)

result = cursor.fetchone()

if result:
    print("Login Successful")
else:
    print("Invalid Credentials")

connection.close()
