from django import forms
from .models import Client, MedicalHistory,ProcedureType,AdverseEvent,Anesthesia,FollowUpVisit,CircumcisionProcedure,Tribe,Religion    
from django.contrib.auth.models import User

class ClientForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255, label="First Name")
    last_name = forms.CharField(max_length=255, label="Last Name")
    nin = forms.CharField(max_length=255, label="National ID Number")
    age = forms.IntegerField(required=False, label="Age", min_value=0)

    education_level = forms.ChoiceField(choices=Client.EDUCATION_CHOICES, label="Education Level")
    tribe = forms.ModelChoiceField(queryset=Tribe.objects.all(), empty_label="Select Tribe", label="Tribe")
    religion = forms.ModelChoiceField(queryset=Religion.objects.all(), empty_label="Select Religion", label="Religion")

    marital_status = forms.ChoiceField(choices=Client.MARITAL_STATUS_CHOICES, label="Marital Status")
    district_of_residence = forms.CharField(max_length=255, required=False, label="District of Residence")
    sub_county = forms.CharField(max_length=255, label="Sub County")
    parish = forms.CharField(max_length=255, label="Parish")
    village = forms.CharField(max_length=255, label="Village")
    

    client_phone_number = forms.CharField(max_length=15, required=False, label="Client Phone Number")
    next_of_kin_name = forms.CharField(max_length=255, label="Next of Kin Name")
    next_of_kin_phone_number = forms.CharField(max_length=15, required=False, label="Next of Kin Phone Number")
    
    hiv_status_choices = forms.ChoiceField(choices=MedicalHistory.HIV_STATUS_CHOICES, required=False, label="HIV Status")

    payment_method = forms.ChoiceField(choices=Client.PAYMENT_METHODS, required=False, label="Payment Method")
    transaction_id = forms.CharField(max_length=100, required=False, label="Transaction ID")
    payment_decription = forms.CharField(widget=forms.Textarea, required=False, label="Payment Description")

    class Meta:
        model = Client
        fields = [
            'first_name', 'last_name', 'nin', 'age', 'education_level', 
            'tribe', 'religion', 'marital_status', 'district_of_residence', 
            'sub_county', 'parish', 'village', 'client_phone_number', 
            'next_of_kin_name', 'next_of_kin_phone_number', 'payment_method', 
            'transaction_id', 'payment_decription','hiv_status_choices'
        ]

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data


# forms.py

AE_TYPE_CHOICES = [
        ('excessive_skin_removal', 'Excessive skin removal'),
        ('damage_to_penis', 'Damage to penis'),
        ('excessive_bleeding', 'Excessive bleeding'),
        ('anesthetic_related', 'Anesthetic-related'),
        ('other', 'Other'),
    ]

SEVERITY_CHOICES = [
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ]

class CircumcisionProcedureForm(forms.ModelForm):
    class Meta:
        model = CircumcisionProcedure
      
        fields = [
             'date_of_circumcision',
             'start_time', 
             'end_time',
             'local_anesthesia',
             'procedure_type',
             'ring_size',
             'circumciser_name',
             'adverse_events_during_procedure',
              'type_of_adverse_event',        
             'severity_of_adverse_event',           
             
             'treatment_given',
             'blood_pressure',
            'pulse',
            'respiratory_rate',
            'post_operative_medication'
              
             ]
        
        widgets = {
            'date_of_circumcision': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'local_anesthesia': forms.Select(attrs={'class': 'form-control'}),
            'procedure_type': forms.Select(),
            'ring_size': forms.NumberInput(),
            'adverse_events_during_procedure': forms.CheckboxInput(),
            'type_of_adverse_event': forms.CheckboxSelectMultiple(),
            'severity_of_adverse_event': forms.RadioSelect(choices=SEVERITY_CHOICES),
            'treatment_given': forms.Textarea(attrs={'rows': 3}),
            'circumciser_name': forms.TextInput(),
            'blood_pressure': forms.TextInput(attrs={'placeholder': 'Blood Pressure', 'class': 'form-control'}),
            'pulse': forms.NumberInput(),
            'respiratory_rate': forms.NumberInput(),
            'post_operative_medication':forms.Textarea(attrs={'rows': 3}),
                    
        }

        """ date_of_circumcision = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
        start_time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}))
        end_time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}))
        local_anesthesia = forms.ModelChoiceField(
            required=False,
        # widget=forms.CheckboxSelectMultiple,
            queryset=Anesthesia.objects.all(),
            label="Local Anesthesia"
        )
        procedure_type = forms.ModelChoiceField(
            queryset=ProcedureType.objects.all(),
            label='Procedure Type',
            empty_label="Select Procedure Type"
        ) 
    # type_of_circumcision = forms.ChoiceField(choices=[('dorsal_slit', 'Dorsal slit'), ('forceps_guided', 'Forceps guided'), ('sleeve', 'Sleeve'), ('other', 'Other')])
        ring_size = forms.IntegerField(required=False, min_value=1, max_value=100)  # adjust the range as needed
        name_of_circumciser = forms.CharField(max_length=100)
        adverse_events = forms.BooleanField(required=False,label="Is there any Adverse Events?")
        
        # ... any other fields you need ...
        adverse_event_types = forms.ModelMultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            queryset=AdverseEvent.objects.all(),
            label="Type of Adverse Events"
        )
        severity = forms.ChoiceField(
            required=False,
            widget=forms.RadioSelect,
            choices=SEVERITY_CHOICES,
            label="Severity of Adverse Events "
        )
        treatment_given = forms.CharField(
            required=False,
            widget=forms.Textarea(attrs={'placeholder': 'Describe the treatment given, if any.'}),
            label="Treatment Given"
        )

        blood_pressure = forms.CharField(label='BP', max_length=10)
        pulse = forms.CharField(label='Pulse', max_length=10)
        respiratory_rate = forms.CharField(label='RR', max_length=10)
        post_operative_medication = forms.CharField(
            widget=forms.Textarea(attrs={'placeholder': 'List Post-Operative medication given'}),
            label='List Post-Operative Medication Given'
        ) """


    def clean(self):
        cleaned_data = super().clean()
        # add custom validation if needed
        return cleaned_data
    


class FollowUpVisitForm(forms.ModelForm):
    class Meta:
        model = FollowUpVisit
        
        fields = [
          
            'Client', 
            'visit_type', 
            'visit_date', 
            'wound_status', 
            'presence_of_adverse_event', 
            'type_of_adverse_event', 
            'severity_of_adverse_event', 
            'treatment_given', 
            'attending_health_worker',
        ]
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'wound_status': forms.Select(attrs={'class': 'form-control'}),
            'severity_of_adverse_event': forms.Select(attrs={'class': 'form-control'}),
            'treatment_given': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'attending_health_worker': forms.TextInput(attrs={'class': 'form-control'}),
            'type_of_adverse_event': forms.CheckboxSelectMultiple(),
        }
