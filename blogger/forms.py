from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from . import models

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
                        "class":"form-control form-control-sm",
                        "id":"username"}
                    ))
    email = forms.EmailField(widget=forms.TextInput(attrs={
                        "class":"form-control form-control-sm",
                        "id":"email"}
                    ))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
                        "class":"form-control form-control-sm",
                        "id":"password1"}
                    ))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                        "class":"form-control form-control-sm",
                        "id":"password2"}
                    ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
                        "class":"form-control form-control-sm",
                        "id":"username"}
                    ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                        "class":"form-control form-control-sm",
                        "id":"password"}
                    ))

class BlogModelForm(ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title', 'subtitle', 'content']

