from django.urls import path

from .import views
#import the views
urlpatterns = [

     path('',views.homepage,name=""),

    #name parameter helps us to switch over when using links
     path('register',views.register,name="register"),

     path('my-login',views.my_login,name="my-login"),
     
     path('dashboard',views.dashboard,name="dashboard"),
    
]
