from django.db import models


class Torrent(models.Model):
    title = models.CharField(max_length=2048)
    link = models.URLField()
    published = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"


class TransmissionClient(models.Model):
    name = models.CharField(max_length=2048, default="")
    host = models.CharField(max_length=2048)
    port = models.CharField(max_length=10)
    username = models.CharField(max_length=2048)
    password = models.CharField(max_length=2048)

    def __str__(self):
        return f"{self.name} ({self.host}:{self.port})"


class Feed(models.Model):
    url = models.URLField()
    expires_at = models.DateTimeField(blank=True, null=True, help_text="Skip feed fetch after this date")
    download_dir = models.CharField(max_length=2048, blank=True)
    ignore_older_than = models.DateTimeField(blank=True, null=True, help_text="Ignore older torrents than this date")
    ignore_newer_than = models.DateTimeField(blank=True, null=True, help_text="Ignore newer torrents than this date")
    transmission_clients = models.ManyToManyField(
        TransmissionClient, related_name="feeds", blank=True
    )

    def __str__(self):
        return f"{self.url}"
