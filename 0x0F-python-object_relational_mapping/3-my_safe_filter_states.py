#!/usr/bin/python3
"""
 script that takes in arguments and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument.
 But this time, one that is safe from MySQL injections!
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
    cur.execute("SELECT * FROM states WHERE name = (%s)\
    ORDER BY states.id ASC", (state_name,))
    table = cur.fetchall()

    for row in table:
        print(row)

    cur.close()
    db.close()
