from django.core.management.base import BaseCommand
from hw2app.models import Client


class Command(BaseCommand):
    help = "Create fake Client."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'{i}Name', mail=f'{i}fsase{i}@mail.re',
                            mobile_number=f'+3752{i}71{i}99{i}{i}', client_address=f'Большие кучугуры {i*1.13}')
            client.save()
            self.stdout.write(f'{client}')
