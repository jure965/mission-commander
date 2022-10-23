# Generated by Django 4.1.2 on 2022-10-23 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rss", "0007_torrent_published"),
    ]

    operations = [
        migrations.AddField(
            model_name="feed",
            name="ignore_older_than",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="transmissionclient",
            name="name",
            field=models.CharField(default="", max_length=2048),
        ),
    ]
