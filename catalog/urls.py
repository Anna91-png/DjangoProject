from django.urls import path
from .views import HomeView, ContactsView, product_list

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('products/', product_list, name='product_list'),
]
