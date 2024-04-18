import json

from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from django.contrib import messages

from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    dict = {'posts': posts}
    return render(request, 'blog/post/list.html', dict)

def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        dict = {'post': post}
    except Post.DoesNotExist:
        raise Http404("Publicacion no encontrada")
    return render(request, 'blog/post/detail.html', dict)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            messages.success(request, "Post creado con éxito")
    else:
        form = PostForm()

    dic = {'form': form}

    return render(request, 'blog/post/createpost.html', dic)
