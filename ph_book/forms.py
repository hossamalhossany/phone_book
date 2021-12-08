from django import forms


class contact_form(forms.Form):
    first_name = forms.CharField(max_length=100)
    second_name = forms.CharField(max_length=100)
