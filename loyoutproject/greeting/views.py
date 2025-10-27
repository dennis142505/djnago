from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Book
from .forms import BookForm

def index(request):
    book_list = Book.objects.all().order_by('-id')  # newest first
    paginator = Paginator(book_list, 5)  # 5 per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'greeting/index.html', {'page_obj': page_obj})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect('home')  # go back to homepage
    else:
        form = BookForm()
    return render(request, 'greeting/book_form.html', {'form': form, 'action': 'Add'})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'greeting/book_form.html', {'form': form, 'action': 'Edit'})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'greeting/confirm_delete.html', {'book': book})
