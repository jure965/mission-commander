from django.db import models


class Torrent(models.Model):
    title = models.CharField(max_length=2048)
    link = models.URLField()
    published = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    torrent_client = models.ForeignKey(
        to="rss.TorrentClient",
        related_name="torrents",
        blank=True,
        default=None,
        null=True,
        on_delete=models.SET_NULL,
    )
    feed = models.ForeignKey(
        to="rss.Feed",
        related_name="torrents",
        blank=True,
        default=None,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = ("-created_at", "-published")

    def __str__(self):
        return f"{self.title}"
