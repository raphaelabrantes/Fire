import mysql.connector
from portas import remove_port_ip

def add_user(cursor, mydb):
    user = input("Name: ")
    ip = input("IP: ")
    query = "INSERT INTO Usuarios(name, ip) VALUES(%s, INET_ATON(%s))"
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
    user = input("Name: ")
    query1 = "SELECT Portas.ip, Portas.port FROM Portas INNER JOIN Usuarios ON Portas.ip=Usuarios.ip WHERE Usuarios.name=%s"
    cursor.execute(query1, (user, ))
    reply = cursor.fetchall()
    for ip, port in reply:
        remove_port_ip(cursor, mydb, [ip, port])
    query = "DELETE FROM Usuarios WHERE name=%s"
    cursor.execute(query, (user,))
    mydb.commit()


def remove_user_ip(cursor, mydb):
    ip = input("Ip: ")
    query = "DELETE FROM Usuarios WHERE ip=INET_ATON(%s)"
    cursor.execute(query, (ip,))
    mydb.commit()


def search_user(cursor, mydb):
    name = input("Name: ")
    ip = input("Ip: ")
    query = "SELECT name, INET_NTOA(ip) as IP FROM Usuarios WHERE name=%s OR ip=INET_ATON(%s)"
    cursor.execute(query, (name, ip))
    reply = cursor.fetchall()
    for name, ip in reply:
        print(name, ip)
