from typing import List

import feedparser
import zoneinfo

from datetime import datetime
from time import mktime

from transmission_rpc import Client

from rss.models import Feed, Torrent, TransmissionClient


def preprocess(entries):
    utc = zoneinfo.ZoneInfo("Etc/UTC")
    for entry in entries:
        # add proper timezone aware datetime property from time_struct
        timestamp = mktime(entry.published_parsed)
        entry.pub = datetime.fromtimestamp(timestamp).replace(tzinfo=utc)


def do_parse_feed(feed: Feed) -> List[Torrent]:
    d = feedparser.parse(feed.url)

    preprocess(d.entries)

    if feed.chronological:
        d.entries.sort(key=lambda x: x.pub)

    if feed.regex_filter:
        d.entries = [e for e in d.entries if feed.regex_filter.search(e.title)]

    if feed.ignore_older_than:
        d.entries = [e for e in d.entries if e.pub > feed.ignore_older_than]

    if feed.ignore_newer_than:
        d.entries = [e for e in d.entries if e.pub < feed.ignore_newer_than]

    torrents = []

    for entry in d.entries:
        torrents.append(
            Torrent.objects.get_or_create(
                title=entry.title,
                link=entry.link,
                published=entry.pub,
            )
        )

    # return only newly created torrents
    return [t[0] for t in torrents if t[1]]


def do_send_torrents(torrent_ids, client_id, download_dir, start_paused):
    if not torrent_ids:
        return

    tc = TransmissionClient.objects.get(id=client_id)

    rpc_client = Client(
        protocol=tc.protocol,
        host=tc.host,
        port=tc.port,
        username=tc.username,
        password=tc.password,
        path=tc.rpc_path,
    )

    for torrent_id in torrent_ids:
        torrent = Torrent.objects.get(id=torrent_id)
        rpc_client.add_torrent(
            torrent.link, download_dir=download_dir or None, paused=start_paused
        )
