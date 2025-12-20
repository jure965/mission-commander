from django.db import models
from django_celery_beat.models import PeriodicTask


class Feed(models.Model):
    enabled = models.BooleanField(default=True)
    name = models.CharField(max_length=2048, blank=True)
    url = models.URLField()
    regex_filter = models.CharField(max_length=2048, blank=True)
    expires_at = models.DateTimeField(
        blank=True, null=True, help_text="Skip feed fetch after this date"
    )
    download_dir = models.CharField(max_length=2048, blank=True)
    ignore_older_than = models.DateTimeField(
        blank=True, null=True, help_text="Ignore older torrents than this date"
    )
    ignore_newer_than = models.DateTimeField(
        blank=True, null=True, help_text="Ignore newer torrents than this date"
    )
    start_paused = models.BooleanField(default=False, help_text="Start torrents paused")
    chronological = models.BooleanField(
        default=True, help_text="Add torrents in chronological order"
    )
    transmission_clients = models.ManyToManyField(
        to="rss.TransmissionClient", related_name="feeds", blank=True
    )
    last_activity = models.DateTimeField(blank=True, null=True)
    last_added = models.DateTimeField(blank=True, null=True, default=None)

    periodic_task = models.OneToOneField(
        to=PeriodicTask,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.url}"
