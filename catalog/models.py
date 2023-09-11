from django.db import models

# Create your models here.

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    picture = models.ImageField(upload_to='products/', verbose_name='изображение', **NULLABLE)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    date_create = models.DateTimeField(verbose_name='дата создания', auto_now=True)
    date_change = models.DateTimeField(verbose_name='дата последнего изменения', auto_now_add=True)

    def __str__(self):
        return f'{self.name}  {self.price} {self.category_id}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('price',)


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
