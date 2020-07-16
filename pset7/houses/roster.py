# TODO
import csv
from sys import argv
import sqlite3

con = sqlite3.connect("students.db")  # connect to database
cur = con.cursor()

if len(argv) != 2:  # check if the number of command-line arguments is correct
    print('Usage: python roster.py Gryffindor')
    exit(0)

cur.execute(f"SELECT * FROM students WHERE house = '{argv[1]}' ORDER BY last, first;")  # execute query
con.commit
rows = cur.fetchall()
my_list = []

for i in range(len(rows)):  # store the data form database in a list
    row = [e for e in rows[i]]
    if row[2] == None:
        result = f'{row[1]} {row[3]}, born {row[5]}'
    else:
        result = f'{row[1]} {row[2]} {row[3]}, born {row[5]}'
    my_list.append(result)

for line in my_list:  # print the results
    print(line)

con.close()  # close the database connection
