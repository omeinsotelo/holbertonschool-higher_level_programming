#!/usr/bin/python3
# takes in an argument and displays all values
# in the states table of hbtn_0e_0_usa where name matches the argument.

# import modules
import sys
import MySQLdb

if __name__ == '__main__':
    # Arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name_input = sys.argv[4]

    # conecting to database
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
        WHERE BINARY name = '{}'\
        ORDER BY states.id ASC".format(name_input)
    # Exceute query
    cursor.execute(sql)
    # fetches and return list
    records = cursor.fetchall()
    # print tuple
    for row in records:
        print(row)
    cursor.close()
    db.close()
