import getpass
import mysql.connector as mysql


def login(host, user, passwd, db):
    mydb = mysql.connect(host=host,
                         user=user,
                         passwd=passwd,
                         database=db)

    cursor = mydb.cursor()
    return mydb, cursor
