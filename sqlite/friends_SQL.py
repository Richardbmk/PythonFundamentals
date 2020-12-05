# 361. Connecting to a DB With Python

import sqlite3
conn = sqlite3.connect("my_friends.db")
"""create cursor object"""
c = conn.cursor()
"""execute some sql"""
c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER)")
"""commit changes"""
insert_query = "INSERT INTO friends VALUES ('Merriwether', 'Lewis', 7)"
insert_query = '''INSERT INTO friends
                   VALUES ('Merriwether', 'Lewis', 7)'''
c.execute(insert_query)

"""BAD WAY, DON'T DOO"""
#form_first = "Dana"
#query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"
#c.execute(query)

"""THE RIGHT WAY!!!!!!!!!!!!"""
form_first = "Mary-Todd"
query = f"INSERT INTO friends (first_name) VALUES (?)"
c.execute(query, (form_first,))


"""THE PERFECT WAY!!!!"""
data = ("Steve", "Irwin", 9)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)
"""commit changes"""
conn.commit()
conn.close()
