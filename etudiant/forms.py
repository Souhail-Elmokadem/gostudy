from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import etudiant
class etudLoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class etudForm(forms.ModelForm):
    class Meta:
        model = etudiant
        fields = ['nom','datenaissence','photo','NiveauEtudiant','bio']

