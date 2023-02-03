from django.contrib.auth.views import (
    LoginView as BuiltinLoginView,
    LogoutView as BuiltinLogoutView,
)
from django.urls import reverse_lazy


class LoginView(BuiltinLoginView):
    template_name = "rss/login.html"


class LogoutView(BuiltinLogoutView):
    next_page = reverse_lazy("login")
