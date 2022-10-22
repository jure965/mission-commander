from django.db import models


class Torrent(models.Model):
    title = models.CharField(max_length=2048)
    info_hash = models.CharField(max_length=2048)
    contents = models.TextField()
    link = models.URLField()
