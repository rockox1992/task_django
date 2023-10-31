from django.http import HttpResponse
import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    context = {
        'text': 'fewgsdgsdgsdgsdgsd'
    }
    return render(request, 'hwapp/index.html', context)


def about(request):
    return render(request, 'hwapp/about2.html')
