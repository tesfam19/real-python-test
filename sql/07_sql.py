# select statement 
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    # use a for loop to iterate through the database and printing the data
    for row in c.execute("SELECT firstname, lastname from employees"):
        print(row)