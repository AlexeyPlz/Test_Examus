from rest_framework import viewsets

from api.pagination import CustomPagination
from api.permissions import TokenAccessPermission
from api.serializers import CreateDishSerializer, ReadDishSerializer
from main.models import Dish


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    permission_classes = [TokenAccessPermission]
    pagination_class = CustomPagination

    def get_serializer_class(self):
        return CreateDishSerializer if self.action in ('create',) else ReadDishSerializer
