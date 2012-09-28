from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(min_length=8)
    sender = forms.EmailField()
    message = forms.CharField(min_length=8,widget=forms.Textarea)
