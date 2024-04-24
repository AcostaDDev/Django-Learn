from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.views import generic

from .models import Book
from .forms import ContactForm, InsertBookForm

# Create your views here.


def buscar_libro(request):
    return render(request, 'loans/form_search.html')

def resultados(request):

    if request.GET['libro']:
        nombre_libros = request.GET['libro']
        libros = Book.objects.filter(title__contains=nombre_libros)
    else:
        libros = "No se encontro el libro"
    
    context = {
        'libros':libros
    }

    return render(request, 'loans/search.html', context)

def form_insert_book(request):
    return render(request, 'loans/form_insert_book.html')

def insert_book(request):
    if request.POST['titulo']:
        myYear = request.POST['year']
        Book.objects.create(
            title=request.POST['titulo'],
            author=request.POST['autor'],
            genre=request.POST['genero'],
            year=myYear if myYear.is_digit() else 1900,
            editorial=request.POST['editorial']
        )
        context = {
            'mensaje':'Libro insertado correctamente, felicidades!!'
        }
    else:
        context = {
            'mensaje':'No se pudo insertar el libro'
        }
    return render(request, 'loans/insert_book.html', context)

def contact(request):
    if request.method == 'POST':
        print(request.POST)
        cf = ContactForm(request.POST)
        print(cf)

        if cf.is_valid():
            data = cf.cleaned_data
            # cc_myself_mail = data["sender"] if data["cc_myself"] else ''
            # send_mail(
            #     data["subject"],
            #     data["message"],
            #     data["sender"],
            #     ["temporal.mail@d3mo.es", cc_myself_mail]          
            # )
            mensaje = "Su correo ha sido enviado correctamente"
        else:
            mensaje = "Ha ocurrido un error"
        return HttpResponse(mensaje)
    else:
        return render(request, 'loans/contact.html', {'formulario':ContactForm()})
    

def form_book(request):

    form = InsertBookForm()
    context = {
        'form':form
    }

    myForm = InsertBookForm(request.POST or None)

    if myForm.is_valid():
        myForm.save()
        context['mensaje'] = 'Libro insertado correctamente, felicidades!!'
    elif request.method == "POST":
        context['mensaje'] = f'No se pudo insertar el libro, error: {myForm.errors}'
    
    return render(request, 'loans/form_book.html', context)


def book_list(request):
    try:
        books = Book.objects.all()
    except Book.DoesNotExist:
        books = None

    context = {
        'books':books
    }  
    
    return render(request, 'loans/pruebas/book_list.html', context)

def book_detail(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        book = None

    context = {
        'book':book
    }  
    
    return render(request, 'loans/pruebas/book_detail.html', context)


class BookListView(generic.ListView):
    model = Book
    template_name = 'loans/pruebas/book_list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        context['title'] = 'Book ListView'

        return context
    
    
class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'loans/pruebas/book_detail.html'


class BookCreateView(generic.edit.CreateView):
    model = Book
    fields = '__all__'
    success_url = '/loans/booklistview'

class BookUpdateView(generic.edit.UpdateView):
    model = Book
    fields = '__all__'
    success_url = '/loans/booklistview'
    template_name = 'loans/book_update_form.html'

class BookDeleteView(generic.edit.DeleteView):
    model = Book
    success_url = '/loans/booklistview'