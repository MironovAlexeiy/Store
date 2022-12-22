from django.contrib import admin

from .models import Basket, Category, Products

admin.site.register(Category)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    """
    Регистрация таблицы "Товара" в адимн-панели
    и настройка отображения
    """
    list_display = ('title', 'price', 'quantity', )
    fields = ('title', 'description', ('price', 'quantity'), 'category', 'image', )
    search_fields = ('title', 'description', )


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created')
    readonly_fields = ('created', )
    extra = 0
