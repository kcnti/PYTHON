import mysql.connector
from mysql.connector import errorcode

dbName = 'prac'

TABLES = {}
TABLES['info'] = (
    "CREATE TABLE `name` ("
    "   `id` int(11) NOT NULL AUTO_INCREMENT,"
    "   `firstname` varchar(255) NOT NULL,"
    "   `lastname` varchar(255) NOT NULL,"
    "   `first_date` date NOT NULL,"
    "   PRIMARY KEY (`id`)"
    ")"
)
TABLES['date'] = (
    "CREATE TABLE `idate` ("
    "   `id` int(11) NOT NULL AUTO_INCREMENT,"
    "   `from_date` date NOT NULL,"
    "   `to_date` date NOT NULL,"
    "   PRIMARY KEY (`id`)"
    ")"
)

cnx = mysql.connector.connect(user='root')
cursor = cnx.cursor()

def createDB(cursor):
    try:
        cursor.execute(
            f"CREATE DATABASE {dbName} DEFAULT CHARACTER SET 'utf8'"
        )
    except mysql.connector.Error as err:
        print(f"Failed to create DB: {err}")
        exit(1)

try:
    cursor.execute(f"USE {dbName}")
except mysql.connector.Error as err:
    print(f"database {dbName} doesn't exist.")
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        #print("this is errno", err.errno)
        createDB(cursor)
        print(f"DB {dbName} created succesfully")
        cnx.database = dbName
    else:
        print("this is err", err)
        exit(1)

for tbName in TABLES:
    table_description = TABLES[tbName]
    try:
        #print('this is table_description', table_description)
        print(f"creating table: {tbName}", end="\n")
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exist")
        else:
            print(err.msg)
    else:
        print("KK")
cursor.close()
cnx.close()