from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact, product_info, products_list

app_name = CatalogConfig.name

urlpatterns = [
    path('', products_list, name='product_list'),
    path('products/<int:pk>/', product_info, name='product_info'),
    path('contacts/', contact, name='contacts'),

]
