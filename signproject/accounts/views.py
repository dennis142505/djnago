from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .models import VisitCount

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
