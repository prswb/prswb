from django import forms
from websites.models import Website

class SuggestForm(forms.ModelForm):
    class Meta:
        model = Website
        exclude = ('submitter',)
