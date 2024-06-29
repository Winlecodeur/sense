from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profil

class SignUpForm (UserCreationForm):
    email = forms.EmailField(max_length=250, help_text='necessite un email valide')
    class Meta :
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfilForm(forms.ModelForm):
    class Meta :
        model = User 
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfilForm(forms.ModelForm):
    class Meta :
        model = Profil
        fields = ['image', 'sujet', 'bio']