from django import forms

class main_form(forms.Form):
    number = forms.CharField(label='main_label', max_length=10)