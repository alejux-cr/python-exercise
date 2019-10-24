from django import forms

class IntegersListForm(forms.Form):
    integersList = forms.CharField(label='Please enter a comma separated list of integers', max_length=250)