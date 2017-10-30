from django.contrib import admin
from product.models import Category, Brand, Product


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'title', 'description', 'parent', 'img', 'slide', 'text', 'currency',
              'price', 'old_price', 'visible', 'hit', 'new', 'sale', 'date']
    list_filter = ['date']


class AttrAdmin(admin.ModelAdmin):
    fields = ['name']
    list_filter = ['date']


class OptionsAdmin(admin.ModelAdmin):
    fields = ['name']
    list_filter = ['product', 'attr', 'value']


admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
