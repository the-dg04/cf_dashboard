from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Friends(models.Model):
    friend_of=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    friend=models.CharField(max_length=200) #later realised, could have been a foreign key(User) as well

    