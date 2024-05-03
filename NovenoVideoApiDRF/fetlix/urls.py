from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('series.urls')),
    path('users/', include('users.urls')),
    path('api/', include('series.api.urls')),
]
