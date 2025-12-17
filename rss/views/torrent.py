from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from rss.models import Torrent


class TorrentListView(LoginRequiredMixin, ListView):
    paginate_by = 15
    template_name = "torrent/list.html"
    model = Torrent
    context_object_name = "torrents"


class TorrentDetailView(LoginRequiredMixin, DetailView):
    template_name = "torrent/details.html"
    model = Torrent
