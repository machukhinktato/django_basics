from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    decription = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return self.name