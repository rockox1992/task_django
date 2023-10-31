from django.contrib import admin
from .models import Client, Ordergds, Goods
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name']


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name_goods', 'price', 'quantity', 'img']


admin.site.register(Client, ClientAdmin)
admin.site.register(Ordergds)
admin.site.register(Goods, GoodsAdmin)
