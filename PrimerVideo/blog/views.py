import json

from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published=True)
    dict = {'posts': posts}
    return render(request, 'blog/post/list.html', dict)

def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        dict = {'post': post}
    except Post.DoesNotExist:
        raise Http404("Publicacion no encontrada")
    return render(request, 'blog/post/detail.html', dict)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, "Post creado con éxito")
            return render(request, 'blog/post/createpost.html', {'new_post': post})
    else:
        form = PostForm()

    return render(request, 'blog/post/createpost.html', {'form': form})
