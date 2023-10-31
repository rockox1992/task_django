from django.core.management.base import BaseCommand
from hw2app.models import Client


class Command(BaseCommand):
    help = "Delete clien by name."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='name')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        client = Client.objects.filter(name=name).first()
        if client is not None:
            client.delete()
        self.stdout.write(f'{Client}')
