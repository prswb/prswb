# coding: utf-8

import codecs
import markdown

from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect
from django.utils.translation import get_language, ugettext as _
from django.views.decorators.csrf import csrf_protect

from uxperiment.utils import send_message

from pages.forms import ContactForm
from utils import resolve_markdown_path


def dashboard(request):
    return render(request, 'dashboard.html')


@csrf_protect
def contact(request):
    """ Contact form
    Display and proceed contact form submission
    """
    form = ContactForm(request.POST or None)
    if form.is_valid():
        send_message('contact', form.cleaned_data)
        return redirect('confirm_contact')

    return render(request, 'pages/contact.html', {'form': form})


def confirm_contact(request):
    """ Contact form confirmation """
    return render(request, 'pages/confirm_contact.html')


def markdown_page(request, slug):
    """
    Computes markdown file path, converts its contents to html and renders it.
    Otherwise, if the file doesn't exist, the view returns a 404.
    """
    filename = resolve_markdown_path(slug, get_language())
    if not filename:
        raise Http404
    try:
        input_file = codecs.open(filename, mode="r", encoding="utf-8")
        content = input_file.readlines()
    except IOError:
        # TODO: Shouldn't we log these kinds of errors?
        messages.error(request, _(u"Unable to render page, sorry."))
    finally:
        input_file.close()
    return render(request, 'pages/markdown.html', {
        'html': markdown.markdown("\n".join(content[2:])),
        'title': content[0].replace("\n", ''),
    })
