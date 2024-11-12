from django.contrib import admin
from apps.books.models import Books

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'pages', 'created_at', 'is_active']
    list_filter = ['author', 'created_at', 'is_active']
    search_fields = ['title', 'author']
    list_editable = ['is_active']

