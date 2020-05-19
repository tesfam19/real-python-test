# create a SQLite3 database and table 
import sqlite3

with sqlite3.connect("new.db") as connection:
    #get a cursor object used to execute SQL commands 
    c = connection.cursor()
    #insert data
    c.execute("INSERT INTO population VALUES('New York City', \
    'NY', 8400000)")
    c.execute("INSERT INTO population VALUES('San Francisco', \
    'CA', 8000000)")

