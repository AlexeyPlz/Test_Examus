from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import DishViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('dishes', DishViewSet, basename='dish')

urlpatterns = [
    path('v1/', include(router_v1.urls))
]
