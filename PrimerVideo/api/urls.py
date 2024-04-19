from rest_framework import routers

from .views import PostViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register('posts', PostViewSet, basename='posts_api')

urlpatterns = router.urls