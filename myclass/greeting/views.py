from django.shortcuts import render

def greeting(request):
    # If the form was submitted via GET
    if 'username' in request.GET:
        username = request.GET.get('username', '')
        return render(request, 'result.html', {
            'username': username,
            'form_data': request.GET
        })
    # If no form data, show the form
    return render(request, 'form.html')
