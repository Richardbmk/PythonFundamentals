# 363. Bulk Inserts With Python
import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()
people = [
    ("Roald", "Amundsen", 5),
    ("Rosa", "Parks", 8),
    ("Henry", "Hundson", 7),
    ("Neil", "Armstron", 7),
    ("Daniel", "Boone", 3),
    ("Pitter", "Parker", 5)
]

c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

for person in people:
   c.execute("INSERT INTO friends VALUES (?,?,?)", person)
   print("INSERTING DATA NOW!")

avarege = 0
for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    avarege += person[2]
print(avarege/len(people))

#commit changs
conn.commit()
conn.close()
