from django.urls import path
from .views import CustomRegisterView, CustomLoginView

urlpatterns = [
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
