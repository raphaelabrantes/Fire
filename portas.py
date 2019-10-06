import mysql.connector
import os


def add_port(cursor, mydb):
    show_ports(cursor, mydb)
    ip = input("IP: ")
    port = input("Port: ")
    query = "INSERT INTO Portas(ip, port) VALUES(INET_ATON(%s), %s)"
    try:
        cursor.execute(query, (ip, port))
        mydb.commit()
        command = "ufw allow from {}  to any port {}".format(ip, port)
    except mysql.connector.errors.IntegrityError as e:
        # TODO verificar exatamente o erro
        print("Port already open to this IP")

    except mysql.connector.errors.DatabaseError as e:
        print("Data is not in right format")
    else:
        reply = list(os.popen(command))
        print(reply[0])


def show_ports(cursor, mydb):
    query = "SELECT INET_NTOA(ip), port, date_add FROM Portas"
    cursor.execute(query)
    reply = cursor.fetchall()
    for ip, port, data in reply:
        print("%s\t\t%s\t%s" % (ip, port, data.strftime("%m/%d/%Y, %H:%M:%S")))


def remove_ports(cursor, mydb):
    show_ports(cursor, mydb)
    port = input("Port: ")
    string = "ufw delete allow from {} to any port {}"
    query1 = "SELECT ip FROM Portas WHERE port=%s"
    query2 = "DELETE FROM Portas WHERE port=%s"
    cursor.execute(query1, (port,))
    select = cursor.fetchall()
    cursor.execute(query2, (port,))
    mydb.commit()
    for ip in select:
        command = string.format(ip, port)
        reply = os.popen(command)
        print(reply)


def remove_port_ip(cursor, mydb, query=None):
    if query:
        ip = query[0]
        port = query[1]
    else:
        show_ports(cursor, mydb)
        ip = input("Ip: ")
        port = input("Port: ")
    command = "ufw delete allow from {} to any port {}".format(ip, port)
    os.system(command)
    query = "DELETE FROM Portas WHERE ip=INET_ATON(%s) AND port=%s"
    cursor.execute(query, (ip, port))
    mydb.commit()


def search_port(cursor, mydb):
    port = input("Port: ")
    ip = input("Ip: ")
    query = "SELECT port, INET_NTOA(ip) as IP FROM Portas WHERE port=%s OR ip=INET_ATON(%s)"
    cursor.execute(query, (port, ip))
    reply = cursor.fetchall()
    for port, ip in reply:
        print(port, ip)
