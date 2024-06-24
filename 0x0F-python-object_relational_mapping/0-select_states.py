#!/usr/bin/python3
""" lists all states from a database. """
import MySQLdb
import sys

if __name__ == '__main__':
    mydb = MySQLdb.Connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cur = mydb.cursor()
    cur.execute("SELECT * FROM states")
    table = cur.fetchall()

    for row in table:
        print(row)

    cur.close()
    mydb.close()
