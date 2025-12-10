import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


from rss.forms import FeedForm
from rss.models import Feed
from rss.utils.feed import do_parse_feed

from rss.tasks import send_torrents

logger = logging.getLogger(__name__)


class OnceCreateView(LoginRequiredMixin, CreateView):
    template_name = "rss/once/create.html"
    model = Feed
    form_class = FeedForm
    success_url = reverse_lazy("feed-list")

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if not form.is_valid():
            return self.form_invalid(form)

        feed = form.instance
        clients = form.cleaned_data["transmission_clients"].all()

        torrents = do_parse_feed(feed)

        for torrent in torrents:
            logger.info(f"Found torrent {torrent.title}")

        torrent_ids = [t.pk for t in torrents]

        for client in clients:
            send_torrents.delay(
                torrent_ids=torrent_ids,
                client_id=client.pk,
                download_dir=feed.download_dir,
                start_paused=feed.start_paused,
            )

        return redirect("torrent-list")
