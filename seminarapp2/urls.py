from django.urls import path
from . import views

urlpatterns = [
    path('eagle/', views.eagle, name='eagle'),
    path('show_eagle/<int:n>/', views.show_eagle, name='show_eagle'),
    path('a/<int:author_id>', views.get_articles, name='a'),
    path('ab/<int:article_id>', views.da, name='ab'),
]
