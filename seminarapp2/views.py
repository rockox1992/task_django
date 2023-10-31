import random
import logging

from django.http import HttpResponse

from .models import Coin
from django.shortcuts import render
from seminarapp2.models import Article, Author_2, Comment

logger = logging.getLogger(__name__)


def eagle(request):
    game_list = ['орел', 'решка']
    response = random.choice(game_list)
    coin = Coin(is_eagle=response)
    coin.save()
    logger.info(f'Сторона {coin}')
    return HttpResponse(coin)


def show_eagle(request, n):
    context = {Coin.counter(n)}
    return render(request, 'base.html', context)


def get_articles(request, author_id: int):
    #author = Author_2.objects.get(id=author_id)
    articles = Article.objects.filter(author_id=author_id)
    context = {
        'articles': articles
    }
    return render(request, 'base1.html', context)


def da(request, article_id: int):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article_id=article_id).order_by('-change_at')
    article.count_views += 1
    article.save()
    context = {
        'article': article,
        'comments': comments
    }
    return render(request, 'ab.html', context)
