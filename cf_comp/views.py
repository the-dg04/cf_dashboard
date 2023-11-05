from django.shortcuts import render,HttpResponse,redirect,redirect
from cf_comp.api_calls.api_func import status
from .forms import FriendForm,SearchForm
from .models import Friends,User

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
def logout(request):
    response=redirect('/')
    response.delete_cookie('username')
    return response

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
    return render(request,"submissions.html",{'sub':sub[:10],'data':data,'isLoggedIn':getLoginStatus(request)})

def add_friend(request,username):
            try:
                isValidUser=User.objects.get(username=username)
                friendObject=Friends(friend=username,friend_of=User.objects.get(username=isLoggedIn(request)))
                friendObject.save()
                return redirect(f'/user/{username}')
            except:
                return redirect(f'/user/{username}')

def view_friends(request):
    username=isLoggedIn(request)
    if(not username):
        return redirect('/login')
    friendsObject=Friends.objects.filter(friend_of=User.objects.get(username=isLoggedIn(request)))
    return render(request,'viewFriends.html',{'friendsList':friendsObject})

def is_friend(request,friend_username):
    username=isLoggedIn(request)
    if(not username):
        return redirect('/login')
    try:
        friendObj=Friends.objects.get(friend=friend_username,friend_of=User.objects.get(username=isLoggedIn(request)))
        return True
    except:
        return False

def userProfile(request,username):
    if request.method == 'POST':
        add_friend(request,username)
    return render(request,'userProfile.html',{'username':username,"isNotFriend":not is_friend(request,username),'isLoggedIn':getLoginStatus(request)})

