from django.urls import path
from catalog.views import product_list, contact, product_info

urlpatterns = [
    path('', product_list, name='product_list'),
    path('products/<int:pk>/', product_info, name='product_info'),
    path('contacts/', contact, name='contacts'),
    # path('products/', product, name='products'),

]
