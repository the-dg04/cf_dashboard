from django.urls import path,include
from . import views
from .user_auth import views as view1

urlpatterns=[
    path("",views.home),
    path("register/",view1.register),
    path("login/",view1.login),
    path('user/',views.userRedirect),
    path('user/<str:username>',views.userProfile),
    path('user/<str:username>/submissions',views.userSubmissions),
    path('logout/',views.logout),
    # path('friends/', views.add_friend, name='add_friend'),
    path('friends/all', views.view_friends),
]