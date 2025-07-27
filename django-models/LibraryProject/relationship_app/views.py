from django.shortcuts import render

# Create your views here.

from django.views.generic.detail import DetailView
from .models import Book, Library
from .models import Library 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def list_books(request):
    books = Book.objects.all()  
    return render(request, 'relationship_app/list_books.html', {'books': books})  


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('login')  # Change to 'home' if you have a home page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

