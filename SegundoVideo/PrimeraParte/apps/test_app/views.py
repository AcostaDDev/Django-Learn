from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def hello(request):
    context = {'saludo':'Hola de nuevo Mundo', 'frameworks':['Python', 'Django', 'Flask']}
    return render(request, 'test_app/index.html', context)

def goodbye(request):
    return HttpResponse("Adiós mundo cruel")

def imc(request, peso, estatura):
    imc = peso / (estatura/100)**2
    datos = [peso, estatura/100, round(imc,2)]
    context = {
        'nombre':'David',
        'datos':datos
    }
    return render(request, 'test_app/imc.html', context)

def contact(request):
    context = {'title' : 'Contacto'}
    return render(request, 'test_app/contact.html', context)

class Hello(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hola mundo")
    
    