from celery import Celery

from rss.utils import feed_utils

app = Celery("rss")


@app.task
def parse_feed(feed_id: int):
    torrents = feed_utils.parse_feed(feed_id)
    for torrent in torrents:
        send_torrent.delay(torrent_id=torrent.id)


@app.task
def send_torrent(torrent_id: int):
    feed_utils.send_torrent(torrent_id=torrent_id)
