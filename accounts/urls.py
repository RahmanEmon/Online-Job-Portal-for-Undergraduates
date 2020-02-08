from . import views
from django.urls import path
from django.conf.urls import url

app_name = 'accounts'

urlpatterns = [
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
]