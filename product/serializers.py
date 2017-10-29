from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Category, Brands, Product, Attr, Options


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'img', 'description', 'brands')


class BrandsSerializer(ModelSerializer):
    class Meta:
        model = Brands
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
    brands = BrandsSerializer()
    attr = AttrSerializer()
    options = OptionsSerializer()
    brand_name = serializers.CharField(source='brand.name')

    class Meta:
        model = Product
        fields = (
            'name', 'title', 'description', 'category', 'brands', 'parent', 'img', 'slide', 'text', 'currency', 'price',
            'old_price', 'hit', 'new', 'sale', 'date', 'attr', 'options', 'brand_name')
