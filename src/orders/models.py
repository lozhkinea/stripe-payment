from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', max_length=2000)
    price = models.DecimalField(
        'Цена',
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0),
        ],
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
