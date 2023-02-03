from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from rss.forms import TransmissionClientForm
from rss.models import TransmissionClient


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
