from django.views.generic import TemplateView


class FeedListView(TemplateView):
    template_name = "rss/feed_list.html"


class TorrentListView(TemplateView):
    template_name = "rss/torrent_list.html"


class ClientListView(TemplateView):
    template_name = "rss/client_list.html"
