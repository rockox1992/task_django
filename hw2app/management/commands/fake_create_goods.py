import random

from django.core.management.base import BaseCommand
from hw2app.models import Goods


class Command(BaseCommand):
    help = "Create fake Goods."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            goods = Goods(name_goods=f'{i}Goods', description=f'{i}bla bla{i}',
                          price=f'{random.randint(1, 9) + random.randint(0, 100)/100}',
                          quantity=f'{random.randint(1, 80)}')
            goods.save()
            self.stdout.write(f'{goods}')
