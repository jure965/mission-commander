import logging
import re
from typing import List

import feedparser
import zoneinfo

from datetime import datetime
from time import mktime

from django.utils import timezone

from rss.clients.backends import get_torrent_client
from rss.models import Feed, Torrent

logger = logging.getLogger(__name__)


def preprocess(entries):
    utc = zoneinfo.ZoneInfo("Etc/UTC")
    for entry in entries:
        # add proper timezone-aware datetime property from time_struct
        timestamp = mktime(entry.published_parsed)
        entry.pub = datetime.fromtimestamp(timestamp).replace(tzinfo=utc)


def get_torrents(feed: Feed) -> List[Torrent]:
    d = feedparser.parse(feed.url)

    preprocess(d.entries)

    if feed.chronological:
        d.entries.sort(key=lambda x: x.pub)

    if feed.regex_filter:
        re_filter = re.compile(feed.regex_filter)
        d.entries = [e for e in d.entries if re_filter.search(e.title)]

    if feed.ignore_older_than:
        d.entries = [e for e in d.entries if e.pub > feed.ignore_older_than]

    if feed.ignore_newer_than:
        d.entries = [e for e in d.entries if e.pub < feed.ignore_newer_than]

    torrents = []

    for entry in d.entries:
        for torrent_client in feed.torrent_clients.all():
            torrents.append(
                Torrent.objects.get_or_create(
                    title=entry.title,
                    link=entry.link,
                    published=entry.pub,
                    feed=feed,
                    torrent_client=torrent_client,
                )
            )

    # return only newly created torrents
    return [t[0] for t in torrents if t[1]]


def send_torrent(torrent_id):
    torrent = Torrent.objects.get(id=torrent_id)
    torrent_client = get_torrent_client(client=torrent.torrent_client)

    torrent_client.add_torrent(
        torrent=torrent.link,
        download_dir=torrent.feed.download_dir or None,
        paused=torrent.feed.start_paused,
    )

    logger.info(f"Sent torrent '{torrent.title}' to '{torrent_client.tc_info.name}'")


def parse_feed(feed_id):
    feed = Feed.objects.get(id=feed_id)

    if not feed.torrent_clients.exists():
        return None

    now = timezone.now()
    if feed.expires_at is not None and feed.expires_at < now:
        feed.enabled = False
        feed.save()
        return None

    torrents = get_torrents(feed)

    if not torrents:
        return None

    feed.last_activity = timezone.now()
    feed.save()

    feed.last_added = timezone.now()
    feed.save()

    return torrents
