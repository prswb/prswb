# coding: utf-8
from registration.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

def signin(request):
    form = UserCreationForm()
    return render(request, 'registration/signin.html', {'form': form})
