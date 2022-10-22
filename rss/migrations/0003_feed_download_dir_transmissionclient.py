# Generated by Django 4.1.2 on 2022-10-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rss", "0002_feed_torrent_seen"),
    ]

    operations = [
        migrations.AddField(
            model_name="feed",
            name="download_dir",
            field=models.CharField(blank=True, max_length=2048),
        ),
        migrations.CreateModel(
            name="TransmissionClient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("host", models.CharField(max_length=2048)),
                ("port", models.CharField(max_length=10)),
                ("username", models.CharField(max_length=2048)),
                ("password", models.CharField(max_length=2048)),
                (
                    "feeds",
                    models.ManyToManyField(
                        related_name="transmission_clients", to="rss.feed"
                    ),
                ),
            ],
        ),
    ]