from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *

app_name = 'base'

urlpatterns = [
    path('', TempView.as_view(), name="home"),

    # RUTAS PARA EL MANEJO DE SESIONES
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='base:login'), name="logout"),
    path('register/', TempView.as_view(), name="register"),
    # RUTAS PARA EL MANEJO DE TAREAS
    path('task/<int:pk>', TempView.as_view(), name="task"),
    path('task-create/', TempView.as_view(), name="task-create"),
    path('task-update/<int:pk>', TempView.as_view(), name="task-update"),
    path('task-delete/<int:pk>', TempView.as_view(), name="task-delete"),

    path('task-reorder/', TempView.as_view(), name="task-reorder"),
]