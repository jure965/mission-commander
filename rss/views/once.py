from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


from rss.forms import FeedForm
from rss.models import Feed
from rss.utils.feed import do_parse_feed, do_send_torrents


class OnceCreateView(LoginRequiredMixin, CreateView):
    template_name = "rss/once/create.html"
    model = Feed
    form_class = FeedForm
    success_url = reverse_lazy("feed-list")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            feed = form.instance
            clients = form.cleaned_data["transmission_clients"].all()
            # todo async
            torrents = do_parse_feed(feed)
            torrent_ids = [t.id for t in torrents]
            for client in clients:
                do_send_torrents(
                    torrent_ids=torrent_ids,
                    client_id=client.id,
                    download_dir=feed.download_dir,
                    start_paused=feed.start_paused,
                )
            return redirect("feed-list")
        else:
            return self.form_invalid(form)
