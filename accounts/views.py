from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import CustomRegisterForm, CustomLoginForm
from .models import CustomUser

class CustomRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = CustomRegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        send_mail(
            'Добро пожаловать!',
            'Вы успешно зарегистрировались.',
            'noreply@example.com',
            [user.email],
        )
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = CustomLoginForm
