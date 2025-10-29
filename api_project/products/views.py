from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def product_list(request):
    products = [
        {"name": "Laptop", "price": 55000, "category": "Electronics"},
        {"name": "Chair", "price": 1500, "category": "Furniture"},
        {"name": "Book", "price": 300, "category": "Stationery"},
        {"name": "Mobile Phone", "price": 20000, "category": "Electronics"},
    ]
    return Response(products)
