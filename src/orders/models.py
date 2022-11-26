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


class Order(models.Model):
    # description = models.TextField('Описание', max_length=2000, blank=True, null=True)
    items = models.ManyToManyField(
        Item, through='OrderItem', verbose_name='Товары'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self._meta.verbose_name} {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name='Заказ',
        on_delete=models.CASCADE,
        related_name='order_items',
    )
    item = models.ForeignKey(
        Item, verbose_name='Товар', on_delete=models.CASCADE
    )
    amount = models.PositiveIntegerField(
        'Количество', validators=[MinValueValidator(1)]
    )

    class Meta:
        verbose_name = 'Товар заказа'
        verbose_name_plural = 'Товары заказа'
        constraints = [
            models.UniqueConstraint(
                fields=['order', 'item'],
                name='unique_order_items)',
            ),
        ]
