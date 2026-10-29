from django import forms
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Benutzername",
        widget=forms.TextInput(attrs={"class": "form-control", "autofocus": True}),
    )
    password = forms.CharField(
        label="Passwort",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class LoginView(auth_views.LoginView):
    template_name = "registration/login.html"
    authentication_form = BootstrapAuthenticationForm


class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy("login")


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "core/home.html"
