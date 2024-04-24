from django.urls import path, include

from .views import hello, goodbye, imc, contact, Hello

app_name = 'test_app'

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('', hello, name='hello'),
    path('goodbye/', goodbye, name='goodbye'),
    path('hello-class/', Hello.as_view(), name='hello_class'),
    path('imc/<int:peso> <int:estatura>', imc, name="imc" ),
    path('contact/', contact, name="contact"),
]