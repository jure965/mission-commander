from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import (
    LoginView as BuiltinLoginView,
    LogoutView as BuiltinLogoutView,
)
from django.urls import reverse_lazy


class LoginView(BuiltinLoginView):
    template_name = "rss/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("feed-list")


class LogoutView(BuiltinLogoutView):
    next_page = reverse_lazy("login")
