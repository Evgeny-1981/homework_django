from django.shortcuts import render


def home(request):
    """Контроллер отображения домашней страницы"""
    return render(request, 'catalog/home.html')


def contact(request):
    """Контроллер отображения страницы с контактами"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, телефон: {phone}, сообщение: {message}')
    return render(request, 'catalog/contacts.html')
