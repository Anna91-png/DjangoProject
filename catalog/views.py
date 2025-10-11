from django.views.generic import TemplateView
from catalog.models import Category, Product

class HomeView(TemplateView):
    template_name = "catalog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        context['category_products'] = {
            category: Product.objects.filter(category=category)
            for category in categories
        }
        return context


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})
