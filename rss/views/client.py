from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from rss.forms import TorrentClientForm
from rss.models import TorrentClient


class ClientListView(LoginRequiredMixin, ListView):
    paginate_by = 15
    template_name = "client/list.html"
    model = TorrentClient
    context_object_name = "clients"


class ClientCreateView(LoginRequiredMixin, CreateView):
    template_name = "client/create.html"
    model = TorrentClient
    form_class = TorrentClientForm
    success_url = reverse_lazy("client-list")


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "client/update.html"
    model = TorrentClient
    form_class = TorrentClientForm
    success_url = reverse_lazy("client-list")


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "client/delete.html"
    model = TorrentClient
    success_url = reverse_lazy("client-list")
