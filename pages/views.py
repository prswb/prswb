from django.shortcuts import render_to_response
from pages.forms import ContactForm

def contact(request):
    form = ContactForm()
    return render_to_response('pages/contact.html', {form: form})
