from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import authenticate
import getpass
from fire.fire import start

class Command(BaseCommand):
    help='start firecli'
    def handle(self, *args, **options):
        user = input("Login: ")
        password = getpass.getpass(prompt='Password: ', stream=None)
        if authenticate(request=None, username=user, password=password):
            self.stdout.write(self.style.SUCCESS("Login OK"))
            start(self)