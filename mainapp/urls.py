from django.urls import path

from mainapp.views import index, contacts

urlpatterns = [
    path('', index),
    path('contacts/', contacts),
]
