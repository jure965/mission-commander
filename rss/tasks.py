from datetime import datetime
from time import mktime
import pytz

import feedparser
from celery import Celery
from django.utils import timezone
from transmission_rpc import Client

from rss.models import Feed, Torrent, TransmissionClient

app = Celery("rss")


@app.task
def fetch_feeds():
    now = timezone.now()
    feeds = Feed.objects.exclude(expires_at__lt=now)

    for feed in feeds:
        parse_feed.delay(feed_id=feed.id)


@app.task
def parse_feed(feed_id: int):
    feed = Feed.objects.get(id=feed_id)
    d = feedparser.parse(feed.url)

    for entry in d.entries:
        timestamp = mktime(entry.published_parsed)
        published = datetime.fromtimestamp(timestamp).replace(tzinfo=pytz.UTC)

        if feed.ignore_older_than and published < feed.ignore_older_than:
            continue

        if feed.ignore_newer_than and published > feed.ignore_newer_than:
            continue

        torrent, created = Torrent.objects.get_or_create(
            title=entry.title,
            link=entry.link,
            published=published,
        )

        if created:
            for client in feed.transmission_clients.all():
                add_torrent.delay(
                    torrent_id=torrent.id,
                    client_id=client.id,
                    download_dir=feed.download_dir,
                )


@app.task
def add_torrent(torrent_id: int, client_id: int, download_dir: str, start_paused: bool):
    torrent = Torrent.objects.get(id=torrent_id)
    tc = TransmissionClient.objects.get(id=client_id)

    rpc_client = Client(
        protocol=tc.protocol,
        host=tc.host,
        port=tc.port,
        username=tc.username,
        password=tc.password,
        path=tc.rpc_path,
    )

    rpc_client.add_torrent(torrent.link, download_dir=download_dir, paused=start_paused)
