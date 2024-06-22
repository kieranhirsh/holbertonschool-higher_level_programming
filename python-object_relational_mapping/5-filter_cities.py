#!/usr/bin/python3
""" the checker demands documentation """


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    cr = db.cursor()
    cr.execute("SELECT cities.id, cities.name, states.name\
               FROM cities\
               LEFT JOIN states\
               ON cities.state_id=states.id\
               WHERE states.name='{}'\
               ORDER BY cities.id ASC;".format(sys.argv[4]))
    rows = cr.fetchall()
    for row in rows:
        print(row)

    cr.close()
    db.close()
