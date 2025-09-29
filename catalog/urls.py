from django.urls import path
from .views import home, contacts_view

urlpatterns = [
    path("", home, name="home"),              # Главная страница
    path("contacts/", contacts_view, name="contacts"),  # Контакты
]
