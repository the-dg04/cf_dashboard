from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Friend

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=200,required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name']  