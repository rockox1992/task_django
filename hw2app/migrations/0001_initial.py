# Generated by Django 4.2.5 on 2023-10-12 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254)),
                ('mobile_number', models.IntegerField()),
                ('client_address', models.CharField(max_length=200)),
                ('registration_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_goods', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField()),
                ('img', models.ImageField(height_field=100, upload_to='media', width_field=100)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ordergds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('num_orders', models.IntegerField(default=0)),
                ('all_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('one_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_added_orders', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hw2app.client')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hw2app.goods')),
            ],
        ),
    ]
