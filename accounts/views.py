from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('jobPost:job_post')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobPost:job_post')
    else:
        form = UserCreationForm()
    return render(request,'accounts/register.html', {'form':form})
