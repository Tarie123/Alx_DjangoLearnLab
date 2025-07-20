from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Fields to filter by (sidebar filters)
    list_filter = ('publication_year', 'author')
    
    # Fields searchable in the search box
    search_fields = ('title', 'author')
