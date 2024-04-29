from django.contrib import messages
from django.shortcuts import render

from django.views import View

from books.models import Book


class ListBookView(View):
    def get(self, request):
        messages.info(request, 'INFO')
        return render(request, 'list_book.html',
                      context={'books': Book.objects.all()})