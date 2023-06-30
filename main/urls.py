from django.urls import path

from main.views import IndexViewSet, OrderViewSet

app_name = 'main'

urlpatterns = [
    path('', IndexViewSet.as_view(), name='index'),
    path('order/', OrderViewSet.as_view(), name='order')
]
