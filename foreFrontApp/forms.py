from django import forms
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, PasswordInput, Select, FileInput, DateInput, DateField, ChoiceField, widgets
from foreFrontApp.models import *
from crispy_forms.helper import FormHelper


class ContactUsForm(forms.ModelForm):
    # class Meta:
    #     model = ContactUs
    #     fields = ['name', 'email', 'subject', 'message']

    # widgets = {
    #     'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'type': 'text'}),
    #     'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email', 'type': 'email'}),
    #     'subject': TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Subject'}),
    #     'zipCode': TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Message'})
    # }

    # def __init__(self, *args, **kwargs):
    #     super(ContactUsForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_show_labels = False

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Your Name', 'type': 'text', 'id': 'name', 'class': 'form-control'}),
        required=True
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Your Email', 'type': 'email', 'id': 'email', 'class': 'form-control'}),
        required=True,
    )
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Subject', 'type': 'text', 'id': 'subject', 'class': 'form-control'}),
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Message', 'type': 'textarea', 'id': 'message', 'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["name"].label = ""
        self.fields["email"].label = ""
        self.fields["subject"].label = ""
        self.fields["message"].label = ""


class subscribeForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Your Email Here', 'type': 'email', 'id': 'sub_email', 'class': 'form-control', 'name': 'sub_email'}),
        required=True,
    )

    class Meta:
        model = NewsTeller
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(subscribeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["email"].label = ""
