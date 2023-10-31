from django.core.management.base import BaseCommand
from hw2app.models import Goods


class Command(BaseCommand):
    help = "Create Goods."

    def handle(self, *args, **kwargs):
        goods = Goods(name_goods=input("Введите название товара: "), description=input("Введите описание товара: "),
                      price=input("Введите цену товара: "),
                      quantity=input("Введите количество товара: "))
        goods.save()
        self.stdout.write(f'{goods}')