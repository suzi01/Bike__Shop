from django.db import models
from django.forms import ModelForm
from .models import BikeForm
from django import forms


class BikeModelForm(forms.Form):
    name = forms.CharField(label='your name:')
    surname = forms.CharField(label='your surname')
    phone_number = forms.CharField(label='your phone number')

    class Meta:
        model = BikeForm
        fields = ['name, surname, phone_number']
