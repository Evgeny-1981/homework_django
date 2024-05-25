from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('contacts/', contact, name='contacts'),

]
