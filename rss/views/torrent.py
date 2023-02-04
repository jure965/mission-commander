from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from rss.models import Torrent


class TorrentListView(LoginRequiredMixin, ListView):
    template_name = "rss/torrent/list.html"
    model = Torrent
    context_object_name = "torrents"


class TorrentDetailView(LoginRequiredMixin, DetailView):
    template_name = "rss/torrent/details.html"
    model = Torrent
