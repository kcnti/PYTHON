import mysql.connector
import sys
from datetime import date, datetime, timedelta

fname = sys.argv[1]
lname = sys.argv[2]
cnx = mysql.connector.connect(user='root', database='prac')
cursor = cnx.cursor()
tomorrow = datetime.now().date() + timedelta(days=1)

insertINFO = ("INSERT INTO name (id, firstname, lastname, first_date) VALUES (NULL, %s, %s, %s)")
insertDATE = ("INSERT INTO idate (id, from_date, to_date) VALUES (NULL, %(from_date)s, %(to_date)s)")

info = (fname, lname, date(2004, 2, 27))

cursor.execute(insertINFO, info)
number = cursor.lastrowid

_date = {
    'from_date' : tomorrow,
    'to_date' : date(9999, 1, 1) 
}
cursor.execute(insertDATE, _date)

cnx.commit()
cursor.close()
cnx.close()
print("insert successfully")