from rest_framework.serializers import ModelSerializer
from .models import Category, Brand, Product, Comment
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name',]

class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name',]

class ProductSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['category', 'brand', 'user', 'name', 'price',]

class CommentSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['message', 'product', 'user']