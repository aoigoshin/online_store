from django.db import models
from datetime import *

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    alias = models.SlugField(verbose_name='Alias категории')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return 'Категория %s' % self.name


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    price = models.IntegerField(default=0, verbose_name='Цена')
    image = models.CharField(max_length=255, verbose_name='Ссылка на картинку')
    alias = models.SlugField(verbose_name='Alias товара')

    category = models.ForeignKey(Category)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return 'Товар %s' % self.name
    
class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя заказчика')
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')
    order = models.CharField(max_length=255, verbose_name='Заказ')
    summa = models.IntegerField(default=0, verbose_name='Сумма заказа')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return 'Заказ на %s' % self.summa

