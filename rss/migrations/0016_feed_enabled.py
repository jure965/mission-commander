# Generated by Django 4.1.6 on 2023-02-05 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rss", "0015_feed_last_activity_feed_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="feed",
            name="enabled",
            field=models.BooleanField(default=True),
        ),
    ]