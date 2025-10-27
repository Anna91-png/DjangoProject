from catalog.models import Product
from django.core.cache import cache


def get_cached_products_by_category(category_slug):
    """
    Возвращает список продуктов из кеша, если он есть.
    Иначе — делает запрос к базе и сохраняет результат в кеш.
    """
    cache_key = f"products_category_{category_slug}"
    products = cache.get(cache_key)

    if products is None:
        products = Product.objects.filter(category__slug=category_slug, is_published=True)
        cache.set(cache_key, products, timeout=600)  # 10 минут

    return products
