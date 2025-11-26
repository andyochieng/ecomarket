from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'seller', 'price', 'is_verified', 'is_featured']
    list_filter = ['category', 'is_verified', 'is_featured']
    search_fields = ['name', 'description']
    list_editable = ['is_verified', 'is_featured']