from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # redirect to the list page
    else:
        form = BookForm()
    return render(request, 'pages/add_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'pages/book_list.html', {'books': books})
