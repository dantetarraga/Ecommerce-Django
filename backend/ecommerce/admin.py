from django.contrib import admin

from .models import (Brand, Category, Inventory, Order, OrderDetail, Product,
                     ProductSize, Size, User)

# Register your models here.

models = [Brand, Category, Inventory, Order, OrderDetail, Product, ProductSize, Size, User]

admin.site.register(models)

