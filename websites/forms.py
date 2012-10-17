from django import forms
from websites.models import Website


class SuggestForm(forms.ModelForm):
    """ Picture field is excluded on purpose, as Heroku provided an ephemeral
        filesystem.
    """
    class Meta:
        model = Website
        exclude = ('submitter','picture',)
