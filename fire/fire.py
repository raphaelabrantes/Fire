from fire.login import *
from fire.menus import *
from django.conf import settings

def start():
    with open(os.path.join(settings.BASE_DIR, 'configs'), 'r') as filename:
        lines = filename.readlines()

    args = {}
    for line in lines:
        if line.strip() == '[client]':
            continue
        args[line.split("=", 1)[0]] = line.split("=", 1)[1].strip()

    host = args["host"]
    user = args["user"]
    passwd = args["password"]
    db = args["database"]

    mydb, cursor = login(host, user, passwd, db)
    first_menu(cursor, mydb)