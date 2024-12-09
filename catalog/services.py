from config.settings import CACHE_ENABLED
from catalog.models import Category
from django.core.cache import cache


def get_categoryes_list():
    """получает данные по категориям из кэша"""
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = "categoryes_list"
    categoryes = cache.get(key)
    if categoryes is not None:
        return categoryes
    categoryes = Category.objects.all()
    cache.set(key, categoryes)
    return categoryes
