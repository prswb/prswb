# coding: utf-8
from registration.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

def signin(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('confirm_signin')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signin.html', {'form': form})

def confirm_signin(request):
    return render(request, 'registration/confirm_signin.html')
