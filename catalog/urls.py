from django.urls import path

from .apps import CatalogConfig
from .views import HomeView, ContactsView, product_list

app_name = CatalogConfig.name
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/', product_list, name='product_list'),
]

