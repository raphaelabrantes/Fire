import getpass
import mysql.connector as mysql


def login(host, user, passwd, db):
    mydb = mysql.connect(host=host,
                         user=user,
                         passwd=passwd,
                         database=db)

    cursor = mydb.cursor()
    while True:
        user = input("Login: ")
        password = getpass.getpass(prompt='Password: ', stream=None)
        query = "SELECT COUNT(*) as T FROM Administrador WHERE name=%s AND password=MD5(%s)"
        cursor.execute(query, (user, password))
        x = cursor.fetchone()[0]
        if x:
            mydb.close()
            cursor.close()
            mydb = mysql.connect(host=host,
                                 user=user,
                                 passwd=password,
                                 database=db)
            cursor = mydb.cursor()
            break
        else:
            print("Usuario ou senha incorretos")

    return (mydb, cursor)
