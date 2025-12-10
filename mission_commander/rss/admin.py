from django.contrib import admin, messages
from django.utils.translation import ngettext

from mission_commander.rss.models import Torrent, Feed, TransmissionClient
from mission_commander.rss.tasks import parse_feed


@admin.register(Torrent)
class TorrentAdmin(admin.ModelAdmin):
    pass


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    actions = ["fetch_selected_feeds"]

    @admin.action(description="Fetch and parse selected feeds")
    def fetch_selected_feeds(self, request, queryset):
        for feed in queryset:
            parse_feed.delay(feed_id=feed.pk)

        count = queryset.count()

        message = ngettext(
            "Running %(count)d feed fetch job.",
            "Running %(count)d feed fetch jobs.",
            count,
        ) % {"count": count}

        self.message_user(request, message, messages.SUCCESS)


@admin.register(TransmissionClient)
class TransmissionClientAdmin(admin.ModelAdmin):
    pass
