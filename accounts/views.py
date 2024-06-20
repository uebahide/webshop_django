from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import User
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

class HomeView(TemplateView):
    template_name = 'accounts/home.html'

class UserRegisterView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    success_message = 'Registration has been completed successfully.'

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = UserLoginForm

    def form_valid(self, form: AuthenticationForm):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(86400)
        return super().form_valid(form)

class UserLogoutView(LogoutView):
    pass

