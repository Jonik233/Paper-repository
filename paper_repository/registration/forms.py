from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser
from django import forms


class RegistrationForm (UserCreationForm):
    full_name = forms.CharField(max_length=150)
    institution = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'institution', 'password1', 'password2')