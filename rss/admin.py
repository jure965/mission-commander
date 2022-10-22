from django.contrib import admin

from rss.models import Torrent


@admin.register(Torrent)
class TorrentAdmin(admin.ModelAdmin):
    pass
