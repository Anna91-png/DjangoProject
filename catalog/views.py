from django.shortcuts import render, get_object_or_404
from .models import Product, Category   # если у тебя есть модель Category

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'catalog/home.html', {
        'categories': categories,
        'products': products,
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

def contacts(request):
    return render(request, 'catalog/contacts.html')

