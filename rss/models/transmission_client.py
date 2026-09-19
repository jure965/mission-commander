from django.db import models


class TransmissionClient(models.Model):
    class ClientType(models.TextChoices):
        TRANSMISSION = "transmission", "transmission"
        QBITTORRENT = "qbittorrent", "qbittorrent"

    class Protocol(models.TextChoices):
        HTTP = "http", "http"
        HTTPS = "https", "https"

    name = models.CharField(max_length=2048, default="transmission")
    protocol = models.CharField(
        max_length=10, choices=Protocol.choices, default=Protocol.HTTP
    )
    host = models.CharField(max_length=2048)
    port = models.CharField(max_length=10, default="9091")
    username = models.CharField(max_length=2048, blank=True)
    password = models.CharField(max_length=2048, blank=True)
    rpc_path = models.CharField(max_length=2048, default="/transmission/")
    client_type = models.CharField(
        max_length=50, choices=ClientType.choices, default=ClientType.TRANSMISSION
    )

    def __str__(self):
        return f"{self.name} ({self.host}:{self.port})"  # noqa: E231
