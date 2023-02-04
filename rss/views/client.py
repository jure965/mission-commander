from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from rss.forms import TransmissionClientForm
from rss.models import TransmissionClient


class ClientListView(LoginRequiredMixin, ListView):
    paginate_by = 15
    template_name = "rss/client/list.html"
    model = TransmissionClient
    context_object_name = "clients"


class ClientCreateView(LoginRequiredMixin, CreateView):
    template_name = "rss/client/create.html"
    model = TransmissionClient
    form_class = TransmissionClientForm
    success_url = reverse_lazy("client-list")


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "rss/client/update.html"
    model = TransmissionClient
    form_class = TransmissionClientForm
    success_url = reverse_lazy("client-list")


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "rss/client/delete.html"
    model = TransmissionClient
    success_url = reverse_lazy("client-list")
