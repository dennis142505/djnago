from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import VisitCount
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login 

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            VisitCount.objects.create(user=user)  # Create visit counter for user
            login(request, user)
            return redirect('counter')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def counter_view(request):
    visit = VisitCount.objects.get(user=request.user)
    visit.count += 1
    visit.save()
    return render(request, 'counter.html', {'count': visit.count})

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')





def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            # Redirect to home page after successful login
            return redirect('counter')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})