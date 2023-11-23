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
  
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('mobile_money', 'Mobile Money'),
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
        ('others', 'others'),
    ]    

    payment_method = models.CharField(max_length=30,choices=PAYMENT_METHODS, blank=True)  # e.g., 'Credit Card', 'PayPal', 'Bank Transfer'
    transaction_id = models.CharField(max_length=100, blank=True)
    payment_decription = models.TextField(blank=True)
 
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class MedicalHistory(models.Model):
    HIV_STATUS_CHOICES = [
        ('negative', 'Negative'),
        ('positive', 'Positive'),
        ('inconclusive', 'Inconclusive'),
        ('known_positive', 'Known Positive'),
        ('unknown', 'Unknown'),
        # Add other options as necessary
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sexually_active = models.BooleanField(null=True, blank=True)
    hts_offered = models.BooleanField(null=True, blank=True)
    hiv_tested_last_four_weeks = models.BooleanField(null=True, blank=True)
    hiv_tested_during_appointment = models.BooleanField(default=False)
    hiv_test_result = models.CharField(max_length=15, choices=HIV_STATUS_CHOICES, null=True, blank=True)
    if_hiv_positive_under_care = models.BooleanField(null=True, blank=True)
    partner_hiv_status = models.CharField(max_length=15, choices=HIV_STATUS_CHOICES, null=True, blank=True)
    tetanus_vaccination_td1_date = models.DateField(null=True, blank=True)
    tetanus_vaccination_td2_date = models.DateField(null=True, blank=True)
    
    # C2: Medical History
    bleeding_disorder = models.BooleanField(null=True, blank=True)
    urethral_discharge = models.BooleanField(null=True, blank=True)
    pain_on_urination = models.BooleanField(null=True, blank=True)
    swelling_of_scrotum = models.BooleanField(null=True, blank=True)
    genital_ulcers = models.BooleanField(null=True, blank=True)
    penile_warts = models.BooleanField(null=True, blank=True)
    difficulty_in_retracting_foreskin = models.BooleanField(null=True, blank=True)
    erectile_dysfunction = models.BooleanField(null=True, blank=True)
    other_medical_history_specify = models.TextField(null=True, blank=True)
    
    # C3: Client Undergoing Treatment
    hypertension = models.BooleanField(null=True, blank=True)
    diabetes = models.BooleanField(null=True, blank=True)
    anaemia = models.BooleanField(null=True, blank=True)
    hiv_aids = models.BooleanField(null=True, blank=True)
    other_treatment_specify = models.TextField(null=True, blank=True)
    
    # C4: Allergies
    local_anesthetics_allergy = models.BooleanField(null=True, blank=True)
    antiseptics_allergy = models.BooleanField(default=False)
    food_allergy = models.BooleanField(default=False)
    drug_allergy = models.BooleanField(default=False)
    other_allergies_specify = models.TextField(null=True, blank=True)
    
    # C5: Physical Exam
    bp_systolic = models.IntegerField(null=True, blank=True)
    bp_diastolic = models.IntegerField(null=True, blank=True)
    pulse = models.IntegerField(null=True, blank=True)
    temperature = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    rr = models.IntegerField(null=True, blank=True)  # Respiratory rate
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    urethra_discharge = models.BooleanField(null=True, blank=True)
    adhesions = models.BooleanField(null=True, blank=True)
    anatomical_abnormalities = models.BooleanField(default=False)
    balanitis = models.BooleanField(default=False)
    genital_ulcer_disease = models.BooleanField(null=True, blank=True)
    genital_warts = models.BooleanField(null=True, blank=True)
    surgical_disorders = models.BooleanField(null=True, blank=True)
    other_sti_abnormality = models.BooleanField(null=True, blank=True)
    jiggers = models.BooleanField(null=True, blank=True)
    other_physical_exam_specify = models.TextField(null=True, blank=True)
    td_given_during_appointment = models.BooleanField(null=True, blank=True)
    client_consented = models.BooleanField(null=True,default=False)
    date_of_consent = models.DateField(null=True, blank=True)
    consent_form = models.FileField(null=True,upload_to= "concent_forms/")
    eligibility_after_examination = models.BooleanField(default=False)
   

    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name}'s Medical History"



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
    def __str__(self):
        return self.name
    
class Anesthesia(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name

class AdverseEvent(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
    


class CircumcisionProcedure(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='circumcision_procedure')
    
    # Section E: Circumcision Procedure
    date_of_circumcision = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True)   
    end_time =  models.TimeField(null=True)
    local_anesthesia = models.ForeignKey(Anesthesia, on_delete=models.CASCADE, null=True, blank=True)
    
    # local_anesthesia_lignocaine = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # local_anesthesia_bupivicaine = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    # emla_cream_used = models.BooleanField(default=False)    
    
    procedure_type = models.ForeignKey(ProcedureType, on_delete=models.CASCADE)
   
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
    post_operative_medication = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Circumcision Procedure for {self.client.first_name} {self.client.last_name}"
    


class VisitType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True) 

    def __str__(self):
        return self.name
    
# Enum choices for Severity of AE
SEVERITY_CHOICES = (
    (1, 'Mild'),
    (2, 'Moderate'),
    (3, 'Severe'),
)
    
class FollowUpVisit(models.Model):
   # circumcision_procedure = models.ForeignKey(CircumcisionProcedure, on_delete=models.CASCADE, related_name='follow_up_visits')
    Client = models.ForeignKey(Client, on_delete=models.CASCADE ,default=1)
    visit_type = models.ForeignKey(VisitType, on_delete=models.SET_NULL, null=True, blank=True)
    
    visit_date = models.DateField(null=True, blank=True)
    wound_status = models.CharField(max_length=20, choices=[('healing', 'Healing'), ('infected', 'Infected'), ('other', 'Other')], null=True, blank=True)
    
    presence_of_adverse_event = models.BooleanField(default=False)
   
    type_of_adverse_event = models.ManyToManyField(AdverseEvent,  null=True, blank=True)
    
    severity_of_adverse_event = models.CharField(max_length=10, choices=[('mild', 'Mild'), ('moderate', 'Moderate'), ('severe', 'Severe')], null=True, blank=True)
    treatment_given = models.TextField(null=True, blank=True)
    attending_health_worker = models.CharField(max_length=100)

    def __str__(self):
        return f"Follow Up Visit for {self.Client.first_name} {self.Client.last_name} - {self.visit_type.name}"
