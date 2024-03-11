from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register", views.registration, name="register"),
    path("login", views.log_in, name="login"),
    path("logout", views.log_out, name="logout"),
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="password-reset.html"), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="password-sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password-form.html"), name="password_reset_confirm"),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="password-complete.html"), name="password_reset_complete"),

]