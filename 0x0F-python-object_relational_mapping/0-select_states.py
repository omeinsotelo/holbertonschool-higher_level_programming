#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa

# import modules
import sys
import MySQLdb


if __name__ == '__main__':
    # Arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # conecting to de database
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
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    # fetches and return list
    records = cursor.fetchall()
    # print tuple
    for row in records:
        print(row)
    cursor.close()
    db.close()
