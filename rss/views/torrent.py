from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from rss.forms.torrent import TorrentForm
from rss.models import Torrent


class TorrentListView(LoginRequiredMixin, ListView):
    paginate_by = 15
    template_name = "torrent/list.html"
    model = Torrent
    context_object_name = "torrents"


class TorrentDetailView(LoginRequiredMixin, DetailView):
    template_name = "torrent/details.html"
    model = Torrent


class TorrentCreateView(LoginRequiredMixin, CreateView):
    template_name = "torrent/create.html"
    model = Torrent
    form_class = TorrentForm
    success_url = reverse_lazy("torrent-list")


class TorrentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "torrent/update.html"
    model = Torrent
    form_class = TorrentForm
    success_url = reverse_lazy("torrent-detail")


class TorrentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "torrent/delete.html"
    model = Torrent
    success_url = reverse_lazy("torrent-list")
