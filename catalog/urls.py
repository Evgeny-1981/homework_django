from django.urls import path
from catalog.views import home, contact

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contact, name='contacts'),

]
