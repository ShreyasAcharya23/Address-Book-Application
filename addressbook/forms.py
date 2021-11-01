from django import forms
from django.forms import fields

from .models import Contact
# Imports the model and creates a form with their respective lists
class contactForm (forms.ModelForm):
    class Meta:
        model = Contact 
        fields = ('first_name','last_name','email','phone_number','address')