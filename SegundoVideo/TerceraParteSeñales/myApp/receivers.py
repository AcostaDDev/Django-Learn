from django.dispatch import receiver
from django.core.signals import request_finished, request_started

@receiver([request_finished, request_started])
def mi_receptor(sender, **kwargs):
    print("Solicitud Inicializada")

@receiver(request_started)
def hola(sender, **kwargs):
    print("Hola mundo")