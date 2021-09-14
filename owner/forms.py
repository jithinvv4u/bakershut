from django import forms
from django.forms import fields,widgets
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class StaffForm(forms.ModelForm):
    
    class Meta:
        model = StaffDetails
        exclude = ['login']
        widgets = {
            'designation': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.NumberInput(attrs={'class':'form-control'}),
            'incentives': forms.NumberInput(attrs={'class':'form-control'}),
        }

class ProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        # fields = '__all__'
        exclude = ['status']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'cost': forms.NumberInput(attrs={'class':'form-control'}),
            'stock': forms.NumberInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'mfg': DateInput(attrs={'class':'form-control'}),
            'status':forms.TextInput(attrs={'type':'hidden'}),
        }

