# insert command with error handler
import sqlite3

with sqlite3.connect("new.db") as connection:
    #get a cursor object used to execute SQL commands 
    c = connection.cursor()
    try:
        # insert data
        c.execute("INSERT INTO population VALUES('New York city', 'NY', 8400000)")
        c.execute("INSERT INTO population VALUES('San Francisco', 'CA', 8000000)")
        # commit the changes 
        #c.commit()
    except sqlite3.OperationalError:
        print("Oops! something went wrong. Try again ...")
