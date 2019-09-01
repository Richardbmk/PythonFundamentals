# 314. Reading CSV Files

# with open("filesio/fighters.csv") as file:
#     print(file.read())

#Using CSV Module

"""Using reader"""
# from csv import reader
# with open("filesio/fighters.csv") as file:
#     csv_reader = reader(file)
#     for row in csv_reader:
#         # each row is a list!
#         print(row)

# from csv import reader
# with open("filesio/fighters.csv") as file:
#     csv_reader = reader(file)
#     next(csv_reader) # avoid the headers
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")
#         # each row is a list!
#         # print(row)

# from csv import reader
# with open("filesio/fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)
#     print(data)

# if the info is separated with a diferent dilimiter (",", "|", ... )
# from csv import reader
# with open("filesio/fighters1.csv") as file:
#     csv_reader = reader(file, delimiter="|")
#     for row in csv_reader:
#         print(row)

"""Using DictReader"""
# from csv import DictReader
# with open("filesio/fighters.csv") as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader:
#         # each row is an OrderedDict"
#         # print(row)
#         print(row["Name"])

# Writing Files in CSV

"""Using writer"""
# from csv import writer
# with open("filesio/test.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Character", "Move"])
#     csv_writer.writerow(["Ryu", "Hadouken"])

""" EXAMPLE. Reading, and wrting in a existing file """
# from csv import reader, writer

# with open("filesio/fighters.csv") as file:
#     csv_reader = reader(file)
#     fighters = [[s.upper() for s in row] for row in csv_reader]
#     for row in fighters:
#         print(row)
#
# with open("filesio/Upperfighters.csv", "w") as file:
#     csv_writer = writer(file)
#     for fighter in fighters:
#         csv_writer.writerow(fighter)

# with open("filesio/fighters.csv") as file:
#     csv_reader = reader(file)
#     with open("filesio/Upperfighters1.csv", "w") as file:
#         csv_writer = writer(file)
#         for fighter in csv_reader:
#             csv_writer.writerow([s.upper() for s in fighter])
""" Using DictWriter"""
# from csv import writer, DictWriter
# # Version usir writer
# with open("filesio/cats.csv", "w") as file:
#     headers = ["Name", "Breed", "Age"]
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "Name": "Garfield",
#         "Breed": "Orange Tabby",
#         "Age": 10
#     })

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
