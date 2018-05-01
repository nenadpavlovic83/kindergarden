# from django.urls import path
# from . import views
# from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
# from django.views.generic import TemplateView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/',
        auth_views.LoginView.as_view(template_name='accounts/login.html'),
        name='login'),
    path('logout/',
        auth_views.LogoutView.as_view(),
        name='logout'),
    path('signup/',
            views.sign_up,
            name='signup'),
    path('profile/',
            views.user_profile,
            name='profile'),
    path('edit/',
            views.edit_profile,
            name='editprofile'),
    path('change_password/',
            views.change_password,
            name='change_password'),
    # path('reset_pass/', auth_views.password_reset, name = 'password_reset'),
    # path('reset_pass_done/', auth_views.password_reset_done, name = 'password_reset_done'),
    # path('reset_pass_confirm/', auth_views.password_reset_confirm, name = 'password_reset_confirm')

    path('password_reset/',
            auth_views.PasswordResetView.as_view(), name = 'password_reset'),
    path('password_reset_done/',
            auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('password_reset_confirm/(?P<uid64>[0-9A-Za-z]+)-(?P<token>.+)/',
            auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('passchangedone/',auth_views.PasswordChangeDoneView.as_view(), name = 'password_reset_complete' )
    # path('password_reset_confirm/(?P<uid64>[0-9A-Za-z]+)-(?P<token>.+)/',
    #         auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm')
    # # path(
    #     'changepass/',
    #     auth_views.PasswordChangeView.as_view(template_name='accounts/changepass.html'),
    # ),

    # path("signup/", views.signup, name='signup'),#register
]
