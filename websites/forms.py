from django import forms

class SuggestForm(forms.Form):
    url = forms.CharField()

