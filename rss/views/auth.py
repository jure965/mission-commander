from django.contrib.auth.views import (
    LoginView as BuiltinLoginView,
    LogoutView as BuiltinLogoutView,
)
from django.urls import reverse_lazy

from rss.forms.login import LoginForm


class LoginView(BuiltinLoginView):
    template_name = "auth/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("feed-list")


class LogoutView(BuiltinLogoutView):
    next_page = reverse_lazy("login")
