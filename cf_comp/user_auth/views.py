from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from cf_comp.forms import UserRegisterForm
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
                return redirect('/')
                form.save()
            else:
                messages.warning(request,"Invalid CF handle")
                # return render(request,"register.html",{'form':form})
    else:
        form = UserCreationForm()
    return render(request,"register.html",{'form':form})