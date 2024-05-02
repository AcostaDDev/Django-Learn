from django.contrib import admin
from django.urls import path, include

from series.views import HelloWorld

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('series.urls')),
]
