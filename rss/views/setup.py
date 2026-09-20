from typing import Any

from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from rss.forms.setup import SetupForm

User = get_user_model()


class SetupView(FormView):
    template_name = "setup/setup.html"
    form_class = SetupForm
    success_url = reverse_lazy("login")

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if User.objects.all().count():
            # users already exists, redirect to login page
            return redirect("login")

        return super().get(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if User.objects.all().count():
            # users already exists, redirect to login page
            return redirect("login")

        return super().post(request, *args, **kwargs)

    def form_valid(self, form: SetupForm) -> HttpResponse:
        username = str(form.data.get("username"))
        password = str(form.data.get("password"))

        User.objects.create_superuser(
            username=username,
            password=password,
        )

        return super().form_valid(form)
