import json

from django.shortcuts import render
from django.views.generic import View, ListView

from main.models import Category, Dish, Order, OrderDish


class IndexViewSet(ListView):
    model = Dish
    template_name = 'main/index.html'
    context_object_name = 'dishes'

    def get_context_data(self, **kwargs):
        context = super(IndexViewSet, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class OrderViewSet(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'main/order.html',
            {
                'dishes': Dish.objects.filter(id__in=json.loads(request.COOKIES.get('order'))),
                'orders': Order.objects.filter(client=request.COOKIES.get('device'))
            }
        )

    def post(self, request, *args, **kwargs):
        order = json.loads(request.COOKIES.get('order'))
        client = request.COOKIES.get('device')
        if client is not None:
            order = Order.objects.create(client=client)
            for id, count in order.items():
                OrderDish.objects.create(
                    dish=Dish.objects.get(id=id),
                    order=order,
                    count=count
                )
        return self.get(request)
