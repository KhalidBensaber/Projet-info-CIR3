from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    #email = forms.EmailField(required=True)
    #first_name = forms.CharField(max_length=30, required=True)
    #last_name = forms.CharField(max_length=30, required=True)
    #STATUS_CHOICES = [
    #    ('spectator', 'Spectator'),
    #    ('player', 'Player'),
    #    ('special-status', 'Special status'),
    #]
    #status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
