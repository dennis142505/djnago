from django.shortcuts import render
 
def greeting(request):
    return render(request, 'form.html') 
def result(request):
    name = request.GET.get('name')
    return render(request, 'resutl.html', {'name': name})    