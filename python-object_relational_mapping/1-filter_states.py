#!/usr/bin/python3
"""a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa:
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """ Connect to the db"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

    """ Create a cursor object"""
    cur = db.cursor()

    """ Execute a sql query"""
    cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")

    """ Fetch all rows"""
    rows = cur.fetchall()

    """ Print all rows"""
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    """ Close cursor and db """
    cur.close()
    db.close()
