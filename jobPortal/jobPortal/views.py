from django.http import HttpResponse
from django.shortcuts import render

def provider_profile(request):
    return render(request,'Provider_Homepage.html')