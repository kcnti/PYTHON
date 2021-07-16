import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', database='prac')
cursor = cnx.cursor()

query = ("SELECT firstname, lastname, first_date FROM name WHERE first_date BETWEEN %s and %s")

fday = datetime.date(2004, 1, 1)
lday = datetime.date(2004, 2, 29)

cursor.execute(query, (fday, lday))

for (firstname, lastname, first_date) in cursor:
    print(f"{firstname} {lastname} was born on {first_date}")

cnx.close()