from django.urls import path
from .views import index,list_clients,client_regsitration,add_client

urlpatterns = [
    path('', index, name='index'),
    path('list_clients/', list_clients, name='list_clients'),
    path('client_registrations/', client_regsitration, name='client_registrations'),
    path('add_client/', add_client, name='add_client'),
]
