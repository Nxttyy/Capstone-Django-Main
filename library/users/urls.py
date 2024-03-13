from django.contrib import admin
from django.urls import path, include
from .views import register, login, log_out, account


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', log_out, name='logout'),
    path('account/', account, name='user-account'),



]