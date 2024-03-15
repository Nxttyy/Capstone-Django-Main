from django.contrib import admin
from django.urls import path, include
from .views import register, login, log_out, account, edit_account


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', log_out, name='logout'),
    path('account/', account, name='user-account'),
    path('book/edit_account/', edit_account, name='account-edit'),

    # path('borrow/<book_id>', borrow, name='borrow-book'),



]