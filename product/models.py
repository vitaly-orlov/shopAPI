from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(_('name'), max_length=250)
    img = models.ImageField(_('photo'), upload_to='category', blank=True, default='noimage.jpg')
    description = models.TextField(_('description'), blank=True, default='')
    brands = models.SmallIntegerField(_('brands'))

    class Meta:
        db_table = 'category'
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name


class Brands(models.Model):
    name = models.CharField(_('name'), max_length=250)
    img = models.ImageField(_('photo'), upload_to='brands', blank=True, default='noimage.jpg')
    country = models.CharField(_('country'), max_length=250)
    description = models.TextField(_('description'), blank=True, default='')

    class Meta:
        db_table = 'brands'
        verbose_name = _('brand')
        verbose_name_plural = _('brands')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=250)
    title = models.CharField('Title', max_length=250, blank=True, default='')
    description = models.TextField('Description', blank=True, default='')
    category = models.IntegerField(_('Category'))
    brand = models.IntegerField(_('Brand'))
    parent = models.IntegerField(_('Base product'), blank=True, default=0)
    img = models.ImageField(_('Preview'), upload_to='clothes/thamb', blank=True, default='noimage.jpg')
    slide = models.ImageField(_('Slides'), upload_to='clothes/slide', blank=True, default='noimage.jpg')
    text = models.TextField(_('Text'), blank=True, default='')
    currency = models.CharField(_('Carrence'), max_length=10)
    price = models.FloatField(_('Price'))
    old_price = models.FloatField(_('Old price'), blank=True, default=0)
    visible = models.SmallIntegerField(_('Viseble'), blank=True, default=1)
    hit = models.SmallIntegerField(_('Hit'), blank=True, default=0)
    new = models.SmallIntegerField(_('New'), blank=True, default=0)
    sale = models.SmallIntegerField(_('Sale'), blank=True, default=0)
    date = models.DateField(_('Date'), auto_now_add=True)

    class Meta:
        db_table = 'product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class Attr(models.Model):
    name = models.CharField(_('Name'), max_length=250)

    class Meta:
        db_table = 'attr'
        verbose_name = _('Atribute')
        verbose_name_plural = _('Atributes')


class Options(models.Model):
    product = models.IntegerField(_('Product'), blank=True, default=0)
    attr = models.IntegerField(_('Atribute'), blank=True, default=0)
    value = models.CharField(_('Value'), max_length=250)

    class Meta:
        db_table = 'options'
        verbose_name = _('Option')
        verbose_name_plural = _('Options')
