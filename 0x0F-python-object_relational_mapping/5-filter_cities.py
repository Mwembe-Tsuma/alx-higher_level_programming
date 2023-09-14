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
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])

    rows = cur.fetchall()
    i = []
    for r in rows:
        i.append(r[1])
    print(", ".join(i))
    cur.close()
    db.close()
