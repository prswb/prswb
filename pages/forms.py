# coding: utf-8
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(
    min_length=3,error_messages={"min_length":"Ce champ est obligatoire. Un minimum de 3 caractères est requis.",
    "required":"Veuillez renseignez les champs obligatoires."},
     widget=forms.TextInput(attrs={"placeholder":"Sujet*"}))
    sender = forms.EmailField(
    error_messages={"invalid":"Veuillez saisir une adresse email valide.",
    "required":"Veuillez renseignez les champs obligatoires."},
    widget=forms.TextInput(attrs={"placeholder":"Adresse email*"}))
    message = forms.CharField(
    	min_length=8,
    	error_messages={"min_length":"Ce champ est obligatoire. Un minimum de 8 caractères est requis.",
    		"required":"Veuillez renseignez les champs obligatoires."},
    	widget=forms.Textarea(attrs={"placeholder":"Message*"}))
