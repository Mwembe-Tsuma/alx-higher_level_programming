#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    nameSr = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cur.execute(nameSr)

    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()