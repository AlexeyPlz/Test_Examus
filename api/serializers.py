from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import (ModelSerializer,
                                        PrimaryKeyRelatedField,
                                        ValidationError)

from main.models import Allergen, Category, Dish


class AllergenSerializer(ModelSerializer):
    class Meta:
        model = Allergen
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ReadDishSerializer(ModelSerializer):
    image = Base64ImageField()
    category = CategorySerializer(read_only=True)
    allergens = AllergenSerializer(read_only=True, many=True)

    class Meta:
        model = Dish
        fields = '__all__'
        read_only_fields = ('id', 'title', 'price', 'calories')


class CreateDishSerializer(ModelSerializer):
    image = Base64ImageField()
    category = PrimaryKeyRelatedField(queryset=Category.objects.all())
    allergens = PrimaryKeyRelatedField(queryset=Allergen.objects.all(), many=True)

    class Meta:
        model = Dish
        fields = '__all__'

    def validate(self, data):
        allergens_check = []
        allergens = self.initial_data.get('allergens')
        if not allergens:
            raise ValidationError({'allergens': 'Обязательное поле.'})
        for allergen in allergens:
            if allergen in allergens_check:
                raise ValidationError({'allergens': 'Нельзя добавлять два одинаковых аллергена.'})
            allergens_check.append(allergen)
        return data
