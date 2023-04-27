from rest_framework.serializers import ModelSerializer
from .models import Category
from .models import Product
from .models import Brand
from .models import Size
from .models import User

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'slug')

class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'name')

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'