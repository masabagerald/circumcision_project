from django import forms
from .models import Client
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
