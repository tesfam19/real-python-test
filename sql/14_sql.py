# joining data from multiple tables - cleanup
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    # retrieve data
    c.execute("""SELECT population.city, population.population, 
                regions.region FROM population, regions
                WHERE population.city = regions.city ORDER by population.city ASC""")
    
    print("\nNEW DATA:\n")

    c.execute("SELECT * FROM population")

    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1], r[2])
        #print("city: " + r[0])
        #print("Population: " + str(r[1]))
        ##print("Region: " + r[2])
        #print("")