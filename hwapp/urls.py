from django.urls import path
from .views import index, about

urlpatterns = [
    path('', index, name='main'),  # по пустой строке у нас вызывется фу-ция index
    path('about/', about, name='about'),  # по строке about после адреса сервера вызывается функция about
]
