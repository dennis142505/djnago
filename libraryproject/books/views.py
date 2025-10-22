from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_books')  # redirect after saving
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def view_books(request):
    books = Book.objects.all()
    return render(request, 'view_books.html', {'books': books})
