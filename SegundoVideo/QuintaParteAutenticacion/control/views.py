from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, LoginForm


@login_required(login_url='control:login')
def home(request):
    users = User.objects.order_by('username')
    context = {'users':users}
    return render(request, 'control/home.html', context)


def register(request):
    context = {'form' : CreateUserForm()}
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            context['mensaje'] = f'Usuario {request.POST["username"]} registrado correctamente, felicidades!!'
        else:
            context['mensaje'] = form.errors
            
    return render(request, 'control/register.html', context)


def login(request):
    context = {'form' : LoginForm()}

    if request.method == "POST":

        user = request.POST["username"]
        passwd = request.POST["password"]

        user = authenticate(request, username=user, password = passwd)

        if user is not None:
            auth_login(request, user)
            return redirect('control:home')
        else:
            context['mensaje'] = 'Usuario o contraseña incorrectos'
    
    return render(request, 'control/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('control:login')



# from django.contrib.auth.mixins import LoginRequiredMixin
# class Inicio(LoginRequiredMixin, TemplateView):
#     template_name='home_template.html'
