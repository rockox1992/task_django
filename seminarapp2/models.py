from django.db import models
from collections import Counter


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'Title is {self.title}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:7])}...'


class Coin(models.Model):
    is_eagle = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Lucky {self.is_eagle, self.create_at}'

    @staticmethod
    def counter(n):
        coins = Coin.objects.order_by('-create_at')[:n]
        # coins = Coin.objects.all()
        print(coins)
        coins_dict = {'орел': 0, 'решка': 0}
        for coin in coins:
            if coin.is_eagle == 'орел':
                coins_dict['орел'] += 1
            else:
                coins_dict['решка'] += 1
        return coins_dict
        # return Counter([str(coin) + '<br>' for coin in coins][-n:][::-1])


class Author_2(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.CharField(max_length=1000)
    dob = models.DateField()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    create_at = models.DateField(auto_now_add=True)
    author_id = models.ForeignKey(Author_2, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)


class Comment(models.Model):
    author_id = models.ForeignKey(Author_2, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    create_at = models.DateField(auto_now_add=True)
    change_at = models.DateField(auto_now_add=True)
