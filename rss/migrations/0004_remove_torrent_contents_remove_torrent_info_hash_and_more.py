# Generated by Django 4.1.2 on 2022-10-22 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rss", "0003_feed_download_dir_transmissionclient"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="torrent",
            name="contents",
        ),
        migrations.RemoveField(
            model_name="torrent",
            name="info_hash",
        ),
        migrations.RemoveField(
            model_name="torrent",
            name="seen",
        ),
    ]