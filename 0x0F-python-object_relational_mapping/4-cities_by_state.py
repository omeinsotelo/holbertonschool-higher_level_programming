#!/usr/bin/python3
# script that takes in arguments and displays all values in the
# states table of hbtn_0e_0_usa where name matches the argument.
# But this time, write one that is safe from MySQL injections!

# import modules
import sys
import MySQLdb

if __name__ == '__main__':
    # Arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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
    sql = "SELECT cities.id, cities.name, states.name\
        FROM cities\
        LEFT JOIN states\
        ON cities.state_id = states.id\
        ORDER BY cities.id ASC"
    # Exceute query
    cursor.execute(sql)
    # fetches and return list
    records = cursor.fetchall()
    # print tuple
    for row in records:
        print(row)
    cursor.close()
    db.close()
