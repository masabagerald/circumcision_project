from django.db import models



# circumcision/models.py


class Tribe(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Religion(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Client(models.Model):
     # Client Information
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nin = models.CharField(max_length=255, verbose_name='National ID Number')
    age = models.PositiveIntegerField(null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
   

    
    EDUCATION_CHOICES = [
        ('none', 'None'),
        ('pre_primary', 'Pre-primary'),
        ('primary', 'Primary'),
        ('o_level', 'O-level'),
        ('a_level', 'A-level'),
        # ... add more as necessary
    ]
    education_level = models.CharField(max_length=50, choices=EDUCATION_CHOICES, default='none')
    tribe = models.ForeignKey(Tribe, on_delete=models.CASCADE)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    
    MARITAL_STATUS_CHOICES = [
        ('never_married', 'Never Married'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    ]
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS_CHOICES)
    
    district_of_residence = models.CharField(max_length=255,null=True, blank=True)
    sub_county = models.CharField(max_length=255)
    parish = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    
    client_phone_number = models.CharField(max_length=15,null=True, blank=True)
    next_of_kin_name = models.CharField(max_length=255)
    next_of_kin_phone_number = models.CharField(max_length=15,null=True, blank=True)
 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

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


class ProcedureType(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField(null=True, blank=True)

class AdverseEvent(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField(null=True, blank=True)


class MedicalHistory(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='medical_history')
    
    # Section C: Client Medical History
    knows_hiv_status = models.BooleanField(default=False)
    tested_hiv_last_four_weeks = models.BooleanField(default=False)
    tested_hiv_this_appointment = models.BooleanField(default=False)
    hiv_status = models.CharField(max_length=20, null=True, blank=True)  # Positive, Negative, Inconclusive, Unknown
    in_hiv_care_or_referred = models.BooleanField(default=False)
    partner_hiv_status = models.CharField(max_length=20, null=True, blank=True)
    
    # Vaccination Dates
    date_of_td1 = models.DateField(null=True, blank=True)
    date_of_td2 = models.DateField(null=True, blank=True)
    
    # Medical History Details
    bleeding_disorder = models.BooleanField(default=False)
    genital_ulcers = models.BooleanField(default=False)
    urethral_discharge = models.BooleanField(default=False)
    penile_warts = models.BooleanField(default=False)
    swelling_of_scrotum = models.BooleanField(default=False)
    
    # Undergoing Treatment
    hypertension = models.BooleanField(default=False)
    anaemia = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    hiv_aids = models.BooleanField(default=False)
    other_conditions = models.TextField(null=True, blank=True)  # In case there are other conditions that are not listed
    
    # Allergies
    has_allergies = models.BooleanField(default=False)
    allergies_description = models.TextField(null=True, blank=True)  # Details about allergies if any
    
    # Physical Exam
    blood_pressure = models.CharField(max_length=20, null=True, blank=True)
    pulse = models.PositiveIntegerField(null=True, blank=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    respiratory_rate = models.PositiveIntegerField(null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    urethra_discharge = models.BooleanField(default=False)
    adhesions = models.BooleanField(default=False)
    genital_ulcer_disease = models.BooleanField(default=False)
    genital_warts = models.BooleanField(default=False)
    surgical_disorders = models.BooleanField(default=False)
    other_sti_or_abnormality = models.BooleanField(default=False)
    open_wounds_or_recently_healed_scars = models.BooleanField(default=False)
    jiggers = models.BooleanField(default=False)
    other_physical_exam_conditions = models.TextField(null=True, blank=True)  # Any other condition detected in the physical exam

    def __str__(self):
        return f"Medical History for {self.client.first_name} {self.client.last_name}"

class CircumcisionProcedure(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='circumcision_procedure')
    
    # Section E: Circumcision Procedure
    date_of_circumcision = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True)   
    end_time =  models.TimeField(null=True)
    
    local_anesthesia_lignocaine = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    local_anesthesia_bupivicaine = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    emla_cream_used = models.BooleanField(default=False)    
    
    procedure_type = models.ForeignKey(ProcedureType, on_delete=models.CASCADE)
    other_procedure_type = models.CharField(max_length=255, null=True, blank=True)  # if procedure_type is 'other'
    ring_size = models.CharField(max_length=255, null=True, blank=True)
    circumciser_name = models.CharField(max_length=255, null=True, blank=True)
    circumciser_cadre = models.CharField(max_length=255, null=True, blank=True)
    adverse_events_during_procedure = models.BooleanField(default=False)    
    
    type_of_adverse_event = models.ManyToManyField(AdverseEvent,  null=True, blank=True)
    severity_of_adverse_event = models.CharField(max_length=10, choices=[('moderate', 'Moderate'), ('severe', 'Severe')], null=True, blank=True)
    treatment_given = models.TextField(null=True, blank=True)
    blood_pressure = models.CharField(max_length=20, null=True, blank=True)
    pulse = models.PositiveIntegerField(null=True, blank=True)
    respiratory_rate = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"Circumcision Procedure for {self.client.first_name} {self.client.last_name}"
    


class VisitType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class FollowUpVisit(models.Model):
    circumcision_procedure = models.ForeignKey(CircumcisionProcedure, on_delete=models.CASCADE, related_name='follow_up_visits')
    visit_type = models.ForeignKey(VisitType, on_delete=models.SET_NULL, null=True, blank=True)
    
    follow_up_dates = models.DateField(null=True, blank=True)
    wound_status = models.CharField(max_length=20, choices=[('healing', 'Healing'), ('infected', 'Infected'), ('other', 'Other')], null=True, blank=True)
    
    presence_of_adverse_event = models.BooleanField(default=False)
   
    type_of_adverse_event = models.ManyToManyField(AdverseEvent,  null=True, blank=True)
    
    severity_of_adverse_event = models.CharField(max_length=10, choices=[('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')], null=True, blank=True)
    treatment_given = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Follow Up Visit for {self.circumcision_procedure.client.first_name} {self.circumcision_procedure.client.last_name} - {self.visit_type.name}"
