from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

class Friend(models.Model):
    name = models.CharField(max_length=200)
    friends = models.ManyToManyField('self', symmetrical=False)
    def __str__(self):
        return self.name
    