from django.urls import path

from mainapp.views import index, contacts, about, product, products

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
    path('about/', about),
    path('product/', product),
    path('products/', products)
]
