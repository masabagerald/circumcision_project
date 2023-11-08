from django.urls import path
from .views import index,list_clients,client_regsitration,add_client,register,logout_view,patient_dashbord,procedure_form
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('list_clients/', list_clients, name='list_clients'),
    path('client_registrations/', client_regsitration, name='client_registrations'),
    path('add_client/', add_client, name='add_client'),

    path('register/', register, name='register'),
    path('clients/<int:client_id>/dashboard/', patient_dashbord, name='client_dashboard'),

    path('<int:client_id>/procedure-form', procedure_form, name='procedure_form'),

    

    path('login/', auth_views.LoginView.as_view(), name='login'),
   # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', logout_view, name='logout'),
]
