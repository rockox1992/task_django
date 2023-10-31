"""
URL configuration for Django_GB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('Django_GB.urls')),
    path('hw2/', include('hw2app.urls')),
    path('admin/', admin.site.urls),
    path('hw/', include('hwapp.urls')), # по пути hw/ строки мы подключаем наше приложение hwapp
    path('sem/', include('seminarapp2.urls')),
    path('sem3/', include('seminarapp3.urls')),
    path('sem4/', include('myapp4.urls')),
    # path('__debug__/', include("debug_toolbar.urls")),
    path('les6/', include('myapp6.urls')),
]
