from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','photo']

class UserRegister(UserCreationForm):
    username=forms.CharField(required=True)
    email=forms.EmailField(required=True,widget=forms.EmailInput())
    password=forms.CharField(required=True,widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')

# class Search(forms.Form):
#     searchbar=forms.CharField(required=True)