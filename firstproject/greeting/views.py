from django.shortcuts import render
# from django.http import HttpResponse    
# Create your views here.
# def greeting(request):
#     return HttpResponse("Hello, Django!")   
def greeting(request):
    # count=23
    # return render(request, 'index.html', {'count': count} )
    # students = ['dennis', 'alice', 'bob', 'charlie']
    # return render(request, 'index.html', {'students': students} )
    # my_object = {
    #     'name': 'dennis',
    #     'age': 30,
    #     'city': 'New York' }
    # return render(request, 'index.html', {'my_object': my_object} )
    # my_object = [
    #     { 'name': 'dennis','age': 30,'city': 'New York'},
    #     { 'name': 'alice','age': 25,'city': 'Los Angeles'},
    #     { 'name': 'bob','age': 28,'city': 'Chicago'},
    #     { 'name': 'charlie','age': 22,'city': 'Houston'}
    #     ]
    # context = { 'my_object': my_object }
    # return render(request, 'index.html', context )
    if request.method == 'POST':
       email = request.POST.get('email')
       password = request.POST.get('password')
       return render(request,'form-data.html', {
          'formData': request.POST,
          'email': email
        })
    return render(request, 'index.html')