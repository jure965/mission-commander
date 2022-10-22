from django.db import models


class Torrent(models.Model):
    title = models.CharField(max_length=2048)
    link = models.URLField()

    def __str__(self):
        return f"{self.title}"


class TransmissionClient(models.Model):
    host = models.CharField(max_length=2048)
    port = models.CharField(max_length=10)
    username = models.CharField(max_length=2048)
    password = models.CharField(max_length=2048)

    def __str__(self):
        return f"{self.host}:{self.port}"


class Feed(models.Model):
    url = models.URLField()
    expire = models.DateTimeField(blank=True, null=True)
    download_dir = models.CharField(max_length=2048, blank=True)
    transmission_clients = models.ManyToManyField(
        TransmissionClient, related_name="feeds", blank=True
    )

    def __str__(self):
        return f"{self.url}"
