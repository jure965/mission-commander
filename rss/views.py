from django.contrib.auth import logout
from django.contrib.auth.views import LoginView as BuiltinLoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from rss.forms import TransmissionClientForm
from rss.models import TransmissionClient


class FeedListView(TemplateView):
    template_name = "rss/feed_list.html"


class TorrentListView(TemplateView):
    template_name = "rss/torrent_list.html"


class ClientListView(ListView):
    template_name = "rss/client_list.html"
    model = TransmissionClient
    context_object_name = "clients"


class ClientCreateView(CreateView):
    template_name = "rss/client_create.html"
    model = TransmissionClient
    form_class = TransmissionClientForm
    success_url = reverse_lazy("client-list")


class ClientUpdateView(UpdateView):
    template_name = "rss/client_update.html"
    model = TransmissionClient
    form_class = TransmissionClientForm
    success_url = reverse_lazy("client-list")


class ClientDeleteView(DeleteView):
    template_name = "rss/client_delete.html"
    model = TransmissionClient
    success_url = reverse_lazy("client-list")


class LoginView(BuiltinLoginView):
    template_name = "rss/login.html"


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/login/")
