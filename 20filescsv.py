# 314. Reading CSV Files

with open("filesio/fighters.csv") as file:
    print(file.read())

#Using CSV Module

"""Using reader"""
from csv import reader
with open("filesio/fighters.csv") as file:
    csv_reader = reader(file)
    for row in csv_reader:
        # each row is a list!
        print(row)

from csv import reader
with open("filesio/fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader) # avoid the headers
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")
        # each row is a list!
        # print(row)

from csv import reader
with open("filesio/fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)
    print(data)

# if the info is separated with a diferent dilimiter (",", "|", ... )
from csv import reader
with open("filesio/fighters1.csv") as file:
    csv_reader = reader(file, delimiter="|")
    for row in csv_reader:
        print(row)

"""Using DictReader"""
from csv import DictReader
with open("filesio/fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # each row is an OrderedDict"
        # print(row)
        print(row["Name"])

# Writing Files in CSV

"""Using writer"""
from csv import writer
with open("filesio/test.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])

""" EXAMPLE. Reading, and wrting in a existing file """
# from csv import reader, writer

with open("filesio/fighters.csv") as file:
    csv_reader = reader(file)
    fighters = [[s.upper() for s in row] for row in csv_reader]
    for row in fighters:
        print(row)
#
with open("filesio/Upperfighters.csv", "w") as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)

with open("filesio/fighters.csv") as file:
    csv_reader = reader(file)
    with open("filesio/Upperfighters1.csv", "w") as file:
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])

""" Using DictWriter"""
from csv import writer, DictWriter
# Version usir writer
with open("filesio/cats.csv", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Garfield",
        "Breed": "Orange Tabby",
        "Age": 10
    })

from csv import DictReader, DictWriter
def cm_to_in(cm):
    return float(cm) * 0.393701

with open("filesio/fighters.csv") as file:
    csv_reader = DictReader(file)
    # print(list(csv_reader))
    fighters = list(csv_reader)

with open("filesio/inches_fighters.csv", "w") as file:
    headers = ("Name", "Country", "Height")
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for f in fighters:
        csv_writer.writerow({
            "Name": f["Name"],
            "Country": f["Country"],
            "Height": cm_to_in(f["Height (in cm)"])
        })



## COPY PASTE CODE SOLUTION ####
# Ejercicio de codificación 101: find_user
import csv
 
def find_user(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
        return "{} {} not found.".format(first_name, last_name)



# Ejercicio de codificación 102: update_users
import csv
 
def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
 
    return "Users updated: {}.".format(count)



# Ejercicio de codificación 103: delete_users

import csv
 
def delete_users(first_name, last_name):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == first_name and row[1] == last_name:
                count += 1
            else:
                csv_writer.writerow(row)
 
    return "Users deleted: {}.".format(count)

