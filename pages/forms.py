# coding: utf-8

from django import forms
from django.utils.translation import ugettext as _


class ContactForm(forms.Form):
    subject = forms.CharField(min_length=3, error_messages={
        'min_length': _('3 characters minimum required.'),
        'required': _('A subject is required.')
        }, widget=forms.TextInput(attrs={'placeholder': _('Subject') + '*'}))
    sender = forms.EmailField(error_messages={
        'invalid': _('A valid email address is required'),
        'required': _('An email is required.')
    }, widget=forms.TextInput(attrs={'placeholder': _('Email address' + '*')}))
    message = forms.CharField(min_length=8, error_messages={
        'min_length': _('8 characters minimum required.'),
        'required': _('A message is required.')
    }, widget=forms.Textarea(attrs={'placeholder': _('Message') + '*'}))
