from django.db import models


class Torrent(models.Model):
    title = models.CharField(max_length=2048)
    info_hash = models.CharField(max_length=2048)
    contents = models.TextField()
    link = models.URLField()
    seen = models.DateTimeField(null=True, blank=True, default=None)


class Feed(models.Model):
    url = models.URLField()
    expire = models.DateTimeField()
    download_dir = models.CharField(max_length=2048, blank=True)


class TransmissionClient(models.Model):
    host = models.CharField(max_length=2048)
    port = models.CharField(max_length=10)
    username = models.CharField(max_length=2048)
    password = models.CharField(max_length=2048)
    feeds = models.ManyToManyField(Feed, related_name="transmission_clients")
