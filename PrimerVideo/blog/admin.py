from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'body', 'published']
    list_filter = ['published']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}      # --> En este campo se rellena automaticamente el slug basándose en el title