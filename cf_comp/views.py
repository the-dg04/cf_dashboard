from django.shortcuts import render,HttpResponse
from cf_comp.api_calls.api_func import status

def home(request):
    return render(request,"getStarted.html")

def userPage(request,username):
    return HttpResponse(f'hello : {username}')

def userSubmissions(request,username):
    sub = status(username)
    return render(request,"submissions.html",{'sub':sub})
