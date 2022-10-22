import feedparser
from celery import Celery
from transmission_rpc import Client

from rss.models import Feed, Torrent, TransmissionClient

app = Celery("rss")


@app.task
def fetch_feeds():
    feeds = Feed.objects.all()
    for feed in feeds:
        parse_feed.delay(feed_id=feed.id)


@app.task
def parse_feed(feed_id: int):
    feed = Feed.objects.get(id=feed_id)
    d = feedparser.parse(feed.url)

    for item in d["items"]:
        torrent, created = Torrent.objects.get_or_create(
            title=item["title"], link=item["link"]
        )

        if created:
            for client in feed.transmission_clients.all():
                add_torrent.delay(
                    torrent_id=torrent.id,
                    client_id=client.id,
                    download_dir=feed.download_dir,
                )


@app.task
def add_torrent(torrent_id: int, client_id: int, download_dir: str):
    torrent = Torrent.objects.get(id=torrent_id)
    tc = TransmissionClient.objects.get(id=client_id)

    rpc_client = Client(
        host=tc.host, port=tc.port, username=tc.username, password=tc.password
    )

    rpc_client.add_torrent(torrent.link, download_dir=download_dir)
