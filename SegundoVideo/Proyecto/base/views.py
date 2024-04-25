from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from . import forms

# Create your views here.


class TempView(TemplateView):
    template_name = "home.html"

class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    authentication_form = forms.CustomAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('base:home')
