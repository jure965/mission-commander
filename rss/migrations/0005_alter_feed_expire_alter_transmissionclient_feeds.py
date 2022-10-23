# Generated by Django 4.1.2 on 2022-10-22 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "rss",
            "0004_remove_torrent_contents_remove_torrent_info_hash_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="feed",
            name="expire",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="transmissionclient",
            name="feeds",
            field=models.ManyToManyField(
                blank=True, related_name="transmission_clients", to="rss.feed"
            ),
        ),
    ]