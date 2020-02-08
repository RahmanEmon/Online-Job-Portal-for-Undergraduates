from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('accounts/',include('accounts.urls')),
    path('jobpost',include('jobPost.urls')),
]

urlpatterns += staticfiles_urlpatterns()
