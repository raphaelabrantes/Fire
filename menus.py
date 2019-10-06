import os
from users import *
from portas import *


def first_menu(cursor, mydb):
    try:
        while True:
            os.system("clear")
            print("Menu/")
            mensagem = "Chose one option\n1 User Menu\n2 Port menu\nCtrl+c para sair\n"
            op = input(mensagem)
            if op == "1":
                os.system("clear")
                menu_users(cursor, mydb)

            elif op == "2":
                os.system("clear")
                menu_portas(cursor, mydb)

    except KeyboardInterrupt:
        cursor.close()
        mydb.close()
        exit()


def menu_users(cursor, mydb):
    switch = {
        "1": show_users,
        "2": search_user,
        "3": add_user,
        "4": remove_user_n,
        "5": remove_user_ip,
    }
    mensagem = "Choose one option\n1 Show all users\n2 Search User Ips\n3 Add User\n4 Remove User by name\n5 Remove " \
               "User by ip "
    while True:
        print("Menu/User/")
        op = input(mensagem)
        if not op:
            op = "7"
        if 6 > int(op) > 0:
            switch.get(op)(cursor, mydb)
        else:
            break


def menu_portas(cursor, mydb):
    switch = {
        "1": show_ports,
        "2": search_port,
        "3": add_port,
        "4": remove_ports,
        "5": remove_port_ip,
    }
    mensagem = "Escolha uma opção\n1Show all ports\n2 Show personalized search\n3 Add port\n4 Remove port by IP\n5 " \
               "Remove IPs by Port\n "
    while True:
        print("Menu/Ports")
        op = input(mensagem)
        if not op:
            op = "7"
        if 6 > int(op) > 0:
            switch.get(op)(cursor, mydb)
        else:
            break
