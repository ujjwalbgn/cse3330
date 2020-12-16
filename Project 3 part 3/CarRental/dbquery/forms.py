from .models import *
from django import forms
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class CustomerForms(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class VehicleForms(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

# class SearchRentalForm(forms.Form):
#
#     start_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
#     class meta:
#         widgets = {'start_date': DateInput}

class RentalForms(ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'
        exclude = ['vehicleid','startdate','orderdate','returned']
        widgets = {'returndate': DateInput}