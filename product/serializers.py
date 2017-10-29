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


class AttrSerializer:
    class Meta:
        model = Attr
        fields = ('name',)


class OptionsSerializer(ModelSerializer):
    class Meta:
        model = Options
        fields = ('value',)


class ProductSerializer(ModelSerializer):
    category = CategorySerializer
    brands = BrandsSerializer
    attr = AttrSerializer
    options = OptionsSerializer

    class Meta:
        fields = (
            'name', 'title', 'description', 'category', 'brands', 'parent', 'img', 'slide', 'text', 'currency', 'price',
            'old_price', 'visible', 'hit', 'new', 'sale', 'date')
