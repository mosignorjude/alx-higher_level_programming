#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
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
    state_name = sys.argv[4]

    # creates a cursor object to execute queries.
    cur = mydb.cursor()

    query = "SELECT * FROM states WHERE name = '%{}%'\
    ORDER BY states.id ASC".format(state_name)
    cur.execute(query)

    # fetches result.
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    mydb.close()
