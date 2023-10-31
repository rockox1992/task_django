from django.core.management.base import BaseCommand
from hw2app.models import Client


class Command(BaseCommand):
    help = "Create Client."
    
    def handle(self, *args, **kwargs):
        client = Client(name=input("Введите имя: "), mail=input("Введите email: "),
                      mobile_number=input("Введите номер: "), client_address=input("Введите адресс: "))
        client.save()
        self.stdout.write(f'{client}')
