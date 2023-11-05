from django.shortcuts import render,HttpResponse
from cf_comp.api_calls.api_func import status

def home(request):
    return render(request,"getStarted.html")

def userPage(request,username):
    return HttpResponse(f'hello : {username}')

# def getRatingsFromSubmissions()

def userSubmissions(request,username):
    sub = status(username)
    ratings=[]
    for i in sub:
        try:
            if(i['sub_status']=='OK'):
                ratings.append(i['problem']['rating'])
        except:
            continue
    ratings.sort()
    rating_dict=dict()
    for i in ratings:
        try:
            rating_dict[i]+=1
        except:
            rating_dict[i]=0
    print(rating_dict)
    data={
        'x':list(rating_dict.keys()),
        'y':list(rating_dict.values())
    }
    return render(request,"submissions.html",{'sub':sub[:10],'data':data})
