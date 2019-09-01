# FILES EXERCIES!!!!!!!!!

# # Exercise add_user
# from csv import writer, DictWriter
# # MY SOLUTION
# """ This solution is not correct becouse over write the existin files
# and it should add information..."""
# def add_user(FirsName, LastName):
#     with open("filesio/users.csv", "w") as file:
#         headers = ["FirsName", "LastName"]
#         csv_writer = DictWriter(file, fieldnames=headers)
#         csv_writer.writeheader()
#         csv_writer.writerow({
#             "FirsName": FirsName,
#             "LastName": LastName,
#         })

# # COLT SOLUTION
# from csv import writer
#
# def add_user(first_name, las_name):
#     with open("filesio/usersColt.csv", "a") as file:
#         csv_writer = writer(file)
#         csv_writer.writerow([first_name, las_name])
#
""" APLICANDO UN IDEA INTERESANTE..."""
from csv import writer, DictWriter

def create_file(fileName, first_row, second_row):
    with open(f"filesio/{fileName}.csv", "w") as file:
        headers = [first_row, second_row]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()

def add_rows(fileName, first_row, second_row):
    with open(f"filesio/{fileName}.csv", "a") as file:
        csv_writer = writer(file)
        csv_writer.writerow([first_row, second_row])


# create_file("Frutas", "Nombre", "Peso")
# add_rows("Frutas", "Banana", "200 g")
# add_rows("Frutas", "Fresa", "50 g")
# add_rows("Frutas", "Kiwi", "250 g")

# Print_users EXERCISES

# my solution!!!
from csv import reader

def print_users(fileName):
    with open(f"filesio/{fileName}.csv") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            print(row)


# COLT SOLUTION!!!!
import csv

def print_users():
    with open("filesio/users.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row["FirsName"], row["LastName"])

# print_users()
# Another solution made by me
# import csv

def print_users(fileName):
    with open(f"filesio/{fileName}.csv") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # print(row["Nombre"], row["Peso"])
            print(row)

# print_users("Frutas")

# EXERCISE find_user
#COLT SOLUTOIN!!!
import csv

def find_user(first_name, last_name):
    with open("filesio/Frutas.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        for (index, row) in enumerate(csv_reader):
            first_name_match = first_name == row[0]
            last_name_match = last_name == row[1]
            if first_name_match and last_name_match:
                return index
            return f"{first_name}, {last_name}"

# find_user("Fresa", "50 g")
