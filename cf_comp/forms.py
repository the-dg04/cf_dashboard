from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Friends

class LoginForm(forms.Form):
    username=forms.CharField(max_length=200,required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friends
        fields = ['friend'] 

class SearchForm(forms.Form):
    username=forms.CharField()

class SearchTag(forms.Form):
    tag=forms.CharField()