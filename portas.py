import mysql.connector
import os


def add_port(cursor, mydb):
    query = "INSERT INTO Portas(ip, port) VALUES(INET_ATON(%s), %s)"
    show_ports(cursor, mydb)
    ip = input("IP: ")
    port = input("Port: ")
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
    query_s = "SELECT INET_NTOA(ip) FROM Portas WHERE port=%s"
    query_d = "DELETE FROM Portas WHERE port=%s"
    show_ports(cursor, mydb)
    port = input("Port: ")
    string = "ufw delete allow from {} to any port {}"
    cursor.execute(query_s, (port,))
    select = cursor.fetchall()
    cursor.execute(query_d, (port,))
    mydb.commit()
    for ip in select:
        command = string.format(ip, port)
        reply = os.popen(command)
        print(list(reply)[0])


def remove_port_ip(cursor, mydb, query=None):
    query = "DELETE FROM Portas WHERE ip=INET_ATON(%s) AND port=%s"
    show_ports(cursor, mydb)
    ip = input("Ip: ")
    port = input("Port: ")
    command = "ufw delete allow from {} to any port {}".format(ip, port)
    reply = os.popen(command)
    print(reply[0])
    cursor.execute(query, (ip, port))
    mydb.commit()


def remove_total_ip(cursor, mydb, ip=None):
    show_ports(cursor, mydb)
    query_s = "SELECT port FROM Portas WHERE ip=INET_ATON(%s)"
    query_d = "DELETE FROM Portas WHERE ip=INET_ATON(%s)"
    if not ip:
        ip = input("Ip: ")
    string = "ufw delete allow from {} to any port {}"
    cursor.execute(query_s, (ip,))
    reply = cursor.fetchall()
    for port in reply:
        command = string.format(ip, port[0])
        reply = list(os.popen(command))
        print(reply)
    cursor.execute(query_d, (ip,))
    mydb.commit()


def search_port(cursor, mydb):
    query = "SELECT port, INET_NTOA(ip) as IP FROM Portas WHERE port=%s OR ip=INET_ATON(%s)"
    port = input("Port: ")
    ip = input("Ip: ")
    cursor.execute(query, (port, ip))
    reply = cursor.fetchall()
    for port, ip in reply:
        print(port, ip)
