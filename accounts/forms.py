from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'avatar', 'phone', 'country', 'password1', 'password2']

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")  # ✅ логинимся по email
