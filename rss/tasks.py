from celery import Celery

from rss.models import Feed
from rss.utils import feed_utils

app = Celery("rss")


@app.task
def fetch_feeds():
    feeds = Feed.objects.filter(enabled=True)

    for feed in feeds:
        parse_feed.delay(feed_id=feed.pk)


@app.task
def parse_feed(feed_id: int):
    torrents = feed_utils.parse_feed(feed_id)
    for torrent in torrents:
        send_torrent.delay(torrent_id=torrent.id)


@app.task
def send_torrent(torrent_id: int):
    feed_utils.send_torrent(torrent_id=torrent_id)
