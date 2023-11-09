from django import forms
from .models import Client,ProcedureType,AdverseEvent,Anesthesia
from django.contrib.auth.models import User

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

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



class CircumcisionProcedureForm(forms.Form):
    date_of_circumcision = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    start_time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}))
    local_anesthesia = forms.ModelMultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
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
    adverse_events = forms.BooleanField(required=False)
    adverse_event_details = forms.CharField(widget=forms.Textarea, required=False)
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
        label="Severity"
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
    )


    def clean(self):
        cleaned_data = super().clean()
        # add custom validation if needed
        return cleaned_data
