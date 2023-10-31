from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import ImageForm
from .models import Client, Ordergds, Goods
from datetime import datetime, timedelta


def order(request, client_id):
    client_orders = Ordergds.objects.filter(client_id=client_id)
    name = Client.objects.get(pk=client_id)
    return render(request, 'hw2app/orders.html', {'client_orders': client_orders,
                                                 'name': name, 'client_id': client_id})


def base(request, num_orders):
    orders = Ordergds.objects.filter(num_orders=num_orders)
    return render(request, 'hw2app/basket.html', {'orders': orders})


def weak(request, client_id, day):
    now = datetime.now()
    before = now - timedelta(days=day)
    client_orders = Ordergds.objects.filter(client_id=client_id, date_added__range=(before, now).all())
    return render(request, 'hw2app/wmy.html', {'data_ord': client_orders})


def month(request, client_id):
    now = datetime.now()
    client_orders = Ordergds.objects.filter(client_id=client_id, date_added__month__lte=now.month)
    return render(request, 'hw2app/wmy.html', {'data_ord': client_orders})


def year(request, client_id):
    now = datetime.now()
    client_orders = Ordergds.objects.filter(client_id=client_id, date_added__year__lte=now.year)
    return render(request, 'hw2app/wmy.html', {'data_ord': client_orders})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'hw2app/upload_image.html', {'form': form})
