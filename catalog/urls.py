from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (contact, ProductDetailView, ProductListView, ContactsView, BlogListView, BlogDetailView,
                           BlogCreateView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_info'),
    path('contacts/', ContactsView.as_view(), name='contacts'),

    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_info'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),

]
