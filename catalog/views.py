from django.shortcuts import render
from .models import Product, Category

def home(request):
    categories = Category.objects.all()
    category_products = {
        category.name: Product.objects.filter(category=category)
        for category in categories
    }
    return render(request, "catalog/home.html", {"category_products": category_products})

def contacts_view(request):
    return render(request, "catalog/contacts.html")
