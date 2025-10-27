from catalog.models import Product
from django.core.cache import cache

def get_cached_products_by_category(category_slug):
    cache_key = f"products_category_{category_slug}"
    products = cache.get(cache_key)

    if products is None:
        products = Product.objects.filter(category__slug=category_slug, is_published=True)
        cache.set(cache_key, products, 60 * 10)  # 10 минут

    return products

def get_products_by_category(category_slug):
    return Product.objects.filter(category__slug=category_slug, is_published=True)
