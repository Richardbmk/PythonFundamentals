# 365. SQL INJECTION!
"""THESE WAY IS TO EASE TO HACK!!!!!!!!!!!!1 DO NOT USEEEEEEE"""
import sqlite3
conn = sqlite3.connect("users.db")

#query = "CREATE TABLE users (username TEXT, password TEXT)"

u = input("please enter you username...")
p = input("please enter your password...")
query = f"SELECT * FROM users WHERE username='{u}' AND password = '{p}'"

c = conn.cursor()
c.execute(query)

result = c.fetchone()
if(result):
    print("WELCOME BACK")
else:
    print("FAILED TO LOGIN")

conn.commit()
conn.close()