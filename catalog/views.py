from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    """Контроллер отображения домашней страницы"""
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


def contact(request):
    """Контроллер отображения страницы с контактами"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя:{name}, тел.:{phone}, сообщение: {message}')
    return render(request, 'catalog/contacts.html')
