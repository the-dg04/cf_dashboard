from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,"getStarted.html")
