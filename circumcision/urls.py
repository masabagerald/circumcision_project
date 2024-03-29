from django.urls import path
from .views import edit_client, edit_medical_history, index,list_clients,client_regsitration,add_client,register,logout_view,patient_dashbord,procedure_form,visit_form,follow_up_visit_detail,edit_follow_up_visit,procedure_details,procedure_edit
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='index'),
    path('list_clients/', list_clients, name='list_clients'),
    path('client_registrations/', client_regsitration, name='client_registrations'),
    path('add_client/', add_client, name='add_client'),

    path('register/', register, name='register'),
    path('clients/<int:client_id>/dashboard/', patient_dashbord, name='patient_dashbord'),

    path('<int:client_id>/procedure-form', procedure_form, name='procedure_form'),

    path('<int:client_id>/visit_form', visit_form, name='visit_form'),
    path('follow-up-visit/<int:visit_id>/', follow_up_visit_detail, name='follow_up_visit_detail'),
    path('follow-up-visit/<int:visit_id>/edit/', edit_follow_up_visit, name='edit_follow_up_visit'),

     path('procedure/<int:procedure_id>/details/', procedure_details, name='procedure_details'),

    path('procedures/<int:procedure_id>/edit/',procedure_edit, name='procedure_edit'),
    path('client/edit/<int:client_id>/', edit_client, name='edit_client'),

    path('client/<int:client_id>/edit-medical-history/', edit_medical_history, name='edit_medical_history'),


    

    path('login/', auth_views.LoginView.as_view(), name='login'),
   # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', logout_view, name='logout'),
]
