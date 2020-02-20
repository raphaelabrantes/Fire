from fire.portas import remove_total_ip


def add_user(cursor, mydb, obj):
    show_users(cursor, mydb, obj)
    query = "INSERT INTO Usuarios(name, ip, date_add) VALUES(%s, INET_ATON(%s), CURRENT_TIMESTAMP )"
    user = input("Name: ")
    ip = input("IP: ")
    cursor.execute(query, (user, ip))
    mydb.commit()
    obj.stdout.write(str(cursor.rowcount))


def show_users(cursor, mydb, obj):
    query = "SELECT name, INET_NTOA(ip), date_add FROM Usuarios"
    cursor.execute(query)
    reply = cursor.fetchall()
    for nome, ip, data in reply:
        obj.stdout.write("%s\t\t%s\t%s" % (nome, ip, data.strftime("%m/%d/%Y, %H:%M:%S")))


def remove_user_n(cursor, mydb, obj):
    show_users(cursor, mydb, obj)
    query_s = "SELECT INET_NTOA(ip) FROM Usuarios WHERE name=%s"
    query_d = "DELETE FROM Usuarios WHERE name=%s"
    user = input("Name: ")
    cursor.execute(query_s, (user, ))
    reply = cursor.fetchall()
    for ip in reply:
        obj.stdout.write(ip[0])
        remove_total_ip(cursor, mydb, obj, ip=ip[0])
    cursor.execute(query_d, (user,))
    mydb.commit()


def remove_user_ip(cursor, mydb, obj):
    query = "DELETE FROM Usuarios WHERE ip=INET_ATON(%s)"
    show_users(cursor, mydb, obj)
    ip = input("Ip: ")
    remove_total_ip(cursor, mydb, obj, ip=ip)
    cursor.execute(query, (ip,))
    mydb.commit()


def search_user(cursor, mydb, obj):
    query = "SELECT name, INET_NTOA(ip) as IP FROM Usuarios WHERE name=%s OR ip=INET_ATON(%s)"
    show_users(cursor, mydb, obj)
    name = input("Name: ")
    ip = input("Ip: ")
    cursor.execute(query, (name, ip))
    reply = cursor.fetchall()
    for name, ip in reply:
        st = name + " " +  ip
        obj.stdout.write(st)
