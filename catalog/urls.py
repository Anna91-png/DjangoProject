from django.urls import path
from .views import (
    HomeView, ContactsView,
    product_list,  # ✅ функция вместо отсутствующего ProductListView
    ProductDetailView,
    ProductCreateView, ProductUpdateView, ProductDeleteView,
    CategoryProductListView,  # ✅ добавлен для отображения по категории
    create_product, delete_product, unpublish_product  # ✅ доп. функции
)

app_name = "catalog"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('contacts/', ContactsView.as_view(), name='contacts'),  # Контакты

    # Список продуктов
    path('products/', product_list, name='product_list'),

    # CRUD для продуктов
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    # Отображение по категории
    path("category/<slug:slug>/", CategoryProductListView.as_view(), name="products_by_category"),

    # Доп. действия
    path("products/<int:pk>/unpublish/", unpublish_product, name="product_unpublish"),
    path("products/<int:pk>/delete-confirm/", delete_product, name="product_delete_confirm"),
    path("products/create-manual/", create_product, name="product_create_manual"),
]
