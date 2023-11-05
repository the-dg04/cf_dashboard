from django.shortcuts import render,HttpResponse,redirect
from cf_comp.api_calls.api_func import status
from .forms import FriendForm

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

def add_friend(request,username):
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('/friends/')  # Redirect to a page displaying friends
    else:
        form = FriendForm()
    return render(request, 'add_friend.html', {'form': form})
    # return HttpResponse('hello')
