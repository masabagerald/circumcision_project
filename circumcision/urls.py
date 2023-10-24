from django.urls import path
from .views import index,list_clients,client_regsitration

urlpatterns = [
    path('', index, name='index'),
    path('list_clients/', list_clients, name='list_clients'),
    path('client_registrations/', client_regsitration, name='client_registrations')
]
