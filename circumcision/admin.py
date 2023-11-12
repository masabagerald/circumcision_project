from django.contrib import admin
from .models import Client, Surgery, AppointmentType, Appointment,CircumcisionMethod,MedicalHistory,CircumcisionProcedure,FollowUpVisit,Tribe,Religion,ProcedureType,Anesthesia,AdverseEvent,VisitType

# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'client_phone_number', 'district_of_residence', 'nin', 'age','marital_status', 'next_of_kin_name', 'next_of_kin_phone_number')
    search_fields = ('first_name', 'last_name', 'client_phone_number', 'district_of_residence', 'nin', 'age','marital_status', 'next_of_kin_name', 'next_of_kin_phone_number')
    

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

class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('client','knows_hiv_status', 'tested_hiv_last_four_weeks', 'in_hiv_care_or_referred', 'has_allergies')
    search_fields = ('client','knows_hiv_status', 'tested_hiv_last_four_weeks', 'in_hiv_care_or_referred', 'has_allergies')

admin.site.register(MedicalHistory, MedicalHistoryAdmin)


class ProcedureTypeAdmin(admin.ModelAdmin):
    list_display = ('name','details')
    search_fields = ('name','details')
admin.site.register(ProcedureType, ProcedureTypeAdmin)


class CircumcisionProcedureAdmin(admin.ModelAdmin):
    list_display = ('client', 'date_of_circumcision', 'procedure_type')
    search_fields = ('client', 'date_of_circumcision', 'procedure_type')

admin.site.register(CircumcisionProcedure, CircumcisionProcedureAdmin)


class FollowUpVisitAdmin(admin.ModelAdmin):
    list_display = ('Client', 'visit_type', 'visit_date', 'wound_status',  'display_type_of_adverse_event', 'severity_of_adverse_event', 'treatment_given')
    search_fields = ('Client','visit_type', 'visit_date', 'wound_status',  'display_type_of_adverse_event', 'severity_of_adverse_event', 'treatment_given')

    def display_type_of_adverse_event(self, obj):
        return ", ".join([str(item) for item in obj.type_of_adverse_event.all()])
    display_type_of_adverse_event.short_description = 'Type of Adverse Event'

admin.site.register(FollowUpVisit, FollowUpVisitAdmin)


class TribeAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)

admin.site.register(Tribe,TribeAdmin)

class ReligionAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)

admin.site.register(Religion,ReligionAdmin)

class AnesthesiaAdmin(admin.ModelAdmin):
    list_display = ('name','details' )
    search_fields = ('name','details')

admin.site.register(Anesthesia,AnesthesiaAdmin)

class AdverseEventAdmin(admin.ModelAdmin):
    list_display = ('name','details' )
    search_fields = ('name','details')

admin.site.register(AdverseEvent,AdverseEventAdmin)

class VisitTypeAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    search_fields = ('name','description')

admin.site.register(VisitType,VisitTypeAdmin)