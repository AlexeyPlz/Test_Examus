from django.contrib import admin

from config.settings import EMPTY_ADMIN_VALUE

from main.models import Allergen, Category, Dish, Order, OrderDish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created',
        'updated'

    )
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = EMPTY_ADMIN_VALUE


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created',
        'updated'
    )
    search_fields = ('title',)
    list_filter = ('title',)
    empty_value_display = EMPTY_ADMIN_VALUE


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'price',
        'calories',
        'category',
        'created',
        'updated'
    )
    search_fields = ('title',)
    list_filter = ('title', 'price', 'calories', 'category')
    empty_value_display = EMPTY_ADMIN_VALUE


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'client',
        'created',
        'updated'
    )
    empty_value_display = EMPTY_ADMIN_VALUE


@admin.register(OrderDish)
class OrderDishAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'count',
        'dish',
        'order',
        'created',
        'updated'
    )
    list_filter = ('dish', 'order')
    empty_value_display = EMPTY_ADMIN_VALUE
