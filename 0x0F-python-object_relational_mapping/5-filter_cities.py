#!/usr/bin/python3
"""

"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    state_name = sys.argv[4]

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
        LEFT JOIN states ON cities.state_id = state.id\
        WHERE states.name LIKE BINARY (%s)\
        ORDER BY cities.id ASC", (state_name))
    rows = cur.fetchall()

    end_str = ""
    str_cities = ""
    for row in rows:
        str_cities = str_cities + end_str + row[0]
        end_str = ", "

    print(str_cities)

    cur.close()
    db.close()
