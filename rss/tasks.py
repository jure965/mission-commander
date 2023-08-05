from typing import List

from celery import Celery
from django.utils import timezone

from rss.models import Feed
from rss.utils.feed import do_parse_feed, do_send_torrents

app = Celery("rss")


@app.task
def fetch_feeds():
    now = timezone.now()
    feeds = Feed.objects.exclude(expires_at__lt=now, enabled=False)

    for feed in feeds:
        parse_feed.delay(feed_id=feed.id)


@app.task
def parse_feed(feed_id: int):
    feed = Feed.objects.get(id=feed_id)

    if not feed.transmission_clients.exists():
        return

    torrents = do_parse_feed(feed)

    if not torrents:
        return

    torrent_ids = [t.id for t in torrents]

    clients = feed.transmission_clients.all()

    for client in clients:
        send_torrents.delay(
            torrent_ids=torrent_ids,
            client_id=client.id,
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
