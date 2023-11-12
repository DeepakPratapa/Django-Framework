from django.shortcuts import render

from django.http import HttpResponse



# Create your views here.

#request is  is an HttpRequest object that contains information about the current request
def homepage(request):

    return HttpResponse("This is the Homepage")
   #allow us to have a view of the homepage



def register(request):

    pass


def my_login(request):

    pass


def dashboard(request):

    pass