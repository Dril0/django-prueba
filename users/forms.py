from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    """UserRegisterForm tendra todas las características y funcionalidades de UserCreationForm, le agregamos el campo email, ponemos los campos que mostraremos en el formulario en field, usando el model User de Django."""

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
