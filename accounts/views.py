from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def login(request):
    return render(request,'accounts/login.html')

def register(request):
    form = UserCreationForm()
    return render(request,'accounts/register.html', {'form':form})
