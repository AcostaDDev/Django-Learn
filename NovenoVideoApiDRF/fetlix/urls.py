from django.contrib import admin
from django.urls import path, include
# from rest_framework.documentation import include_docs_urls

from series.api.router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('docs/', include_docs_urls(title='Felix Docs', public=True)),
    path('', include('series.urls')),
    path('users/', include('users.urls')),
    path('api/', include(router.urls)),
]
