from django.urls import path,include
from . import views
from .user_auth import views as view1

urlpatterns=[
    path("",views.home),
    path("register/",view1.register)
]