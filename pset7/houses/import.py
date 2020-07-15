# TODO
import csv
from sys import argv
import sqlite3

con = sqlite3.connect("students.db")  # connect to database
cur = con.cursor()

if len(argv) != 2:  # check if the number of command-line arguments is correct
    print('Usage: python import.py characters.csv')
    exit(0)

file_name = argv[1]

with open(file_name, "r") as file:  # read the csv file from the command-line argument

    reader = csv.DictReader(file)

    # insert data from csv file to students table in database
    for row in reader:
        name = row['name'].split(' ')
        if len(name) == 3:
            cur.execute("INSERT INTO students (first,middle,last,house,birth) VALUES(?,?,?,?,?);",
                        (name[0], name[1], name[2], row['house'], row['birth']))
        elif len(name) == 2:
            cur.execute("INSERT INTO students (first,last,house,birth) VALUES(?,?,?,?);",
                        (name[0], name[1], row['house'], row['birth']))
        con.commit()


con.close()  # close the database