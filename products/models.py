from django.db import models

from users.models import User


class Category(models.Model):
    """
    Модель описывающая таблицу 'Категория' в БД
    """
    title = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Products(models.Model):
    """
    Модель описывающая таблицу 'Товары' в БД
    """
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey(to=Category, on_delete=models.SET_DEFAULT, default='Category not set', db_index=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'Товар: {self.title} | Категория: {self.category.title}'


class BasketQuerySet(models.QuerySet):

    def total_sum(self):
        return sum(item.get_sum() for item in self)

    def total_quantity(self):
        return sum(item.quantity for item in self)


class Basket(models.Model):
    """
    Модель описывающая карзину товаров
    """
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Товар: {self.product.title}'

    def get_sum(self):
        return self.quantity * self.product.price

    def de_json(self):
        basket_item = {
            'product_name': self.product.title,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.get_sum())
        }
        return basket_item
