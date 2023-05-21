from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import etudiant
from django.contrib.auth.forms import PasswordChangeForm
class etudLoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class etudForm(forms.ModelForm):
    class Meta:
        model = etudiant
        fields = ['nom','datenaissence','photo','NiveauEtudiant','bio']



class MyChangeFormPassword(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Old password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm New password'}))
    class Meta:
        model = User 
        fields = ['old_password','new_password1','new_password2']