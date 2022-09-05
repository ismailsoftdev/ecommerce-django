from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    # list_editable = ['price', 'available']