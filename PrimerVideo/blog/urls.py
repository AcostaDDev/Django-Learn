from django.urls import path

from .views import post_list, post_detail, create_post

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:pk>/', post_detail, name='post_detail'), 
    path('create-post/', create_post, name='create_post')
]