from django.db import models


class Torrent(models.Model):
    title = models.CharField(max_length=2048)
    link = models.URLField()
    published = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
