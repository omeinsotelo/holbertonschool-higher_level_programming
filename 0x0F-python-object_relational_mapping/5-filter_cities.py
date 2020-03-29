#!/usr/bin/python3
# script that takes in the name of a state
# as an argument and lists all cities
# of that state, using the database hbtn_0e_4_usa

# import modules
import sys
import MySQLdb

if __name__ == '__main__':
    # Arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_inp = sys.argv[4]

    # connect the db
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # Cursor class
    cursor = db.cursor()
    # Query
    sql = "SELECT cities.name\
        FROM cities\
        INNER JOIN states\
        ON cities.state_id = states.id\
        AND states.name = %s\
        ORDER BY cities.id ASC"
    # Exceute query
    cursor.execute(sql, (name_inp, ))
    # fetches and return list
    records = cursor.fetchall()
    # print name with separator
    separator = ""
    for row in records:
        print("{}{}".format(separator, row[0]), end="")
        separator = ", "
    print("")
    cursor.close()
    db.close()
