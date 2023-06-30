from django.core import validators
from django.db import models

from core.models import Base


class Category(Base):
    title = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name='Название')

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория блюд'
        verbose_name_plural = 'Категории блюд'

    def __str__(self):
        return self.title


class Allergen(Base):
    title = models.CharField(max_length=50, unique=True, null=False, blank=False, verbose_name='Название')

    class Meta:
        ordering = ['title']
        verbose_name = 'Аллерген'
        verbose_name_plural = 'Аллергены'

    def __str__(self):
        return self.title


class Dish(Base):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Название')
    price = models.IntegerField(null=False, blank=False, verbose_name='Цена')
    calories = models.IntegerField(null=False, blank=False, verbose_name='Коллорийность')
    image = models.ImageField(upload_to='dishes/', null=False, blank=False, verbose_name='Изображение')
    allergens = models.ManyToManyField(Allergen, related_name='dishes', verbose_name='Аллергены')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='dishes',
        verbose_name='Категория'
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return f'{self.title} - {self.price} рублей - {self.category}'


class Order(Base):
    client = models.UUIDField(null=False, blank=False, verbose_name="Клиент")
    dishes = models.ManyToManyField(Dish, through='OrderDish', related_name='orders', verbose_name='Блюда')

    class Meta:
        ordering = ['id']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.client}'


class OrderDish(Base):
    count = models.IntegerField(
        default=1,
        null=False,
        blank=False,
        verbose_name='Количество',
        validators=(
            validators.MinValueValidator(
                1,
                message='Количество порций должно быть больше одного.'
            ),
        )
    )
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Блюдо'
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='Заказ'
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Блюдо заказа'
        verbose_name_plural = 'Блюда заказов'
        constraints = [
            models.UniqueConstraint(
                fields=('dish', 'order'),
                name='unique_order_dish'
            )
        ]

    def __str__(self):
        return f'{self.dish} - {self.order}'
