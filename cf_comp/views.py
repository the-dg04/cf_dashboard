from django.shortcuts import render,HttpResponse,redirect
from cf_comp.api_calls.api_func import status

def isLoggedIn(request):
    try:
        username=request.COOKIES['username']
        return username
    except:
        return False

def getLoginStatus(request):
    loginStatus=False
    if(isLoggedIn(request)):
        loginStatus=True
    return loginStatus

def home(request):
    return render(request,"getStarted.html",{'isLoggedIn':getLoginStatus(request)})

def userPage(request,username):
    return HttpResponse(f'hello : {username}')

# def getRatingsFromSubmissions()
def userRedirect(request):
    usernameOrNull=isLoggedIn(request)
    if(usernameOrNull):
        return redirect(f'/user/{usernameOrNull}/submissions')
    else:
        return redirect('/login')

def userSubmissions(request,username):
    if(not isLoggedIn(request)):
       return redirect('/login')
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

def logout(request):
    response=redirect('/')
    response.delete_cookie('username')
    return response

