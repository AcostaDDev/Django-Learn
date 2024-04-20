from django.urls import path, include

from .views import hello, goodbye, imc, Hello

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('goodbye/', goodbye, name='goodbye'),
    path('hello-class/', Hello.as_view(), name='hello_class'),
    path('imc/<int:peso> <int:estatura>', imc, name="imc" )
]