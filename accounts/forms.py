from django.forms import fields, widgets
from .models import *
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class ShopForm(forms.ModelForm):

    class Meta:
        model = ShopDetails
        # fields = '__all__'
        exclude = ['login']
        widgets = {
            'shopname':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
        }

class UserForm(forms.ModelForm):
    
    class Meta:
        model = UserLogin
        fields = ('first_name','last_name','address','phone','gender','dob','email','username','password','usertype')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'dob':DateInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'usertype': forms.TextInput(attrs={'class':'form-control','type':'hidden'})
        }
        help_texts = {'username':None}

    def clean(self):
        super(UserForm,self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        phone = self.cleaned_data.get('phone')
        if len(username)<5:
            self._errors['username'] = self.error_class(['minimum 5 characters required'])
        if len(password)<8:
            self._errors['password'] = self.error_class(['minimum 8 characters required'])
        if len(str(phone))<10:
            self._errors['phone'] = self.error_class(['enter a valid mobile no.'])

        for instance in UserLogin.objects.all():
            if instance.username == username:
                self._errors['username'] = self.error_class(['username already taken'])

        return self.cleaned_data


class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = UserLogin
        fields = ('first_name','last_name','address','phone','gender','dob','email','username')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'dob':DateInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
        help_texts = {'username':None}
    def clean(self):
        super(UserForm,self).clean()
        username = self.cleaned_data.get('username')
        phone = self.cleaned_data.get('phone')
        if len(username)<5:
            self._errors['username'] = self.error_class(['minimum 5 characters required'])
        if len(str(phone))<10:
            self._errors['phone'] = self.error_class(['enter a valid mobile no.'])
        return self.cleaned_data
