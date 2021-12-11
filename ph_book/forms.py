from django import forms


class contact_form(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    second_name = forms.CharField(label='Second name', max_length=100)
