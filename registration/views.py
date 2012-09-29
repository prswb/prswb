# coding: utf-8
from registration.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def signin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('confirm_signin'))
    else:
        form = UserCreationForm()

    return render(request, 'registration/signin.html', {'form': form})

def confirm_signin(request):
    return render(request, 'registration/confirm_signin.html')
