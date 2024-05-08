from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name='наименование')
    description = models.TextField(max_length=255, verbose_name='описание', **NULLABLE)

    def __str__(self):
       return f"Наименование категории: {self.name}, описание: {self.description}"


    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=120, verbose_name='наименование')
    description = models.TextField(max_length=255, verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='prod_image/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='категория', **NULLABLE)
    price = models.FloatField(verbose_name='цена за покупку')
    create_at = models.DateTimeField(verbose_name='дата создания')
    update_at = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f"Наименование продукта: {self.name}, категория продукта: {self.category}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)


