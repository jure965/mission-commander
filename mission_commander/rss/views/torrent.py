from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from mission_commander.rss.models import Torrent


class TorrentListView(LoginRequiredMixin, ListView):
    paginate_by = 15
    template_name = "rss/torrent/list.html"
    model = Torrent
    context_object_name = "torrents"


class TorrentDetailView(LoginRequiredMixin, DetailView):
    template_name = "rss/torrent/details.html"
    model = Torrent
