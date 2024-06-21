# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('', home_view, name='home'),
]
