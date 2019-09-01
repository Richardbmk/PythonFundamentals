# 364. Selecting With Python
import sqlite3
conn = sqlite3.connect("my_friends.db")

# Create cursor object
c = conn.cursor()
#c.execute("SELECT * FROM friends")

#c.execute("SELECT * FROM friends WHERE first_name IS 'Steve'")

c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")

#for result in c:
#    print(result)

#print(c.fetchall())
#print(c.fetchone())
print(c.fetchall())



# commit changes
conn.commit()
conn.close()

