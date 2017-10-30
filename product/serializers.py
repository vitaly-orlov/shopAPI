from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Category, Brand, Product, Attr, Options


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'img', 'description')


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ('name', 'img', 'country', 'description')


class AttrSerializer(ModelSerializer):
    class Meta:
        model = Attr
        fields = ('name',)


class OptionsSerializer(ModelSerializer):
    class Meta:
        model = Options
        fields = ('value',)


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    # attr = AttrSerializer()
    # options = OptionsSerializer()
    brand_name = serializers.CharField(source='brand.name')

    class Meta:
        model = Product
        fields = (
            'name', 'title', 'description', 'parent', 'img', 'slide', 'text', 'currency', 'price',
            'old_price', 'hit', 'new', 'sale', 'created_date', 'brand_name', 'category', 'brand',)
