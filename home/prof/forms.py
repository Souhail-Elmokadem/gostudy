from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from courses.models import course

class profLoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class courseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = ['titre','description','categorie','tag','level','cover','video','prix','duration']

