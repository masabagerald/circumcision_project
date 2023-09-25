from django.db import models


# circumcision/models.py
class Client(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    next_of_kin_name = models.CharField(max_length=100)
    next_of_kin_contacts = models.CharField(max_length=15)

class CircumcisionMethod(models.Model):
    name = models.CharField(max_length=100)
    

class Surgery(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_of_circumcision = models.DateField()
    method_of_circumcision = models.ForeignKey(CircumcisionMethod, on_delete=models.CASCADE)

class AppointmentType(models.Model):
    name = models.CharField(max_length=100)

class Appointment(models.Model):
    date = models.DateField()
    appointment_type = models.ForeignKey(AppointmentType, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    medication = models.TextField(null=True, blank=True)
