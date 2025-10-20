from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import CustomUserCreationForm

class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        send_mail(
            'Добро пожаловать!',
            'Спасибо за регистрацию в нашем магазине.',
            'your_email@example.com',
            [user.email],
            fail_silently=False,
        )
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
