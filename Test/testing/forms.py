from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


#converting django models to a form

from django.contrib.auth.models import User

#using forms class
from django import forms
#to use widget (fields)
from django.forms.widgets import PasswordInput,TextInput

#modifying the Existing default UserCreation Form

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields =['username','email','password1','password2']


#modifying the existing User Authentication

class LoginForm(AuthenticationForm):

    username=forms.CharField(widget=TextInput())
    
    password=forms.CharField(widget=PasswordInput())

    