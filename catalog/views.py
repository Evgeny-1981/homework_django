from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def product_list(request):
    """Контроллер отображения домашней страницы"""
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/product_list.html', context)


def contact(request):
    """Контроллер отображения страницы с контактами"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, телефон: {phone}, сообщение: {message}')
    return render(request, 'catalog/contacts.html')


def product_info(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product_info.html', context)

