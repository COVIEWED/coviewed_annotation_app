from django import forms

CHOICES=[('Yes','Yes'),
         ('No','No'),
         ('Dont know', 'Dont know')]

class validate(forms.Form):
  related = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Is this claim related to COVID-19?")
  claim = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="Is this claim valid?")