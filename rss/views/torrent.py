from django.views.generic import TemplateView


class TorrentListView(TemplateView):
    template_name = "rss/torrent_list.html"
