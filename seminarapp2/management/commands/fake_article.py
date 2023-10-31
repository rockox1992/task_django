from django.core.management.base import BaseCommand
from seminarapp2.models import Author_2, Article


class Command(BaseCommand):
    help = "Generate fake authors and article."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for i in range(1, count + 1):
            author = Author_2(first_name=f'firstname{i}', last_name=f'lastname{i}', email=f'email{i}@mail.ru',
                              biography=f'biography{i}', dob=f'2000-11-23')
            author.save()
            for j in range(1, count + 1):
                article = Article(title=f'title{j}', description=f'description{j}', author_id=author,
                                  category=f'category{i}')
            article.save()
