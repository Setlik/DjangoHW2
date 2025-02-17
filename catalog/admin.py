from django.contrib import admin
from .models import Product, Category, Contact


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "description")
    list_filter = ("category", "name")
    search_fields = ("name", "description")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)
