from django.contrib import admin

from .models import Loan, User, Book


admin.site.register(User)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'year', )
    search_fields=('title', 'author', 'year', 'publisher')
    list_filter=('genre',)

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display=('book_id', 'user_id', 'loan_date', 'due_date')
    search_fields=('user_id',)
    list_filter=('loan_date', 'due_date')
    date_hierarchy='due_date'


