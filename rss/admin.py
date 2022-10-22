from django.contrib import admin

from rss.models import Torrent, Feed, TransmissionClient


@admin.register(Torrent)
class TorrentAdmin(admin.ModelAdmin):
    pass


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    pass


@admin.register(TransmissionClient)
class TransmissionClientAdmin(admin.ModelAdmin):
    pass
