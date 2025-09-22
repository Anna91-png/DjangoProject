from django.shortcuts import render

# Контроллер для главной страницы
def home_view(request):
    return render(request, 'catalog/home.html')

# Контроллер для страницы контактов
def contacts_view(request):
    return render(request, 'catalog/contacts.html')
