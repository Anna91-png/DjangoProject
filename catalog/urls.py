from django.urls import path
from .views import (
    HomeView, ContactsView,
    ProductDetailView,
    ProductCreateView, ProductUpdateView, ProductDeleteView,
    CategoryProductListView
)

app_name = "catalog"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('contacts/', ContactsView.as_view(), name='contacts'),  # Контакты

    # CRUD для продуктов
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    # Отображение по категории
    path("category/<slug:slug>/", CategoryProductListView.as_view(), name="products_by_category"),
]
