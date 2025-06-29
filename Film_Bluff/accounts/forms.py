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
            'title', 'genre',
            'actor1', 'actor2', 'actor3', 'actor4',
            'poster_url', 'release_year',
        ]
        widgets = {
            'genre': forms.Select(),  # renders a <select> with your GENRE_CHOICES
            'title': forms.TextInput(attrs={'placeholder': 'Film title'}),
            'actor1': forms.TextInput(attrs={'placeholder': 'Actor/Actress 1'}),
            # … rest unchanged …
        }