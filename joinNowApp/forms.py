from django import forms
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, PasswordInput, Select, FileInput, DateInput, DateField, ChoiceField, widgets
from django.forms.fields import EmailField
from joinNowApp.models import *
import re 
from crispy_forms.helper import FormHelper



class joinUsForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name','type':'text','id':'name','class': 'form-control'}),
        required=True
    )
    email=forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Email Address','type':'email','id':'email','class': 'form-control'}),
        required=True,
    )
    
    
    # widgets = {
    #         'phone': NumberInput(attrs={'class': 'form-control', 'placeholder': 'enter a phone number(016xxxxx)','type':'tel'}),
    #         'CV': FileInput(attrs={'class': 'form-control','type':'file'}),
    #     }
    
    phone=forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': 'Email Address','type':'tel','id':'phone','class': 'form-control'}),
        required=True,
    )
    
    CV=forms.FileField(
        widget=forms.FileInput(attrs={'placeholder': 'CV Attachment','file':'email','id':'CV','class': 'form-control'}),
        required=True,
    )
    class Meta:
        model=joinNow
        fields=['name','email','phone','CV']

    def __init__(self, *args, **kwargs):
        super(joinUsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["name"].label = ""
        self.fields["email"].label = ""
        self.fields["phone"].label = ""
        self.fields["CV"].label = ""


