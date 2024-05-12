from django.urls import path
from catalog.views import home, contact, product

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contact, name='contacts'),
    path('products/', product, name='products'),

]
