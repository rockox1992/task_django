# Generated by Django 4.2.5 on 2023-09-28 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seminarapp2', '0004_author_2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('category', models.CharField(max_length=100)),
                ('count_views', models.IntegerField(default=0)),
                ('is_published', models.BooleanField(default=False)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminarapp2.author_2')),
            ],
        ),
    ]
