from django.shortcuts import render_to_response

def contact(request):
    render_to_response('pages/contact.html')
