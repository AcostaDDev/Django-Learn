from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.views import View

from .models import Book
from .forms import BookForm


class ListBookView(View):
    def get(self, request):
        return render(request, 'list_book.html', context={'books': Book.objects.all().order_by('-created_at')})

class CreateBookView(View):
    def get(self, request):
        return render(request, 'create_book.html', context={'form': formset_factory(BookForm, extra=2)})
    def post(self, request):
        if request.method == 'POST':
            formset = formset_factory(BookForm)(data=request.POST)
            if formset.is_valid():
                for form in formset:
                    cd = form.cleaned_data
                    Book.objects.create(
                        title=cd['title'],
                        author_id=cd['author'],
                        rating=cd['rating']
                    )
                return redirect('list-book')
            else:
                return render(request, 'create_book.html', context={'form': formset})
