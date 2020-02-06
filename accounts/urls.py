from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('',views.login, name='login'),
    path('register/',views.register, name='register'),
]