from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name='control'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    # path('login_view/', auth_views.LoginView.as_view(), name='login_view'),
    # path('change_password/', auth_views.PasswordChangeView.as_view(), name='change_password'),
    # path('change_password_template/', auth_views.PasswordChangeDoneView.as_view(), name='change_password_template'),
]