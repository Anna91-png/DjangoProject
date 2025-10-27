from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin  # ✅ добавляем
from catalog.models import Category, Product
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from catalog.services.product_service import get_cached_products_by_category


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

class CategoryProductListView(ListView):
    template_name = "catalog/products_by_category.html"
    context_object_name = "products"

    def get_queryset(self):
        category_slug = self.kwargs["slug"]
        return get_cached_products_by_category(category_slug)

@method_decorator(cache_page(60 * 15), name='dispatch')  # 15 минут
class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

class ProductCreateView(LoginRequiredMixin, CreateView):  # ✅ доступ только авторизованным
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

class ProductUpdateView(LoginRequiredMixin, UpdateView):  # ✅ доступ только авторизованным
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

class ProductDeleteView(LoginRequiredMixin, DeleteView):  # ✅ доступ только авторизованным
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

def create_product(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save(commit=False)
        product.owner = request.user
        product.save()

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user == product.owner or request.user.has_perm('catalog.delete_product'):
        product.delete()
    else:
        raise PermissionDenied

def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user.has_perm('catalog.can_unpublish_product'):
        product.is_published = False
        product.save()
    else:
        raise PermissionDenied
