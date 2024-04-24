from django.urls import path

from . import views


app_name = 'loans'

urlpatterns = [
    path('search/', views.buscar_libro, name='search'),
    path('search_result/', views.resultados, name='search_result'),
    path("form_insert_book/", views.form_insert_book, name="form_insert_book"),
    path('insert_book/', views.insert_book, name='insert_book'),
    path('contact/', views.contact, name='contact'),
    path('form_book/', views.form_book, name='form_book'),
    path('book_list/', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    # path('book_list/', views.book_list, name='book_list'),
    # path('book/<int:pk>/', views.book_detail, name='book_detail'),

    path('booklistview/', views.BookListView.as_view(), name='book_list_view'),
    path('bookdetailview/<int:pk>/', views.BookDetailView.as_view(), name='book_detail_view'),

    path('bookcreateview/', views.BookCreateView.as_view(), name='book_create_view'),
    path('bookupdateview/<int:pk>/', views.BookUpdateView.as_view(), name='book_update_view'),
    path('bookdeleteview/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete_view'),
]