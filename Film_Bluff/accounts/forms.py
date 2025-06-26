# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Film

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class':'', 'placeholder':'Enter your email'}
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = [
            'title',
            'actor1', 'actor2', 'actor3', 'actor4',
            'poster_url',
            'release_year',
        ]
        widgets = {
            'title':      forms.TextInput(attrs={'placeholder': 'Film title'}),
            'actor1':     forms.TextInput(attrs={'placeholder': 'Actor/Actress 1'}),
            'actor2':     forms.TextInput(attrs={'placeholder': 'Actor/Actress 2'}),
            'actor3':     forms.TextInput(attrs={'placeholder': 'Actor/Actress 3'}),
            'actor4':     forms.TextInput(attrs={'placeholder': 'Actor/Actress 4'}),
            'poster_url': forms.URLInput(attrs={'placeholder': 'Poster image URL'}),
            'release_year': forms.NumberInput(attrs={'placeholder': 'e.g. 2025'}),
        }

