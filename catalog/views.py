from django.shortcuts import render

def home(request):
    """Контроллер отображения домашней страницы"""
    return render(request, 'catalog/home.html')

def contact(request):
    """Контроллер отображения страницы с контактами"""
    return render(request, 'catalog/contacts.html')