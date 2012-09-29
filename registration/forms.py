from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
 
class UserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Pseudo'
        self.fields['password1'].label = 'Mot de passe'
        self.fields['password2'].label = 'Confirmation du mot de passe'

    email = forms.EmailField(required=True, label="Email")
 
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
 
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
