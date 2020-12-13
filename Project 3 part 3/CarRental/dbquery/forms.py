from .models import *
from django import forms
from django.forms import ModelForm

class CustomerForms(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

# class RateForms(ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'