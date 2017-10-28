from django.db import models


class Category(models.Model):
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField('Название категории', max_length=250)
    img = models.ImageField('Фото', upload_to='category', blank=True, default='noimage.jpg')
    description = models.TextField('Описание', blank=True, default='')
    brands = models.SmallIntegerField('Бренды')

    def __str__(self):
        return self.name


class Brands(models.Model):
    class Meta:
        db_table = 'brands'
        verbose_name = 'Брэнд'
        verbose_name_plural = 'Брэнды'

    name = models.CharField('Имя', max_length=250)
    img = models.ImageField('Фото', upload_to='brands', blank=True, default='noimage.jpg')
    country = models.CharField('Страна', max_length=250)
    description = models.TextField('Описание', blank=True, default='')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    name = models.CharField('Название', max_length=250)
    title = models.CharField('Title', max_length=250, blank=True, default='')
    description = models.TextField('Description', blank=True, default='')
    category = models.IntegerField('Категория')
    brand = models.IntegerField('Бренд')
    parent = models.IntegerField('Основной товар', blank=True, default=0)
    img = models.ImageField('Превью', upload_to='clothes/thamb', blank=True, default='noimage.jpg')
    slide = models.ImageField('Слайды', upload_to='clothes/slide', blank=True, default='noimage.jpg')
    text = models.TextField('Текст', blank=True, default='')
    currency = models.CharField('Валюта', max_length=10)
    price = models.FloatField('Цена')
    old_price = models.FloatField('Старая цена', blank=True, default=0)
    visible = models.SmallIntegerField('Видимость на сайте', blank=True, default=1)
    hit = models.SmallIntegerField('Хит продаж', blank=True, default=0)
    new = models.SmallIntegerField('Новинка', blank=True, default=0)
    sale = models.SmallIntegerField('Распродажа', blank=True, default=0)
    date = models.DateField('Дата добавления', auto_now_add=True)

    def __str__(self):
        return self.name


class Attr(models.Model):
    class Meta:
        db_table = 'attr'
        verbose_name = 'Атрибут'
        verbose_name_plural = 'Атрибуты'

    name = models.CharField('Имя', max_length=250)



class Options(models.Model):
    class Meta:
        db_table = 'options'
        verbose_name = 'Опция'
        verbose_name_plural = 'Опции'

    product = models.IntegerField('Товар', blank=True, default=0)
    attr = models.IntegerField('Атрибут', blank=True, default=0)
    value = models.CharField('Значение', max_length=250)
