from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.contrib import messages
from .models import URL
from .forms import URLForm

def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'signup.html', {'form': form})

from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def add_url(request):
    if URL.objects.filter(user=request.user).count() >= 5:
        messages.error(request, "You cannot add more than 5 URLs.")
        return redirect('list_urls')

    form = URLForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        messages.success(request, "URL added successfully.")
        return redirect('list_urls')

    return render(request, 'add_url.html', {'form': form})



@login_required
def list_urls(request):
    search = request.GET.get("search", "")
    urls = URL.objects.filter(user=request.user, title__icontains=search) | \
           URL.objects.filter(user=request.user, original__icontains=search)

    paginator = Paginator(urls, 5)
    urls = paginator.get_page(request.GET.get('page'))
    return render(request, 'list_urls.html', {'urls': urls, 'search': search})

@login_required
def edit_url(request, id):
    url = get_object_or_404(URL, id=id, user=request.user)
    form = URLForm(request.POST or None, instance=url)
    if form.is_valid():
        form.save()
        return redirect('list_urls')
    return render(request, 'edit_url.html', {'form': form})


@login_required
def delete_url(request, id):
    get_object_or_404(URL, id=id, user=request.user).delete()
    return redirect('list_urls')

def go(request, short):
    url = get_object_or_404(URL, short=short)
    return redirect(url.original)




def logout_user(request):
    logout(request)
    return render(request, "logout.html")
      
