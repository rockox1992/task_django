from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Author3, Post3

def hello(request):
    return HttpResponse("Hello World from function!")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")


def year_post(request, year):
    text = ""
    ...  # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ...  # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")


def post_detail(request, year, month, slug):
    ...  # Формируем статьи за год и месяц по идентификатору.Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
            "content": "В процессе написания очередной программы задумался над тем, какой способ создания "
                       "списков в Pythonработает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})


def my_view(request):
    context = {"name": "John"}
    return render(request, "seminarapp3/index.html", context)


def author_posts(request, author_id):
    author = get_object_or_404(Author3, pk=author_id)
    posts = Post3.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'seminarapp3/author_posts.html', {'author': author, 'posts': posts})


def post_full(request, post_id):
    post = get_object_or_404(Post3, pk=post_id)
    return render(request, 'seminarapp3/post_full.html', {'post': post})
