from django.core.cache import cache

from .models import Product
from config.settings import CACHES

def get_products_by_category(category_name):
    """Возвращает список продуктов по заданной категории."""
    return Product.objects.filter(category=category_name)


def get_products_from_cache():
    """Получаем данные по продуктам из кэша"""
    if not CACHES:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products
