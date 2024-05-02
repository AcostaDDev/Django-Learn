from django.urls import path

from .views import HelloWorld

app_name = "series"

urlpatterns = [
    path("", HelloWorld.as_view(), name="hello-world")
]