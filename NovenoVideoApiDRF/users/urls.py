from django.urls import path
from .views import LoginView

app_name = "users"

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('register/', views.register_view, name='register'),
]
