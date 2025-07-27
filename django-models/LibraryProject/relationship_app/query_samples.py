import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query: All books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

# Query: List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library.name}: {[book.title for book in books_in_library]}")

# Query: Retrieve the librarian for a library
librarian = library.librarian
print(f"Librarian at {library.name}: {librarian.name}")
