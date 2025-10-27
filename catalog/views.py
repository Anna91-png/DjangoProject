from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from catalog.models import Category, Product
from catalog.forms import ProductForm
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


class CategoryProductListView(ListView):
    template_name = "catalog/products_by_category.html"
    context_object_name = "products"

    def get_queryset(self):
        category_slug = self.kwargs["slug"]
        return get_cached_products_by_category(category_slug)


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")


def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})


def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.owner = request.user
        product.save()
        return redirect("catalog:product_list")
    return render(request, "catalog/product_form.html", {"form": form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user == product.owner or request.user.has_perm('catalog.delete_product'):
        product.delete()
        return redirect("catalog:product_list")
    raise PermissionDenied


def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.user.has_perm('catalog.can_unpublish_product'):
        product.is_published = False
        product.save()
        return redirect("catalog:product_list")
    raise PermissionDenied
