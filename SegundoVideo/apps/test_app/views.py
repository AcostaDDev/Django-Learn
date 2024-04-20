from django.http import HttpResponse
from django.views import View

def hello(request):
    return HttpResponse("Hola mundo")

def goodbye(request):
    return HttpResponse("Adiós mundo cruel")

def imc(requestm, peso, estatura):
    imc = peso / (estatura/100)**2
    return HttpResponse(f"""
                            El peso es: {peso}
                            Tu estatura es: {estatura/100} metros
                            Tu IMC es: {imc}
                        """)

class Hello(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hola mundo")