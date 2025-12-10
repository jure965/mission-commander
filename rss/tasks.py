from typing import List

from celery import Celery
from django.utils import timezone

from rss.models import Feed
from rss.utils.feed import do_parse_feed, do_send_torrents

app = Celery("rss")


@app.task
def fetch_feeds():
    feeds = Feed.objects.filter(enabled=True)

    for feed in feeds:
        parse_feed.delay(feed_id=feed.pk)


@app.task
def parse_feed(feed_id: int):
    feed = Feed.objects.get(id=feed_id)

    if not feed.transmission_clients.exists():
        return

    now = timezone.now()
    if feed.expires_at is not None and feed.expires_at < now:
        feed.enabled = False
        feed.save()
        return

    torrents = do_parse_feed(feed)

    feed.last_activity = timezone.now()
    feed.save()

    if not torrents:
        return

    feed.last_added = timezone.now()
    feed.save()

    torrent_ids = [t.pk for t in torrents]

    clients = feed.transmission_clients.all()

    for client in clients:
        send_torrents.delay(
            torrent_ids=torrent_ids,
            client_id=client.pk,
            download_dir=feed.download_dir,
            start_paused=feed.start_paused,
        )


@app.task
def send_torrents(
    torrent_ids: List, client_id: int, download_dir: str, start_paused: bool
):
    do_send_torrents(
        torrent_ids=torrent_ids,
        client_id=client_id,
        download_dir=download_dir,
        start_paused=start_paused,
    )
