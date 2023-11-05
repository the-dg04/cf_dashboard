from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from cf_comp.forms import LoginForm
import requests

def isValid(username):
    response=requests.get(f"https://codeforces.com/api/user.info?handles={username}")
    resp=response.json()
    return resp['status']=='OK'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if(isValid(username)):
                messages.success(request, f'Account created for {username}!')
                form.save()
                response=redirect(f'/user/{username}')
                response.set_cookie('username',username)
                return response
            else:
                messages.error(request,'Bad request')
                return redirect('/register')
    else:
        form = UserCreationForm()
    return render(request,"register.html",{'form':form})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            try:
                m=User.objects.get(username=username)
                if m.check_password(password):
                    response=redirect(f'/user/{username}/submissions')
                    response.set_cookie('username',username)
                    return response
                else:
                    return redirect('/login')
            except:
                return redirect('/login')
    else:
        form=LoginForm()
        return render(request,"login.html",{'form':form})
