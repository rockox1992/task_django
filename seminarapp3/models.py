from django.db import models


class Author3(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post3(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author3, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'
