from django.urls import path
from .views import index,list_clients,client_regsitration,add_client,register,logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('list_clients/', list_clients, name='list_clients'),
    path('client_registrations/', client_regsitration, name='client_registrations'),
    path('add_client/', add_client, name='add_client'),
    path('register/', register, name='register'),

    #path('login/', auth_views.LoginView.as_view(), name='login'),
   # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', logout_view, name='logout'),
]
