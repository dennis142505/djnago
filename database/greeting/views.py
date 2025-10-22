

# Create your views here.
from django.http import HttpResponse
from .models import Customer
def greeting(request):
    cust = Customer()
    cust.email = 'user2@mashupstack.com'
    cust.password = 'hello123'
    cust.save()
    return HttpResponse('Db table row created')