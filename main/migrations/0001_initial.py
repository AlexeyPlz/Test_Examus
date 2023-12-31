# Generated by Django 3.2.19 on 2023-06-29 13:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата изменения')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Аллерген',
                'verbose_name_plural': 'Аллергены',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата изменения')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория блюд',
                'verbose_name_plural': 'Категории блюд',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата изменения')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('calories', models.IntegerField(verbose_name='Коллорийность')),
                ('image', models.ImageField(upload_to='dishes/', verbose_name='Изображение')),
                ('allergens', models.ManyToManyField(related_name='dishes', to='main.Allergen', verbose_name='Аллергены')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='main.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата изменения')),
                ('client', models.UUIDField(verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='OrderDish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата изменения')),
                ('count', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Количество порций должно быть больше одного.')], verbose_name='Количество')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.dish', verbose_name='Блюдо')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'Блюдо заказа',
                'verbose_name_plural': 'Блюда заказов',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='dishes',
            field=models.ManyToManyField(related_name='orders', through='main.OrderDish', to='main.Dish', verbose_name='Блюда'),
        ),
        migrations.AddConstraint(
            model_name='orderdish',
            constraint=models.UniqueConstraint(fields=('dish', 'order'), name='unique_order_dish'),
        ),
    ]
