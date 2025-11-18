from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny as allowAny
from rest_framework.decorators import permission_classes    

# Add product / Show all products
@api_view(['GET', 'POST'])
@permission_classes([allowAny])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


# Update / Delete a product using ID
@api_view(['PUT', 'DELETE'])
@permission_classes([allowAny])
def product_detail(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        product.delete()
        return Response({"message": "Product deleted successfully"})
