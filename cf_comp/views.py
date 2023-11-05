from django.shortcuts import render,HttpResponse
def home(request):
    return render(request,"getStarted.html")

def userPage(request,username):
    return HttpResponse(f'hello : {username}')

def userSubmissions(request,username):
    return HttpResponse(f'submissions {username}')