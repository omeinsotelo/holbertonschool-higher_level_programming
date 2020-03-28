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
    sql = "SELECT *\
        FROM states\
        WHERE name = %s\
        ORDER BY states.id ASC"
    # Exceute query
    cursor.execute(sql, (name_inp,))
    # fetches and return list a tuples
    records = cursor.fetchall()
    # print tuple
    for row in records:
        print(row)
    cursor.close()
    db.close()
