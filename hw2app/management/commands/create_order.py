from django.core.management.base import BaseCommand
from hw2app.models import Ordergds, Client, Goods
from unicodedata import decimal


class Command(BaseCommand):
    help = "Create Ordergds."

    def handle(self, *args, **kwargs):

        id_client = int(input('Введите id клиента: '))
        id_goods = int(input('Введите id товара: '))
        price_gds = (Goods.objects.get(id=id_goods)).price
        # print(price_gds)
        order = Ordergds(client=Client.objects.get(id=id_client),
                         goods=Goods.objects.get(id=id_goods),
                         all_price=price_gds)
        order.save()

        self.stdout.write(f'{order}')

