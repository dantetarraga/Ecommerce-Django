from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category
from .models import Brand
from .models import Product
from .models import Size
from .models import Product
from .serializers import CategorySerializer
from .serializers import ProductSerializer
from .serializers import SizeSerializer
from .serializers import BrandSerializer
from .serializers import ProductSerializer

# Create your views here

class CategoryAPIView(APIView):
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'data': serializer.data, 'success': True, 'message': 'Category created successfully.'}
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {'data': serializer.data, 'success': False, 'message': 'Error Create.'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def put(self, request, category_id):
        category = Category.objects.get(pk=category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            image = request.FILES.get('image')
            if image:
                category.image = image
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, category_id):
        category = Category.objects.get(pk=category_id)
        category.delete()
        response = {
            'message': 'Category with id {category_id} was successfully deleted'.format(category_id=category_id),
            'deleted_category': CategorySerializer(category).data
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)


class BrandAPIView(APIView):
    def get(self, request, format=None):
        Brands = Brand.objects.all()
        serializer = BrandSerializer(Brands, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, brand_id):
        brand = Brand.objects.get(pk=brand_id)
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, brand_id):
        brand = Brand.objects.get(pk=brand_id)
        brand.delete()
        response = {
            'message': 'Brand with id {brand_id} was successfully deleted'.format(brand_id=brand_id),
            'deleted_category': BrandSerializer(brand).data
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)


class SizeAPIView(APIView):
    def get(self, request, format=None):
        sizes = Size.objects.all()
        serializer = SizeSerializer(sizes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, size_id):
        size = Size.objects.get(pk=size_id)
        serializer = CategorySerializer(size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, size_id):
        size = Size.objects.get(pk=size_id)
        size.delete()
        response = {
            'message': 'Size with id {size_id} was successfully deleted'.format(size_id=size_id),
            'deleted_category': SizeSerializer(size).data
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)

class ProductAPIView(APIView):
    def get(self, request, format=None):
        products = Size.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, product_id):
        product = Product.objects.get(pk=product_id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, product_id):
        size = Product.objects.get(pk=product_id)
        size.delete()
        response = {
            'message': 'Size with id {product_id} was successfully deleted'.format(product_id=product_id),
            'deleted_category': ProductSerializer(size).data
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)

class ProductByCategoryAPIView(APIView):
    def get(self, request, category_id, format=None):
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category does not exist'}, status=status.HTTP_404_NOT_FOUND)

        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)



