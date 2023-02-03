from django.contrib.auth import logout
from django.contrib.auth.views import LoginView as BuiltinLoginView
from django.shortcuts import redirect
from django.views import View


class LoginView(BuiltinLoginView):
    template_name = "rss/login.html"


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/login/")
