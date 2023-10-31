from django.urls import path
from .views import order, base, weak, month, year, upload_image

urlpatterns = [
    path('or/<int:client_id>/', order, name='orders'), # заказы пользователя
    path('bas/<int:num_orders>/', base, name='basket'), # список товаров в заказе
    path('w/<int:client_id>/<int:day>', weak, name='time'),
    path('m/<int:client_id>/', month, name='time'),
    path('y/<int:client_id>/', year, name='time'),
    path('upload/', upload_image, name='upload_image'),
]
