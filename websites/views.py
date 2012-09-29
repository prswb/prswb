# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse
from django.core.mail import send_mass_mail
from django.conf import settings
from websites.forms import SuggestForm

@csrf_protect
def suggest(request):
    """ Suggest form
    Display and proceed suggest a website form submission
    """
    if request.method == 'POST':
        form = SuggestForm(request.POST)
        if form.is_valid():
            #send_message(form.cleaned_data)
            return HttpResponseRedirect(reverse('confirm_suggest_website'))
    else:
        form = SuggestForm()
    return render(request, 'websites/suggest.html', {'form': form})

def confirm_suggest(request):
    """ Suggest form confirmation """
    return render(request, 'websites/confirm_suggest.html')


#def send_message(data):
#
