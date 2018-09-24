from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm

from . import models

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
