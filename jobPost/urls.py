from . import views
from django.urls import path
from django.conf.urls import url

app_name = 'jobPost'

urlpatterns = [
    path('',views.job_post, name='job_post'),
]