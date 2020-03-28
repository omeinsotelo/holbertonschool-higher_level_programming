#!/usr/bin/python3
# lists all states with a name starting with N

# import modules
import sys
import MySQLdb


if __name__ == '__main__':
    # Arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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
    # Exceute query
    sql = "SELECT *\
        FROM states\
        WHERE name\
        LIKE BINARY 'N%'\
        ORDER BY states.id ASC"
    # Exceute query
    cursor.execute(sql)
    # fetches and return list
    records = cursor.fetchall()
    # print tuple
    for row in records:
        print(row)
    cursor.close()
    db.close()
