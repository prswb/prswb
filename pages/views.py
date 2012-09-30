# coding: utf-8
import os.path
import codecs
import markdown
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_protect
from pages.forms import ContactForm
from django.conf import settings
from uxperiment.utils import send_message

def dashboard(request):
    return render(request, 'dashboard.html')

@csrf_protect
def contact(request):
    """ Contact form
    Display and proceed contact form submission
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message('contact', form.cleaned_data)
            return HttpResponseRedirect('confirm_contact')
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})

def confirm_contact(request):
    """ Contact form confirmation """
    return render(request, 'pages/confirm_contact.html')

def markdown_page(request, slug):
    """ Display markdown file for slug if exist """
    filename = os.path.join(settings.MARKDOWN_DIR, '%s.md' % slug)
    if os.path.isfile(filename):
        try:
            input_file = codecs.open(filename, mode="r", encoding="utf-8")
            text = input_file.read()
            html = markdown.markdown(text)
            return render(request, 'pages/markdown.html', {'html': html})
        except:
            pass
    raise Http404
