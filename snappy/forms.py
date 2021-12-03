from django import forms
from django.forms import ModelForm
from .models import Driver



class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
