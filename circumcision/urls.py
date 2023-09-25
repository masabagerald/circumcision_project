from django.urls import path
from .views import index,list_clients

urlpatterns = [
    path('', index, name='index'),
     path('list_clients/', list_clients, name='list_clients'),
]
