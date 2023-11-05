from django.shortcuts import render,HttpResponse
from cf_comp.api_calls.api_func import status
def home(request):
    return render(request,"getStarted.html")

def submissions(request):
    username = 'ttirth1234518'
    sub = status(username)
    return render(request,"submissions.html",{'sub':sub})
    # return HttpResponse('hi')
