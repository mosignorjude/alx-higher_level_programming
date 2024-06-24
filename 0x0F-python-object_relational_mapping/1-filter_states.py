#!/usr/bin/python3
""" lists all states from a database. """
import MySQLdb
import sys

if __name__ == '__main__':
    # creates a connection object using database credentials.
    mydb = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    # creates a cursor object to execute queries.
    cur = mydb.cursor()
    cur.execute("SELECT * FROM states")
    # fetches result.
    table = cur.fetchall()

    for row in table:
        print(row)

    cur.close()
    mydb.close()
