from django import forms


class UserForm(forms.Form):
    name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)
