import mysql.connector
from portas import remove_total_ip


def add_user(cursor, mydb):
    query = "INSERT INTO Usuarios(name, ip) VALUES(%s, INET_ATON(%s))"
    user = input("Name: ")
    ip = input("IP: ")
    cursor.execute(query, (user, ip))
    mydb.commit()
    print(cursor.rowcount)


def show_users(cursor, mydb):
    query = "SELECT name, INET_NTOA(ip), date_add FROM Usuarios"
    cursor.execute(query)
    reply = cursor.fetchall()
    for nome, ip, data in reply:
        print("%s\t\t%s\t%s" % (nome, ip, data.strftime("%m/%d/%Y, %H:%M:%S")))


def remove_user_n(cursor, mydb):
    query_s = "SELECT Portas.ip FROM Portas INNER JOIN Usuarios ON Portas.ip=Usuarios.ip WHERE Usuarios.name=%s LIMIT 1"
    query_d = "DELETE FROM Usuarios WHERE name=%s"
    user = input("Name: ")
    cursor.execute(query_s, (user, ))
    reply = cursor.fetchall()
    for ip in reply:
        remove_total_ip(cursor, mydb, ip[0])
    cursor.execute(query_d, (user,))
    mydb.commit()


def remove_user_ip(cursor, mydb):
    query = "DELETE FROM Usuarios WHERE ip=INET_ATON(%s)"
    ip = input("Ip: ")
    cursor.execute(query, (ip,))
    mydb.commit()


def search_user(cursor, mydb):
    query = "SELECT name, INET_NTOA(ip) as IP FROM Usuarios WHERE name=%s OR ip=INET_ATON(%s)"
    name = input("Name: ")
    ip = input("Ip: ")
    cursor.execute(query, (name, ip))
    reply = cursor.fetchall()
    for name, ip in reply:
        print(name, ip)
