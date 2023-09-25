from django.contrib import admin
from .models import Client, Surgery, AppointmentType, Appointment,CircumcisionMethod

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address', 'next_of_kin_name', 'next_of_kin_contacts')
    search_fields = ('name', 'phone_number', 'address', 'next_of_kin_name', 'next_of_kin_contacts')

# Register the Client model with the admin site
admin.site.register(Client, ClientAdmin)

#surgery admin
class SurgeryAdmin(admin.ModelAdmin):
    list_display = ('client', 'date_of_circumcision', 'method_of_circumcision')
    search_fields = ('client', 'date_of_circumcision', 'method_of_circumcision')

# Register the Client model with the admin site
admin.site.register(Surgery, SurgeryAdmin)

#surgery admin
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date', 'appointment_type', 'client', 'medication')
    search_fields = ('date', 'appointment_type', 'client', 'medication')

# Register the Client model with the admin site
admin.site.register(Appointment, AppointmentAdmin)
#surgery admin
class CircumcisionMethodAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register the Client model with the admin site
admin.site.register(CircumcisionMethod, CircumcisionMethodAdmin) 

#Appointment Type admin
class AppointmentTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register the Client model with the admin site
admin.site.register(AppointmentType, AppointmentTypeAdmin) 

